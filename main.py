import base64
import json
import requests
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.backends import default_backend
import subprocess
from eth_abi import encode


def fix_base64_padding(b64_string):
    """Helper to fix base64url padding [base64url removes padding but decoder needs it]"""
    return b64_string + "=" * (-len(b64_string) % 4)


def get_signing_key(jku_url: str, target_kid: str):
    """
    Fetches the Azure attestation service's signing key - this is what signed the attestation report.
    The key is fetched from Azure's attestation service using:
    - jku_url: URL hosting the signing keys [attestation service endpoint]
    - target_kid: ID of specific key used [to find right key from set]
    """
    try:
        response = requests.get(
            jku_url
        )  # [Get the signing keys from Azure - list of public keys in JWKS format]
        response.raise_for_status()
        keys = response.json()["keys"]

        for key in keys:
            if (
                key.get("kid") == target_kid
            ):  # [Find the specific key used to sign this attestation via key ID]
                n = base64.urlsafe_b64decode(
                    fix_base64_padding(key["n"])
                )  # [Extract RSA key modulus]
                e = base64.urlsafe_b64decode(
                    fix_base64_padding(key["e"])
                )  # [Extract RSA key exponent]
                e_int = int.from_bytes(
                    e, byteorder="big"
                )  # [Convert bytes to integers - needed to construct RSA key]
                n_int = int.from_bytes(n, byteorder="big")

                pub_key = rsa.RSAPublicNumbers(e=e_int, n=n_int).public_key(
                    default_backend()
                )  # [Create RSA public key object for signature verification]
                return pub_key

        raise ValueError(f"No key found with kid: {target_kid}")

    except Exception as e:
        print(f"Error fetching signing key: {str(e)}")
        raise


def verify_azure_attestation(jwt: str):
    jwt_parts = jwt.split(".")  # [Split JWT into header, payload, signature parts]
    header_b64 = jwt_parts[0]  # [Base64url encoded header]
    payload_b64 = jwt_parts[1]  # [Base64url encoded attestation report]
    signature_b64 = jwt_parts[2]  # [Base64url encoded signature]

    message_to_verify = (
        f"{header_b64}.{payload_b64}".encode()
    )  # [Construct message that was signed - header.payload]
    signature = base64.urlsafe_b64decode(
        fix_base64_padding(signature_b64)
    )  # [Decode the signature bytes for verification]

    header_decoded = json.loads(
        base64.urlsafe_b64decode(fix_base64_padding(header_b64))
    )
    jku_url = header_decoded[
        "jku"
    ]  # [Get JKU (endpoint URL) from JWT header - tells us where to find signing key]
    kid = header_decoded[
        "kid"
    ]  # [Get KID from JWT header - Key ID that signed this attestation]

    signing_key = get_signing_key(
        jku_url, kid
    )  # [Fetch the specific signing key from Azure attestation service]

    key_info = signing_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    try:
        signing_key.verify(
            signature,
            message_to_verify,
            padding.PKCS1v15(),  # [RSA PKCS#1 v1.5 padding]
            hashes.SHA256(),  # [SHA-256 hash of message]
        )
        # print("Signature is valid!")  # [Attestation is genuine]
        return True
    except InvalidSignature:
        print("Invalid signature - verification failed")
        print("\nVerification details:")
        print(f"- Signature length: {len(signature)} bytes")
        print(f"- Message length: {len(message_to_verify)} bytes")
        print(f"- RSA key size: {signing_key.key_size} bits")
        return False
    except Exception as e:
        print("Other verification error:", str(e), type(e))
        return False


def get_signature_params(jwt: str):
    jwt_parts = jwt.split(".")
    header_b64 = jwt_parts[0]
    payload_b64 = jwt_parts[1]
    signature_b64 = jwt_parts[2]

    message_to_verify = f"{header_b64}.{payload_b64}".encode()
    signature = base64.urlsafe_b64decode(fix_base64_padding(signature_b64))

    header_decoded = json.loads(
        base64.urlsafe_b64decode(fix_base64_padding(header_b64))
    )
    jku_url = header_decoded["jku"]
    kid = header_decoded["kid"]

    signing_key = get_signing_key(jku_url, kid)

    signature_hex = signature.hex()
    message_hex = message_to_verify.hex()
    e_hex = signing_key.public_numbers().e.to_bytes(4, "big").hex()
    n_hex = signing_key.public_numbers().n.to_bytes(256, "big").hex()

    return message_hex, signature_hex, e_hex, n_hex


def get_price_from_cmc():
    url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
    headers = {"X-CMC_PRO_API_KEY": "a7712394-8f34-4e3f-9cfb-b0cf73eaf456"}
    params = {"symbol": "ETH"}
    response = requests.get(url, headers=headers, params=params)
    return response.json()["data"]["ETH"][0]["quote"]["USD"]["price"]


def get_attested_price():
    # 1. Get price from CMC API
    price = get_price_from_cmc()

    # 2. Call C++ attestation client with price
    proc = subprocess.run(
        [
            "sudo",
            "/home/jesserc/sevsnp-cvm/AttestationClient",  # Calls our C++ program
            "-p",
            str(price),
            "-o",
            "TOKEN",
            "-n",
            "coinmarketcap.com",
        ],
        capture_output=True,
    )
    jwt = proc.stdout.decode()

    # 3. Process JWT and get params for contract
    return jwt


if __name__ == "__main__":
    # Azure VM attestation report in JWT format
    jwt = get_attested_price()
    jwt = jwt.strip()

    is_valid = verify_azure_attestation(jwt)

    if not is_valid:
        raise Exception("Invalid attestation report")

    # Get signature parameters
    sig, msg, e, n = get_signature_params(jwt)

    # Convert hex strings to bytes for ABI encoding [needed for Solidity bytes type]
    sig_bytes = bytes.fromhex(sig)
    msg_bytes = bytes.fromhex(msg)
    e_bytes = bytes.fromhex(e)
    n_bytes = bytes.fromhex(n)

    # Encode params as (bytes, bytes, bytes, bytes) for Solidity
    encoded = encode(
        ["bytes", "bytes", "bytes", "bytes"], [sig_bytes, msg_bytes, e_bytes, n_bytes]
    )

    # Print encoded params for Foundry FFI use
    print(encoded.hex())
