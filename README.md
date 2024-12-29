# On-Chain RSA Signature Verification for Azure SEV-SNP confidential VM

## Overview
This project aims to demonstrate on-chain verification for AMD SEV-SNP (Secure Encrypted Virtualization - Secure Nested Paging) TEE. The goal is to provide a mechanism for verifying the integrity and authenticity of data processed within a Trusted Execution Environment (TEE). 

This project uses AMD SEV-SNP TEE on Azure cloud.

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

# Decoded Attestation Report
*NOTE: The Attestation report is in JWT format, which is **Base64url** encoded, and some inner values, like nonce and price, are further **Base64** encoded.
This is the decoded attestation report.*
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
  "exp": 1735520673,
  "iat": 1735491873,
  "iss": "https://sharedeus2.eus2.attest.azure.net",
  "jti": "306e081393b2f30c0af3017d7ebc4ee05818961a0c9d10460dfaabae231a73da",
  "nbf": 1735491873,
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
  "x-ms-azurevm-vmid": "1588CFD1-4BCA-40E9-8FA1-A29F3EDDFCD9",
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
          "n": "pngUgQABC2ieAWrd1qyM14oVNkIS71D1UkyzYFHPu1nHPgPhH2oF4MPumYBS_OBeBjSY-L7KzD-ochGZe0ixqYzEhpHMh1YARIVOHVl7nDvU4R923A5pPzOHbRcN85a5HuqVVmDPcC3Ju8-oL-xIFmFnDlmN0q2EfC9Nt74Z_tftPvdXTUhw7camQ1zHY9so5k2S1pIKUvY5mcCsLVKjQaayVbaX4ag_pOZyp6PK5RqDB4g1Nurtz4S1BcqFlVE_LcKEMsA1rWJZoiNvp6HCr9U9vpWCnAqAYAEcFq9lBhITb7Yif_9zKrIbUeHZujFtphWRB3EyM6-ip5YlaRqBGw"
        },
        {
          "e": "AQAB",
          "key_ops": [
            "encrypt"
          ],
          "kid": "HCLEkPub",
          "kty": "RSA",
          "n": "vwlYDAAAb5LonvSpZhCXvycDvwbMiClpjcwq5j_YjMrbL610iqoJcUkF-AXS4y4p3NyRlMPdfJ9pJrGYeUVWptb-kPdsy35TEgGlsZ7N7UJxJZWwEVQozdyAPwvukvo7jathgmZp6ig5uZM_itfZ5WuvpWQkJZOI82N9NMeqsxJ5vaDagStH0zNDvBzpEpGrPZAXH3QNoZO52fbSyXBQof6o_mPA-pTDjC3YZMII7q1znBgRtz0x3FJ_pRPnxccA60vIBVs2efQOQpzOLVZAJHbWt2FecGZ5vT3LH9R1b5AiNxo6TY3pKfDK34wnOKJ2sSw9WaR_tg5R6ZjRXwtm2w"
        }
      ],
      "user-data": "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
      "vm-configuration": {
        "console-enabled": true,
        "secure-boot": true,
        "tpm-enabled": true,
        "vmUniqueId": "1588CFD1-4BCA-40E9-8FA1-A29F3EDDFCD9"
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
    "x-ms-sevsnpvm-reportdata": "d6039652c4e30390b0b4484e53237c2c29e06b32078b9b4436d36769150298ba0000000000000000000000000000000000000000000000000000000000000000",
    "x-ms-sevsnpvm-reportid": "318f3518064eb76ec282397c599492ec295fa43a795b99b781c9c464a8282953",
    "x-ms-sevsnpvm-smt-allowed": true,
    "x-ms-sevsnpvm-snpfw-svn": 21,
    "x-ms-sevsnpvm-tee-svn": 0,
    "x-ms-sevsnpvm-vmpl": 0
  },
  "x-ms-policy-hash": "wm9mHlvTU82e8UqoOy1Yj1FBRSNkfe99-69IYDq9eWs",
  "x-ms-runtime": {
    "client-payload": {
      "nonce": "Y29pbm1hcmtldGNhcC5jb20=",
      "price": "MzM0OS45NzU3NTM5NzQ1NDM3",
      "timestamp": "MTczNTQ5MTg3Mg=="
    },
    "keys": [
      {
        "e": "AQAB",
        "key_ops": [
          "encrypt"
        ],
        "kid": "TpmEphemeralEncryptionKey",
        "kty": "RSA",
        "n": "xvBXhAAAjaKiTunomRDGoX9VaqpDx_d-YKknggtksNeOt14auPSBHbFfKad5-juA6FkQc9D2Q01ZBEumM70yv3zlXw9LpnzhwSLeQXJAa-XTCivc8YE15ESOVY3-1suahbbV-gtlFNLHCSr-x5P4XsHMaZ9RR75EGu60NPRr-Ws3GFzS31c1jOOJ9wBRRXFwWoWBaJHUUHPRfxd1Bp0PiuO1k19JaMxH9Qkugh6fkw6bPRL1xA4kXR7KEtYuI2p7kmhqnddvVac1b5v0EsZ_AHWv_NkZxurrSkI5Z6CV64AIGd19DskIeeP3Nm7UkQoC8CEiPgD1ZferkN3zBDIXBw"
      }
    ]
  },
  "x-ms-ver": "1.0"
}
```

## Signature
```bash
sJtpL4veGuSa8PDZ_JFogDiZOqMtNoR9e57kY7dxeazikRhkfAjNivLRSkOvcdjxNLVZSgApoUzMB6OF_M-QnffTLY9iYHQTmkQN4ggBHffQJzAG3EOpyS2OqPlS_0qvHNSbCqIGW_a_HLyRrzwh4-4XSF486PjVkeQS9QJO2mcrCbzXfX8xYlqvUw3-j0NvPiH4NNyzmIBJoL8zIwuef_p94GLRm21FP-P8Jwbs6VtX3yMYy4pGYTNTpvNRGoVEO6jOfmFyaO8OIsSU2jYndN31dlieU4dlLbHLenVxbNk1hile_RYhUlDE5ve5Tbu64DqQD9AzMsD1_hh_b2viEw
```
