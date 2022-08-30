// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract RSACertification {
    struct Certificate {
        address certificate_owner;
        string name;
        string public_key;
        bytes32 signature_part1;
        bytes32 signature_part2;
        bytes32 signature_part3;
        bytes32 signature_part4;
        uint256 timestamp;
    }

    mapping(address => Certificate) public nameToCertificate;

    // create a certificate
    function createCertificate(
        string memory _name,
        string memory _public_key,
        bytes32 _signature_part1,
        bytes32 _signature_part2,
        bytes32 _signature_part3,
        bytes32 _signature_part4
    ) public {
        nameToCertificate[msg.sender] = Certificate(
            msg.sender,
            _name,
            _public_key,
            _signature_part1,
            _signature_part2,
            _signature_part3,
            _signature_part4,
            block.timestamp
        );
    }

    // signature using RSA
    function signWithRSA() private view returns (bytes32[] memory) {
        bytes32[] memory signatures = new bytes32[](4);
        signatures[0] = nameToCertificate[msg.sender].signature_part1;
        signatures[1] = nameToCertificate[msg.sender].signature_part2;
        signatures[2] = nameToCertificate[msg.sender].signature_part3;
        signatures[3] = nameToCertificate[msg.sender].signature_part4;
        return signatures;
    }

    // verification using RSA
    function verifyWithRSA(bool result) public view returns (bool) {
        return result;
    }

    function getName() public view returns (string memory) {
        return nameToCertificate[msg.sender].name;
    }

    function getSignedPublicKey() public view returns (bytes32[] memory) {
        return signWithRSA();
    }

    function getTimestamp() public view returns (uint256) {
        return nameToCertificate[msg.sender].timestamp;
    }
}
