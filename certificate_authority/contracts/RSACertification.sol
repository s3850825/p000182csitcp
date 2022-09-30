// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract RSACertification {
    struct Certificate {
        address certificate_owner;
        string name;
        bytes public_key_part1;
        bytes public_key_part2;
        bytes public_key_part3;
        bytes public_key_part4;
        bytes public_key_part5;
        bytes public_key_part6;
        bytes public_key_part7;
        bytes public_key_part8;
        bytes public_key_part9;
        uint256 timestamp;
    }

    mapping(address => Certificate) public nameToCertificate;

    // create a certificate
    function createCertificate(
        string memory _name,
        bytes memory _public_key_part1,
        bytes memory _public_key_part2,
        bytes memory _public_key_part3,
        bytes memory _public_key_part4,
        bytes memory _public_key_part5,
        bytes memory _public_key_part6,
        bytes memory _public_key_part7,
        bytes memory _public_key_part8,
        bytes memory _public_key_part9
    ) public {
        nameToCertificate[msg.sender] = Certificate(
            msg.sender,
            _name,
            _public_key_part1,
            _public_key_part2,
            _public_key_part3,
            _public_key_part4,
            _public_key_part5,
            _public_key_part6,
            _public_key_part7,
            _public_key_part8,
            _public_key_part9,
            block.timestamp
        );
    }

    // signature using RSA
    // function signWithRSA() private view returns (bytes32[] memory) {
    //     bytes32[] memory signatures = new bytes32[](4);
    //     signatures[0] = nameToCertificate[msg.sender].signature_part1;
    //     signatures[1] = nameToCertificate[msg.sender].signature_part2;
    //     signatures[2] = nameToCertificate[msg.sender].signature_part3;
    //     signatures[3] = nameToCertificate[msg.sender].signature_part4;
    //     return signatures;
    // }

    // verification using RSA
    // function verifyWithRSA(bool result) public view returns (bool) {
    //     return result;
    // }

    function getName() public view returns (string memory) {
        return nameToCertificate[msg.sender].name;
    }

    function getPublicKey() public view returns (bytes[] memory) {
        bytes[] memory public_keys = new bytes[](9);
        public_keys[0] = nameToCertificate[msg.sender].public_key_part1;
        public_keys[1] = nameToCertificate[msg.sender].public_key_part2;
        public_keys[2] = nameToCertificate[msg.sender].public_key_part3;
        public_keys[3] = nameToCertificate[msg.sender].public_key_part4;
        public_keys[4] = nameToCertificate[msg.sender].public_key_part5;
        public_keys[5] = nameToCertificate[msg.sender].public_key_part6;
        public_keys[6] = nameToCertificate[msg.sender].public_key_part7;
        public_keys[7] = nameToCertificate[msg.sender].public_key_part8;
        public_keys[8] = nameToCertificate[msg.sender].public_key_part9;
        return public_keys;
    }

    function getTimestamp() public view returns (uint256) {
        return nameToCertificate[msg.sender].timestamp;
    }
}
