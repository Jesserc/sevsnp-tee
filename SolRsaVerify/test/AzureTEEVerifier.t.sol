// SPDX-License-Identifier: GPL-3.0-or-later
pragma solidity ^0.8.13;

import "forge-std/Test.sol";
import "../src/AzureTEEVerifier.sol";

contract AzureTEEVerifierTest is Test {
    AzureTEEVerifier public verifier;

    function setUp() public {
        verifier = new AzureTEEVerifier();
    }

    function testVerifyAttestedPrice() public {
        // Execute Python script to get attestation params
        string[] memory inputs = new string[](2);
        inputs[0] = "python3";
        inputs[1] = "./main.py";

        bytes memory result = vm.ffi(inputs);

        // Decode all parameters
        (
            bytes memory signature,
            bytes memory message,
            bytes memory exponent,
            bytes memory modulus,
            uint256 price,
            string memory nonce,
            uint256 timestamp,
            string memory attestationType,
            string memory complianceStatus,
            bool isDebuggable,
            uint8 vmpl
        ) = abi.decode(result, (bytes, bytes, bytes, bytes, uint256, string, uint256, string, string, bool, uint8));

        // Verify attestation
        bool success = verifier.verifyAttestedPrice(
            signature,
            message,
            exponent, 
            modulus,
            price,
            nonce,
            timestamp,
            attestationType,
            complianceStatus,
            isDebuggable,
            vmpl
        );

        assertTrue(success);

        // Verify price was stored
        (uint256 storedPrice, uint256 storedTimestamp) = verifier.getVerifiedPrice();
        assertEq(storedPrice, price);
        assertEq(storedTimestamp, timestamp);
    }
}