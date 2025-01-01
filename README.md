# Azure SEV-SNP TEE Attestation Setup Guide

## Overview

This project enables secure price attestation for Ethereum applications running in Azure SEV-SNP TEEs. It verifies on-chain that price fetching occurred in a genuine TEE environment [Using hardware-based remote attestation to prove code execution].

## Project Structure

```
/sevsnp-cvm/
├── SolRsaVerify/                      # Solidity verification contracts
│
├── confidential-computing-cvm-guest-attestation/ # Guest attestation files
│
├── main.py                            # Price fetching and JWT generation
├── run.sh                             # Attestation automation
```

## Prerequisites

- Azure SEV-SNP TEE virtual machine
- SSH access
- Python3 + pip
- Foundry toolkit

## Installation

1. SSH into VM:

```bash
ssh -i <path/to/you/rsa/private/key>.pem <username>@<vm-ip>
# e.g. ssh -i rsa-key.pem jesserc@72.50.96.28 
```

2. Clone repositories:

```bash
git clone --recurse-submodules https://github.com/Jesserc/sevsnp-tee.git
cd  sevsnp-tee
```

3. Install system dependencies [Required for building C++ attestation client]:

```bash
sudo apt-get update
sudo apt-get install -y build-essential libcurl4-openssl-dev libjsoncpp-dev libboost-all-dev cmake nlohmann-json3-dev
```
Note: While some of these dependencies are installing, you'll see two types of prompts - just press 'yes' for package installation and Enter for service restart  (like the screenshot below). Feel free to read the details.
![alt text](<Screenshot 2024-12-20 at 6.10.21 PM.png>)

4. Install Azure attestation package [Provides hardware attestation capabilities]:

```bash
curl -O https://packages.microsoft.com/repos/azurecore/pool/main/a/azguestattestation1/azguestattestation1_1.0.5_amd64.deb
sudo dpkg -i azguestattestation1_1.0.5_amd64.deb
```

5. Build attestation client:

```bash
cd confidential-computing-cvm-guest-attestation/cvm-attestation-sample-app
cmake .
make
```

6. Install Python package manager (pip3) and required Python packages:

```bash
# Install pip3
sudo apt-get install -y python3-pip

# Install required Python packages:
pip3 install requests cryptography eth-abi
```

```bash
pip3 install --user requests cryptography eth-abi
```

7. Install Foundry for Solidity testing:
   Follow instructions at https://getfoundry.sh

8. Configure permissions:

```bash
cp confidential-computing-cvm-guest-attestation/cvm-attestation-sample-app/AttestationClient  ../
```

## Usage

Run the attestation process:

```bash
chmod +x run.sh

./run.sh
```

This will:

1. Fetch current ETH price [Using CoinMarketCap API]
2. Generate attestation JWT [Proves price was fetched in TEE]
3. Verify attestation on-chain [Using RSA signature verification]

## Components

### Python Script (main.py)

- Fetches price data
- Interacts with attestation client
- Prepares parameters for Solidity verification

### Solidity Contract (AzureTEEVerifier.sol)

- Verifies attestation signatures [Using RSA-PKCS1.5]
- Manages attested price data
- Provides staleness checks

### Test Contract (AzureTEEVerifier.t.sol)

- Validates end-to-end attestation flow
- Tests signature verification
- Checks price storage/retrieval
