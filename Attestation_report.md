# Decoded attestation report

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
  "exp": 1736726200,
  "iat": 1736697400,
  "iss": "https://sharedeus2.eus2.attest.azure.net",
  "jti": "21a0e717ab00342230b21bb9ff58e7058a66f46cfe1b91b5a12ac513162d49cf",
  "nbf": 1736697400,
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
  "x-ms-azurevm-osversion-major": 24,
  "x-ms-azurevm-osversion-minor": 4,
  "x-ms-azurevm-signingdisabled": true,
  "x-ms-azurevm-testsigning-enabled": false,
  "x-ms-azurevm-vmid": "88543EA6-88B0-42E3-ABB6-0CA34DF51AD9",
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
          "n": "v1212AAA0em-1JPTU0sIi9g5r0yKKoGeu-YeKJMmUYwfHdncmKa5-rUT1szPMxV7F-9_wZMGhf9rtwCkJep1SkBhvetVb8PcDK44a2K5vGkFtdk11_mrA1LmPGkRBq7Es_x2-tfVN4_DKG2zNGaeLfvestyOUh_cgOeZJLhdndWbotMXIa1Qq5Bnq1OlIk9ezWvUuYJGbBcuIu0AKF0TKreLBT6sVvUo64PrZ0vSKxIvMJSY9zz4VtBrXevjXexjrxP77XObacX9vlHPkggJSatDx666hT5C71cEAg8JC7oTisg50W7BArCNso9Y0RIK8lWh8iXG_iGSgZOtVF_OFw"
        },
        {
          "e": "AQAB",
          "key_ops": [
            "encrypt"
          ],
          "kid": "HCLEkPub",
          "kty": "RSA",
          "n": "zbVBDgAA5VFa2SR0pLIVfu_DhOCSnYi4YHPwb-pyHMv1TdghQD_nhXoh2_r0G8Q8eW6SvegKbwCeC58jHEkmmPRzShjqYOuCSCVZ4BZrap305fVXDIZrX6u5Af-gjOJNssbUReUxpE3KesLAIE9odRRW1nMZtn_aMhuVypWogo2YWvp5LjL412sxvEYiUh210426R6GrPAnKyqUcYNLfWsveaoalxATUh6XlrURIRTWS5MNm1ZyY0xAVjpQeA9OtyKEFZRU4amIXvqM19UbkBefwt2WmZvLb630Z_qzbTNuybgQLTnH0OEF2Jp0jAHnZPKLVUOP_uSicZc6XYxZhKQ"
        }
      ],
      "user-data": "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
      "vm-configuration": {
        "console-enabled": true,
        "secure-boot": true,
        "tpm-enabled": true,
        "vmUniqueId": "88543EA6-88B0-42E3-ABB6-0CA34DF51AD9"
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
    "x-ms-sevsnpvm-reportdata": "267112875bb879d143ad3d25f5176cd05c5ecd62c16a49c127d2b5a032c1bc960000000000000000000000000000000000000000000000000000000000000000",
    "x-ms-sevsnpvm-reportid": "869aaf08b15d1ce622eac1794396ff0c98e81dbc94f1ae3b7fd7db47be927418",
    "x-ms-sevsnpvm-smt-allowed": true,
    "x-ms-sevsnpvm-snpfw-svn": 21,
    "x-ms-sevsnpvm-tee-svn": 0,
    "x-ms-sevsnpvm-vmpl": 0
  },
  "x-ms-policy-hash": "wm9mHlvTU82e8UqoOy1Yj1FBRSNkfe99-69IYDq9eWs",
  "x-ms-runtime": {
    "client-payload": {
      "nonce": "",
      "price": "",
      "timestamp": "MTczNjY5NzM5OQ=="
    },
    "keys": [
      {
        "e": "AQAB",
        "key_ops": [
          "encrypt"
        ],
        "kid": "TpmEphemeralEncryptionKey",
        "kty": "RSA",
        "n": "lKg5qgAAmqhuDGKkkCUrjdfzBiJTCwBUqKTQSkauTCXErtp55fN-1LmbPCyFIZDYroawQSh_YrMY4hXde0dJ98FNEm8WWWsm1c_mvI9uJqvHTnfZ-5aSOTF0ee-M3SdMQHH_uPSJUSEyJwJeRho9M6FGH7ifvgH5hA3a1QUmWPwOKxGvv4tGA5E2iJ8rB3FR_APEFSvyoGossrkh5U72N-YkYU84sRULZPHBXqDAkAHUu4RTgWqn-vyVoKiVhqhydxNDykC1c_q16W1XYgxSBiU7OW8AtYjBd4eXY6EiAV9-VtShRF3KXKb1sgCAoehPUvO2ON-l5HMxw4YTRTCaKw"
      }
    ]
  },
  "x-ms-ver": "1.0"
}
```

## Signature
```shell
GpiDJz5R4OAEj_UzW-8_qpnfo-GizOp9I7f7zCZYRqcie3TEUa3M4swKcNG1F--oGL59eMKWQGYSjIMSCugkOV_K8mBddyqSiuQTsQ9wRXlrMmRMH7Mg5L5uDt09E6NS0AwxNp8GrHRRvxrG3XwluU_nJg81Erfgk_hxIOJeDaOePS0mB2O7hfATx4Xv0wWRH3x3xHF6-dLDaBPowtQBTNIdKri02SqT8HMB3-Dvh4VAOXJ1xnC0CMdpi_LFKa72Z3vgGOr_WgCuTRaSBiAXonAQPC-V9bgaB_UaBJSUuTKxGQklklrkh21eMRWo2LOjKLW6Lruk8LEP_f9WqxheEQ
```

See [Attestation_report_jwt.md](./Attestation_report_jwt.md) for the JWT-encoded attestation report.
