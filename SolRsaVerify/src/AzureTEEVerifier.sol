// SPDX-License-Identifier: GPL-3.0-or-later
pragma solidity ^0.8.13;

import "./RsaVerify.sol";

contract AzureTEEVerifier {
    using RsaVerify for bytes32;

    // Security configuration constants
    string constant EXPECTED_ATTESTATION_TYPE = "sevsnpvm";
    string constant EXPECTED_COMPLIANCE_STATUS = "azure-compliant-cvm";
    uint8 constant EXPECTED_VMPL = 0;

    // Time window for price freshness (15 minutes)
    uint256 constant PRICE_FRESHNESS_WINDOW = 15 minutes;

    // Storage for latest verified price
    uint256 public latestPrice;
    uint256 public latestTimestamp;

    event PriceVerified(uint256 price, uint256 timestamp, string source);

    error InvalidSignature();
    error InvalidAttestationType();
    error InvalidComplianceStatus();
    error DebuggingEnabled();
    error InvalidVMPL();
    error InvalidNonce();
    error StalePrice();

    function verifyAttestedPrice(
        bytes calldata message,
        bytes calldata signature,
        bytes calldata exponent,
        bytes calldata modulus,
        uint256 price,
        string calldata nonce,
        uint256 timestamp,
        string calldata attestationType,
        string calldata complianceStatus,
        bool isDebuggable,
        uint8 vmpl
    ) external returns (bool) {
        // 1. Verify RSA signature [this proves the attestation report wasn't tampered with]
        if (!RsaVerify.pkcs1Sha256Raw(message, signature, exponent, modulus)) {
            revert InvalidSignature();
        }

        // 2. Verify security claims [these prove the TEE was configured securely]
        if (!_compareStrings(attestationType, EXPECTED_ATTESTATION_TYPE)) {
            revert InvalidAttestationType();
        }

        if (!_compareStrings(complianceStatus, EXPECTED_COMPLIANCE_STATUS)) {
            revert InvalidComplianceStatus();
        }

        if (isDebuggable) {
            revert DebuggingEnabled();
        }

        if (vmpl != EXPECTED_VMPL) {
            revert InvalidVMPL();
        }

        // 3. Verify price source and freshness
        if (!_compareStrings(nonce, "coinmarketcap.com")) {
            revert InvalidNonce();
        }

        if (block.timestamp > timestamp + PRICE_FRESHNESS_WINDOW) {
            revert StalePrice();
        }

        // 4. Store verified price
        latestPrice = price;
        latestTimestamp = timestamp;

        emit PriceVerified(price, timestamp, nonce);
        return true;
    }

    function _compareStrings(
        string memory a,
        string memory b
    ) internal pure returns (bool) {
        return keccak256(abi.encodePacked(a)) == keccak256(abi.encodePacked(b));
    }

    // View function to get latest verified price if not stale
    function getVerifiedPrice()
        external
        view
        returns (uint256 price, uint256 timestamp)
    {
        require(
            block.timestamp <= latestTimestamp + PRICE_FRESHNESS_WINDOW,
            "Price is stale"
        );
        return (latestPrice, latestTimestamp);
    }
}
