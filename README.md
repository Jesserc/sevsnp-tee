# On-Chain RSA Signature Verification for Azure SEV-SNP confidential VM

## Overview
This project aims to demonstrate on-chain RSA signature verification for Azure SEV-SNP (Secure Encrypted Virtualization - Secure Nested Paging) Cloud Virtual Machines (CVMs). The goal is to provide a mechanism for verifying the integrity and authenticity of data processed within a Trusted Execution Environment (TEE).

## Setup
1. Clone the repository:
```bash
git clone <repository-url>
cd sevsnp-cvm
```
2. Set up a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

# Decode Attestation Report
## Header
```json
{
  "alg": "RS256",
  "jku": "https://sharedeus2.eus2.attest.azure.net/certs",
  "kid": "J0pAPdfXXHqWWimgrH853wMIdh5/fLe1z6uSXYPXCa0=",
  "typ": "JWT"
}

```

## Payload
```json
{
  "exp": 1734747894,
  "iat": 1734719094,
  "iss": "https://sharedeus2.eus2.attest.azure.net",
  "jti": "faefb2918d2b57928d1aa5e8fc2ca188d4f10115834bddc10181e929b14205c5",
  "nbf": 1734719094,
  "secureboot": true,
  "x-ms-attestation-type": "azurevm",
  "x-ms-azurevm-attestation-protocol-ver": "2.0",
  "x-ms-azurevm-attested-pcrs": [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7
  ],
  "x-ms-azurevm-bootdebug-enabled": false,
  "x-ms-azurevm-dbvalidated": true,
  "x-ms-azurevm-dbxvalidated": true,
  "x-ms-azurevm-debuggersdisabled": true,
  "x-ms-azurevm-default-securebootkeysvalidated": true,
  "x-ms-azurevm-elam-enabled": false,
  "x-ms-azurevm-flightsigning-enabled": false,
  "x-ms-azurevm-hvci-policy": 0,
  "x-ms-azurevm-hypervisordebug-enabled": false,
  "x-ms-azurevm-is-windows": false,
  "x-ms-azurevm-kerneldebug-enabled": false,
  "x-ms-azurevm-osbuild": "NotApplication",
  "x-ms-azurevm-osdistro": "Ubuntu",
  "x-ms-azurevm-ostype": "Linux",
  "x-ms-azurevm-osversion-major": 22,
  "x-ms-azurevm-osversion-minor": 4,
  "x-ms-azurevm-signingdisabled": true,
  "x-ms-azurevm-testsigning-enabled": false,
  "x-ms-azurevm-vmid": "9A42ABD5-8385-42B3-9255-FE7807698194",
  "x-ms-isolation-tee": {
    "x-ms-attestation-type": "sevsnpvm",
    "x-ms-compliance-status": "azure-compliant-cvm",
    "x-ms-runtime": {
      "keys": [
        {
          "e": "AQAB",
          "key_ops": [
            "sign"
          ],
          "kid": "HCLAkPub",
          "kty": "RSA",
          "n": "p5uigAAAL175E0DxAta28tOOA1IKTxbwl3LWkRNfTpvf9kJPt-j1hpNFZfxTepQaNFJbtqSBqQaPpc8b8UEKN5Ikv1LIfKAAxFuFRIfo0dPqhnQt8hf-4g4Bnm4yt0TLwzRXPvm0pxfJaOjHBlpDeagsRX9kRNUjqgUitQpmT6H3Wq4s-7wwNPEQtGdnads_nk_vaz2yIu4_XKF2E-b7QLZzrMYk2l-X9Mik4GNW3VgSFsMeNhIVFjvQoF2LyZDfvUZwyz1ZEDV3EU3VI2rwDzDLrJtZN1_piALzK0JndXcUiCwYqalzJKan_tyefWrXUwsi0u7_Sn263CwOFOTUyw"
        },
        {
          "e": "AQAB",
          "key_ops": [
            "encrypt"
          ],
          "kid": "HCLEkPub",
          "kty": "RSA",
          "n": "wD03cAAAolev7yiHjVWgZp42vh7Cm6PzXPkqsLXYRbIJBwSeObFCTABGoTQWfk8Irh1PhPXee09s2SV4m7gYuc2CWD3Re6Ld7bdPsc5XAjfl8BPcp2bGVbNbjRpxI_Dq097n8KNZGQMuxKdoukigYuhZhiuzyhIXTY8XRH4Maade8ADGbHxqWMrhoNOY8HT-rsMTDBSxKIkd1CXF7OUzLoOMlbhqO4gKGH8vUjInwLf3AyobhuxglbbT3l6ookCCSI1JIm_BMAcj73_KH5MMediE1Aio3m1fxP8WMlaZxZyGhfaVw0fspSbpCyul3cftopM6NBkqg7X3T_lsv2N6Sw"
        }
      ],
      "user-data": "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
      "vm-configuration": {
        "console-enabled": true,
        "secure-boot": true,
        "tpm-enabled": true,
        "vmUniqueId": "9A42ABD5-8385-42B3-9255-FE7807698194"
      }
    },
    "x-ms-sevsnpvm-authorkeydigest": "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "x-ms-sevsnpvm-bootloader-svn": 4,
    "x-ms-sevsnpvm-familyId": "01000000000000000000000000000000",
    "x-ms-sevsnpvm-guestsvn": 7,
    "x-ms-sevsnpvm-hostdata": "0000000000000000000000000000000000000000000000000000000000000000",
    "x-ms-sevsnpvm-idkeydigest": "0356215882a825279a85b300b0b742931d113bf7e32dde2e50ffde7ec743ca491ecdd7f336dc28a6e0b2bb57af7a44a3",
    "x-ms-sevsnpvm-imageId": "02000000000000000000000000000000",
    "x-ms-sevsnpvm-is-debuggable": false,
    "x-ms-sevsnpvm-launchmeasurement": "036fc22b517981a791f7f8b89d634a00e964f6b0dfabc568090eb4393d6026f96aa6b7cca2759f29e521469f1189c00c",
    "x-ms-sevsnpvm-microcode-svn": 211,
    "x-ms-sevsnpvm-migration-allowed": false,
    "x-ms-sevsnpvm-reportdata": "bce8ee65d40931a9b33e1a29869bb23df4dd8097f038898f6b2acbb445d386a50000000000000000000000000000000000000000000000000000000000000000",
    "x-ms-sevsnpvm-reportid": "6b3247d1e0e2e07360c11bfcbbeaf1d4b8d42c5310601e90c32ebc68a5a16e84",
    "x-ms-sevsnpvm-smt-allowed": true,
    "x-ms-sevsnpvm-snpfw-svn": 21,
    "x-ms-sevsnpvm-tee-svn": 0,
    "x-ms-sevsnpvm-vmpl": 0
  },
  "x-ms-policy-hash": "wm9mHlvTU82e8UqoOy1Yj1FBRSNkfe99-69IYDq9eWs",
  "x-ms-runtime": {
    "client-payload": {
      "nonce": ""
    },
    "keys": [
      {
        "e": "AQAB",
        "key_ops": [
          "encrypt"
        ],
        "kid": "TpmEphemeralEncryptionKey",
        "kty": "RSA",
        "n": "wKq5DAAApeieiGeeLsW7VMdeXaPUuBCaZcGZyMCY7uN_qywEpJL7m2tReWd0DskTeRZ053747Sqffmgo5csdeoT1RkapSwh-jlvvzfhD0OaV1ATfFAxMPy1_xVCQ8i6pb-vOzykVre3oaRLiARaawwn0325K-VhfZJecMkR19F06V7hwy6E6P16rWNHqCj7eqlfZJfihFAYt17RHXzViFtF47rWtSJJXtC2_gFc79du5YqmffanVPdVdPpkP0mQxSt5AQH_LZE7ny3XKtCOQYSwLp44uVVOPVpc011HNlxuk0utDXbltiZwoISW9ran2IcdVZdrGe8DvOR7lfA5JXw"
      }
    ]
  },
  "x-ms-ver": "1.0"
}
```

## Signature
```bash
vl6lGLG9TDPK8zjrTSmyUeH9c85Cw1lw7ON9qKLuWNHTusZHFnhpieLISb9h5MAN_7EaL_uirtPAK7rII30Zbokka9hQCQqpJ18ZGozZRg99gfYsO3PIKqtt7hNQyP5Rs9bQaSbU8llKwxLP3aUHCjK4lQnIB29-QQVZ36uu393OBTH0wIE55TpapSyasIQvDgoGdFO69cZzNcQElPpp7xZjc1QDBkoGW6mG3b4sU4aVMw7erLIaD71FguHVfl0QrWBc542M_1jhsfMJaCJ-I5dtvIZPvMb_cIr_MHVb1vxnzH8QjJSvNDHxTSKs_NUKIhHO3lhfcnjypRzw  
```