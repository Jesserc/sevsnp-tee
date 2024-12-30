#!/bin/bash
# chmod +x ./run_attestation.sh

# Function to install pip3 if not available
install_pip3() {
    echo "pip3 not found. Attempting to install..."
    if ! command -v snap &> /dev/null; then
        echo "Error: snap not found. Please install snapd first"
        exit 1
    fi
    
    sudo snap install pip || {
        echo "Error: Failed to install pip via snap"
        exit 1
    }
}

# Check if python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is not installed"
    exit 1
fi

# Check if pip3 is installed, install if not
if ! command -v pip3 &> /dev/null; then
    install_pip3
fi

# Check if forge is installed [Needed for Solidity testing]
if ! command -v forge &> /dev/null; then
    echo "Error: forge is not installed. Please install Foundry tools"
    exit 1
fi

# Check if the main.py exists in current directory
if [ ! -f "main.py" ]; then
    echo "Error: main.py not found in current directory"
    exit 1
fi

# Check if AttestationClient exists and is executable
if [ ! -x "./AttestationClient" ]; then
    echo "Error: AttestationClient not found or not executable"
    exit 1
fi

# Check if Solidity test file exists
TEST_PATH="/home/jesserc/sevsnp-cvm/SolRsaVerify/test/RsaVerifyAttestedPriceTest.t.sol"
if [ ! -f "$TEST_PATH" ]; then
    echo "Error: Test file not found at $TEST_PATH"
    exit 1
fi

# Check if required Python packages are installed
echo "Checking required Python packages..."
python3 -c "import requests, cryptography" 2>/dev/null || {
    echo "Installing required Python packages..."
    pip3 install requests cryptography
}

# Run the Python script
echo "Running price attestation script..."
python3 main.py

# Check Python script exit status
if [ $? -ne 0 ]; then
    echo "Error: Price attestation failed"
    exit 1
fi
echo "Price attestation completed successfully"

# Change to the Solidity test directory
cd /home/jesserc/sevsnp-cvm/SolRsaVerify || {
    echo "Error: Could not change to test directory"
    exit 1
}

# Run Forge test with FFI enabled
echo "Running Solidity verification test..."
forge test --mc RsaVerifyAttestedPriceTest --ffi -vv

# Check Forge test exit status
if [ $? -eq 0 ]; then
    echo "All tests passed successfully!"
else
    echo "Error: Solidity verification test failed"
    exit 1
fi