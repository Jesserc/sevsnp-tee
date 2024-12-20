from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature
import base64
import requests
import json

jwt = "eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vc2hhcmVkZXVzMi5ldXMyLmF0dGVzdC5henVyZS5uZXQvY2VydHMiLCJraWQiOiJKMHBBUGRmWFhIcVdXaW1nckg4NTN3TUlkaDUvZkxlMXo2dVNYWVBYQ2EwPSIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzQ3NDc4OTQsImlhdCI6MTczNDcxOTA5NCwiaXNzIjoiaHR0cHM6Ly9zaGFyZWRldXMyLmV1czIuYXR0ZXN0LmF6dXJlLm5ldCIsImp0aSI6ImZhZWZiMjkxOGQyYjU3OTI4ZDFhYTVlOGZjMmNhMTg4ZDRmMTAxMTU4MzRiZGRjMTAxODFlOTI5YjE0MjA1YzUiLCJuYmYiOjE3MzQ3MTkwOTQsInNlY3VyZWJvb3QiOnRydWUsIngtbXMtYXR0ZXN0YXRpb24tdHlwZSI6ImF6dXJldm0iLCJ4LW1zLWF6dXJldm0tYXR0ZXN0YXRpb24tcHJvdG9jb2wtdmVyIjoiMi4wIiwieC1tcy1henVyZXZtLWF0dGVzdGVkLXBjcnMiOlswLDEsMiwzLDQsNSw2LDddLCJ4LW1zLWF6dXJldm0tYm9vdGRlYnVnLWVuYWJsZWQiOmZhbHNlLCJ4LW1zLWF6dXJldm0tZGJ2YWxpZGF0ZWQiOnRydWUsIngtbXMtYXp1cmV2bS1kYnh2YWxpZGF0ZWQiOnRydWUsIngtbXMtYXp1cmV2bS1kZWJ1Z2dlcnNkaXNhYmxlZCI6dHJ1ZSwieC1tcy1henVyZXZtLWRlZmF1bHQtc2VjdXJlYm9vdGtleXN2YWxpZGF0ZWQiOnRydWUsIngtbXMtYXp1cmV2bS1lbGFtLWVuYWJsZWQiOmZhbHNlLCJ4LW1zLWF6dXJldm0tZmxpZ2h0c2lnbmluZy1lbmFibGVkIjpmYWxzZSwieC1tcy1henVyZXZtLWh2Y2ktcG9saWN5IjowLCJ4LW1zLWF6dXJldm0taHlwZXJ2aXNvcmRlYnVnLWVuYWJsZWQiOmZhbHNlLCJ4LW1zLWF6dXJldm0taXMtd2luZG93cyI6ZmFsc2UsIngtbXMtYXp1cmV2bS1rZXJuZWxkZWJ1Zy1lbmFibGVkIjpmYWxzZSwieC1tcy1henVyZXZtLW9zYnVpbGQiOiJOb3RBcHBsaWNhdGlvbiIsIngtbXMtYXp1cmV2bS1vc2Rpc3RybyI6IlVidW50dSIsIngtbXMtYXp1cmV2bS1vc3R5cGUiOiJMaW51eCIsIngtbXMtYXp1cmV2bS1vc3ZlcnNpb24tbWFqb3IiOjIyLCJ4LW1zLWF6dXJldm0tb3N2ZXJzaW9uLW1pbm9yIjo0LCJ4LW1zLWF6dXJldm0tc2lnbmluZ2Rpc2FibGVkIjp0cnVlLCJ4LW1zLWF6dXJldm0tdGVzdHNpZ25pbmctZW5hYmxlZCI6ZmFsc2UsIngtbXMtYXp1cmV2bS12bWlkIjoiOUE0MkFCRDUtODM4NS00MkIzLTkyNTUtRkU3ODA3Njk4MTk0IiwieC1tcy1pc29sYXRpb24tdGVlIjp7IngtbXMtYXR0ZXN0YXRpb24tdHlwZSI6InNldnNucHZtIiwieC1tcy1jb21wbGlhbmNlLXN0YXR1cyI6ImF6dXJlLWNvbXBsaWFudC1jdm0iLCJ4LW1zLXJ1bnRpbWUiOnsia2V5cyI6W3siZSI6IkFRQUIiLCJrZXlfb3BzIjpbInNpZ24iXSwia2lkIjoiSENMQWtQdWIiLCJrdHkiOiJSU0EiLCJuIjoicDV1aWdBQUFMMTc1RTBEeEF0YTI4dE9PQTFJS1R4YndsM0xXa1JOZlRwdmY5a0pQdC1qMWhwTkZaZnhUZXBRYU5GSmJ0cVNCcVFhUHBjOGI4VUVLTjVJa3YxTElmS0FBeEZ1RlJJZm8wZFBxaG5RdDhoZi00ZzRCbm00eXQwVEx3elJYUHZtMHB4ZkphT2pIQmxwRGVhZ3NSWDlrUk5VanFnVWl0UXBtVDZIM1dxNHMtN3d3TlBFUXRHZG5hZHNfbmtfdmF6MnlJdTRfWEtGMkUtYjdRTFp6ck1ZazJsLVg5TWlrNEdOVzNWZ1NGc01lTmhJVkZqdlFvRjJMeVpEZnZVWnd5ejFaRURWM0VVM1ZJMnJ3RHpETHJKdFpOMV9waUFMekswSm5kWGNVaUN3WXFhbHpKS2FuX3R5ZWZXclhVd3NpMHU3X1NuMjYzQ3dPRk9UVXl3In0seyJlIjoiQVFBQiIsImtleV9vcHMiOlsiZW5jcnlwdCJdLCJraWQiOiJIQ0xFa1B1YiIsImt0eSI6IlJTQSIsIm4iOiJ3RDAzY0FBQW9sZXY3eWlIalZXZ1pwNDJ2aDdDbTZQelhQa3FzTFhZUmJJSkJ3U2VPYkZDVEFCR29UUVdmazhJcmgxUGhQWGVlMDlzMlNWNG03Z1l1YzJDV0QzUmU2TGQ3YmRQc2M1WEFqZmw4QlBjcDJiR1ZiTmJqUnB4SV9EcTA5N244S05aR1FNdXhLZG91a2lnWXVoWmhpdXp5aElYVFk4WFJINE1hYWRlOEFER2JIeHFXTXJob05PWThIVC1yc01UREJTeEtJa2QxQ1hGN09VekxvT01sYmhxTzRnS0dIOHZVaklud0xmM0F5b2JodXhnbGJiVDNsNm9va0NDU0kxSkltX0JNQWNqNzNfS0g1TU1lZGlFMUFpbzNtMWZ4UDhXTWxhWnhaeUdoZmFWdzBmc3BTYnBDeXVsM2NmdG9wTTZOQmtxZzdYM1RfbHN2Mk42U3cifV0sInVzZXItZGF0YSI6IjAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwIiwidm0tY29uZmlndXJhdGlvbiI6eyJjb25zb2xlLWVuYWJsZWQiOnRydWUsInNlY3VyZS1ib290Ijp0cnVlLCJ0cG0tZW5hYmxlZCI6dHJ1ZSwidm1VbmlxdWVJZCI6IjlBNDJBQkQ1LTgzODUtNDJCMy05MjU1LUZFNzgwNzY5ODE5NCJ9fSwieC1tcy1zZXZzbnB2bS1hdXRob3JrZXlkaWdlc3QiOiIwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAiLCJ4LW1zLXNldnNucHZtLWJvb3Rsb2FkZXItc3ZuIjo0LCJ4LW1zLXNldnNucHZtLWZhbWlseUlkIjoiMDEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAiLCJ4LW1zLXNldnNucHZtLWd1ZXN0c3ZuIjo3LCJ4LW1zLXNldnNucHZtLWhvc3RkYXRhIjoiMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMCIsIngtbXMtc2V2c25wdm0taWRrZXlkaWdlc3QiOiIwMzU2MjE1ODgyYTgyNTI3OWE4NWIzMDBiMGI3NDI5MzFkMTEzYmY3ZTMyZGRlMmU1MGZmZGU3ZWM3NDNjYTQ5MWVjZGQ3ZjMzNmRjMjhhNmUwYjJiYjU3YWY3YTQ0YTMiLCJ4LW1zLXNldnNucHZtLWltYWdlSWQiOiIwMjAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMCIsIngtbXMtc2V2c25wdm0taXMtZGVidWdnYWJsZSI6ZmFsc2UsIngtbXMtc2V2c25wdm0tbGF1bmNobWVhc3VyZW1lbnQiOiIwMzZmYzIyYjUxNzk4MWE3OTFmN2Y4Yjg5ZDYzNGEwMGU5NjRmNmIwZGZhYmM1NjgwOTBlYjQzOTNkNjAyNmY5NmFhNmI3Y2NhMjc1OWYyOWU1MjE0NjlmMTE4OWMwMGMiLCJ4LW1zLXNldnNucHZtLW1pY3JvY29kZS1zdm4iOjIxMSwieC1tcy1zZXZzbnB2bS1taWdyYXRpb24tYWxsb3dlZCI6ZmFsc2UsIngtbXMtc2V2c25wdm0tcmVwb3J0ZGF0YSI6ImJjZThlZTY1ZDQwOTMxYTliMzNlMWEyOTg2OWJiMjNkZjRkZDgwOTdmMDM4ODk4ZjZiMmFjYmI0NDVkMzg2YTUwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwIiwieC1tcy1zZXZzbnB2bS1yZXBvcnRpZCI6IjZiMzI0N2QxZTBlMmUwNzM2MGMxMWJmY2JiZWFmMWQ0YjhkNDJjNTMxMDYwMWU5MGMzMmViYzY4YTVhMTZlODQiLCJ4LW1zLXNldnNucHZtLXNtdC1hbGxvd2VkIjp0cnVlLCJ4LW1zLXNldnNucHZtLXNucGZ3LXN2biI6MjEsIngtbXMtc2V2c25wdm0tdGVlLXN2biI6MCwieC1tcy1zZXZzbnB2bS12bXBsIjowfSwieC1tcy1wb2xpY3ktaGFzaCI6IndtOW1IbHZUVTgyZThVcW9PeTFZajFGQlJTTmtmZTk5LTY5SVlEcTllV3MiLCJ4LW1zLXJ1bnRpbWUiOnsiY2xpZW50LXBheWxvYWQiOnsibm9uY2UiOiIifSwia2V5cyI6W3siZSI6IkFRQUIiLCJrZXlfb3BzIjpbImVuY3J5cHQiXSwia2lkIjoiVHBtRXBoZW1lcmFsRW5jcnlwdGlvbktleSIsImt0eSI6IlJTQSIsIm4iOiJ3S3E1REFBQXBlaWVpR2VlTHNXN1ZNZGVYYVBVdUJDYVpjR1p5TUNZN3VOX3F5d0VwSkw3bTJ0UmVXZDBEc2tUZVJaMDUzNzQ3U3FmZm1nbzVjc2Rlb1QxUmthcFN3aC1qbHZ2emZoRDBPYVYxQVRmRkF4TVB5MV94VkNROGk2cGItdk96eWtWcmUzb2FSTGlBUmFhd3duMDMyNUstVmhmWkplY01rUjE5RjA2Vjdod3k2RTZQMTZyV05IcUNqN2VxbGZaSmZpaEZBWXQxN1JIWHpWaUZ0RjQ3cld0U0pKWHRDMl9nRmM3OWR1NVlxbWZmYW5WUGRWZFBwa1AwbVF4U3Q1QVFIX0xaRTdueTNYS3RDT1FZU3dMcDQ0dVZWT1BWcGMwMTFITmx4dWswdXREWGJsdGlad29JU1c5cmFuMkljZFZaZHJHZThEdk9SN2xmQTVKWHcifV19LCJ4LW1zLXZlciI6IjEuMCJ9.WZ8QBavl6lGLG9TDPK8zjrTSmyUeH9c85Cw1lw7ON9qKLuWNHTusZHFnhpieLISb9h5MAN_7EaL_uirtPAK7rII30Zbokka9hQCQqpJ18ZGozZRg99gfYsO3PIKqtt7hNQyP5Rs9bQaSbU8llKwxLP3aUHCjK4lQnIB29-QQVZ36uu393OBTH0wIE55TpapSyasIQvDgoGdFO69cZzNcQElPpp7xZjc1QDBkoGW6mG3b4sU4aVMw7erLIaD71FguHVfl0QrWBc542M_1jhsfMJaCJ-I5dtvIZPvMb_cIr_MHVb1vxnzH8QjJSvNDHxTSKs_NUKIhHO3lhfcnjypRzw"

# Parse JWT components
jwt_parts = jwt.split(".") # [Split JWT into header, payload, signature parts]
header_b64 = jwt_parts[0] # [Base64url encoded header]
payload_b64 = jwt_parts[1] # [Base64url encoded attestation report]
signature_b64 = jwt_parts[2] # [Base64url encoded signature]

# Construct message that was signed - header.payload [this is what Azure attestation service signed]
message_to_verify = f"{header_b64}.{payload_b64}".encode() 

# Helper to fix base64url padding [base64url removes padding but decoder needs it]
def fix_base64_padding(b64_string):
    return b64_string + "=" * (-len(b64_string) % 4)

# Decode the signature bytes [so we can verify it cryptographically]
signature = base64.urlsafe_b64decode(fix_base64_padding(signature_b64))

# Function to fetch signing key from Azure attestation service
def get_signing_key(jku_url: str, target_kid: str):
    """
    Fetches the Azure attestation service's signing key - this is what signed the attestation report.
    The key is fetched from Azure's attestation service using:
    - jku_url: URL hosting the signing keys [attestation service endpoint]
    - target_kid: ID of specific key used [to find right key from set]
    """
    try:
        # Get the signing keys from Azure [list of public keys in JWKS format]
        response = requests.get(jku_url)
        response.raise_for_status()
        keys = response.json()["keys"]

        # Find the specific key used to sign this attestation [via key ID]
        for key in keys:
            if key.get("kid") == target_kid:
                # Extract RSA key components [modulus and exponent]
                n = base64.urlsafe_b64decode(fix_base64_padding(key["n"])) # [modulus]
                e = base64.urlsafe_b64decode(fix_base64_padding(key["e"])) # [exponent]

                # Convert bytes to integers [needed to construct RSA key]
                e_int = int.from_bytes(e, byteorder="big") 
                n_int = int.from_bytes(n, byteorder="big")

                # Create RSA public key object [for signature verification]
                pub_key = rsa.RSAPublicNumbers(e=e_int, n=n_int).public_key(
                    default_backend()
                )

                return pub_key

        raise ValueError(f"No key found with kid: {target_kid}")

    except Exception as e:
        print(f"Error fetching signing key: {str(e)}")
        raise

# Get JKU and KID from JWT header [tells us where to find signing key]
header_decoded = json.loads(base64.urlsafe_b64decode(fix_base64_padding(header_b64)))
jku_url = header_decoded["jku"]  # [Azure attestation endpoint URL]
kid = header_decoded["kid"]  # [Key ID that signed this attestation]

print("=== Fetching Signing Key ===")
print(f"JKU URL: {jku_url}")
print(f"Key ID: {kid}")

# Fetch the specific signing key [from Azure attestation service]
signing_key = get_signing_key(jku_url, kid)

# Print key details [for debugging/verification]
print("\n=== Debug Information ===")
key_info = signing_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)
print("Signing key PEM format:", key_info.decode("utf-8"))

# Verify the signature [to prove attestation is genuine]
try:
    signing_key.verify(
        signature, 
        message_to_verify,
        padding.PKCS1v15(),  # [RSA PKCS#1 v1.5 padding] 
        hashes.SHA256()  # [SHA-256 hash of message]
    )
    print("Signature is valid!") # [Attestation is genuine]
except InvalidSignature:
    # Print details if verification fails [for debugging]
    print("Invalid signature - verification failed") 
    print("\nVerification details:")
    print(f"- Signature length: {len(signature)} bytes")
    print(f"- Message length: {len(message_to_verify)} bytes") 
    print(f"- RSA key size: {signing_key.key_size} bits")
except Exception as e:
    print("Other verification error:", str(e), type(e))