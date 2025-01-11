# TEE-Verified Price Feed Using Azure Confidential VMs

This project demonstrates how Trusted Execution Environments (TEEs) can be utilized. Here I create a secure and verifiable cryptocurrency price feed, by leveraging AMD SEV-SNP TEE technology with Azure cloud services. The key aspects include:

1. **Secure Price Fetching**: Prices are fetched within an encrypted TEE, isolated from the host OS and hypervisor, including the cloud provider (Azure in this case).

2. **Hardware Attestation**: Azure's attestation service verifies the TEE's integrity and signs a report containing the price data and VM security configuration.

3. **Multi-Layer Verification**: The signed attestation report is verified both off-chain and on-chain.


## Project Structure

```
/sevsnp-tee/
├── SolRsaVerify/                 # Solidity verification contracts
│   ├── src/
│   │   ├── AzureTEEVerifier.sol  # Main attestation verification
│   │   ├── RsaVerify.sol         # RSA signature validation
│   ├── test/
│   │   └── AzureTEEVerifier.t.sol # Integration tests with foundry's FFI
├── main.py                       # Price fetching & attestation
├── AttestationClient             # Azure TEE attestation binary  
└── run.sh                        # Automation script
```

## Components
![image](https://github.com/user-attachments/assets/ed855de2-e172-440c-a1bc-7b2a3bc917fc)

### Price Attestation (main.py)
- Fetches real-time cryptocurrency prices from CoinMarketCap's API using an authentication key
- Executes a C++ Attestation Client binary (via a sub-process) which requests hardware-level attestation from the AMD SEV-SNP TEE and obtains a verified JWT token (of the attestation report) from Microsoft Azure Attestation service
- Extracts and formats the JWT token's signature, message, security claims and price data into ABI-encoded parameters [enables smart contracts to verify the attestation on-chain]

### Onchain Attestation Verification (AzureTEEVerifier.sol)
- Verifies the cryptographic authenticity of attestation reports using RSA signature validation against Microsoft Azure Attestation's public key [proves report wasn't tampered with]  
- Checks TEE security claims to ensure the environment is properly hardened - including debug mode status, AMD SEV-SNP configuration, and VM isolation level [confirms secure execution]
- Stores verified price data with timestamps and enforces 15-minute freshness window for price validity [prevents use of stale data]

### Integration Testing (AzureTEEVerifier.t.sol)  
- Executes Python-based attestation script through Foundry's FFI to obtain real hardware attestations [tests full attestation flow]
- ABI decodes attestation parameters and validates them through the onchain verification contract [ensures verification logic works]
- Confirms both successful signature verification and correct storage of attested price data [validates core functionality]

## Setup Requirements

- Azure SEV-SNP VM with attestation support
- Python 3.x with imported libraries (more details in the setup below)
- Foundry toolkit for Solidity testing
  
## Installation

1. **SSH Access Setup** (Required for VM access)
```bash
# Make private key read-only for SSH security
chmod 400 <path/to/private/key>.pem

# Connect to VM
ssh -i <path/to/private/key>.pem <username>@<vm-ip>
```

2. **Project Setup** (Get source code and dependencies)
```bash
# Clone repository with submodules
git clone --recurse-submodules https://github.com/Jesserc/sevsnp-tee.git
cd sevsnp-tee

# Install system dependencies for C++ attestation client
sudo apt-get update
sudo apt-get install -y build-essential libcurl4-openssl-dev \
    libjsoncpp-dev libboost-all-dev cmake nlohmann-json3-dev
```

3. **Azure Attestation Setup** (For hardware attestation functionality)
```bash
# Download and install Azure guest attestation package
curl -O https://packages.microsoft.com/repos/azurecore/pool/main/a/azguestattestation1/azguestattestation1_1.0.5_amd64.deb
sudo dpkg -i azguestattestation1_1.0.5_amd64.deb
```

4. **Attestation Client Build** (Compile C++ attestation code)
```bash
# Build the attestation client
cd confidential-computing-cvm-guest-attestation/cvm-attestation-sample-app
cmake .
make

# Copy binary to project root
cp AttestationClient ../../
cd ../../
```

5. **Development Tools** (For testing and verification)
```bash
# Install Python dependencies
sudo apt-get install -y python3-pip
pip3 install requests cryptography eth-abi

# Install Foundry toolkit for Solidity
curl -L https://foundry.paradigm.xyz | bash
source ~/.bashrc
foundryup
```

6. **Final Setup** (Prepare for execution)
```bash
# Make run script executable
chmod +x run.sh
```

## Usage

Run the complete attestation & verification flow:
```bash
./run.sh
```

This executes:
1. Price fetching in TEE
2. Attestation report generation
3. On-chain verification
4. Integration tests
