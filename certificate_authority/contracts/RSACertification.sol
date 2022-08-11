// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract RSACertification {
    // RSA key pair
    uint256 d = 23;
    uint256 n = 187;
    uint256 e = 7;

    struct Certificate {
        address certificate_owner;
        string name;
        uint256 public_key;
        uint256 timestamp;
    }

    mapping(address => Certificate) public nameToCertificate;

    // create a certificate
    function createCertificate(string memory _name, uint256 _public_key)
        public
    {
        nameToCertificate[msg.sender] = Certificate(
            msg.sender,
            _name,
            _public_key,
            block.timestamp
        );
    }

    // signature using RSA
    function signWithRSA(uint256 public_key) private view returns (uint256) {
        uint256 signature = public_key**d % n;
        return signature;
    }

    // verification using RSA
    function verifyWithRSA(uint256 public_key, uint256 signature)
        public
        view
        returns (bool)
    {
        uint256 result = signature**e % n;
        return result == public_key;
    }

    function getName() public view returns (string memory) {
        return nameToCertificate[msg.sender].name;
    }

    function getSignedPublicKey() public view returns (uint256) {
        return signWithRSA(nameToCertificate[msg.sender].public_key);
    }

    function getTimestamp() public view returns (uint256) {
        return nameToCertificate[msg.sender].timestamp;
    }
}
