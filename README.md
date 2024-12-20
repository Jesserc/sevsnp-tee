## On-Chain RSA Signature Verification for Azure SEV-SNP confidential VM

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