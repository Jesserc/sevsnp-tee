// SPDX-License-Identifier: GPL-3.0-or-later
pragma solidity ^0.8.13;

import "forge-std/Test.sol";
import "../src/RsaVerify.sol";

contract RsaVerifyAttestedPriceTest is Test {
    function testAttestedPrice() public {
        // Execute Python script
        string[] memory inputs = new string[](2);
        inputs[0] = "python3";
        inputs[1] = "/home/jesserc/sevsnp-cvm/main.py";

        bytes memory result = vm.ffi(inputs);

        // Decode the ABI-encoded parameters
        (
            bytes memory message, 
            bytes memory signature,
            bytes memory exponent,
            bytes memory modulus
        ) = abi.decode(result, (bytes, bytes, bytes, bytes));

        // emit log_named_bytes("Signature", signature);
        // emit log_named_bytes("MessageHash", message);
        // emit log_named_bytes("Exponent", exponent);
        // emit log_named_bytes("Modulus", modulus);
        
        // Verify using RsaVerify
        bool isValid = RsaVerify.pkcs1Sha256Raw(
            message,
            signature,
            exponent,
            modulus
        );

        assertTrue(isValid);
    }
}
