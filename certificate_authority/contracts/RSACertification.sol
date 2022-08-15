// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract RSACertification {
    struct Certificate {
        address certificate_owner;
        string name;
        uint256 public_key;
        //uint256 signature;
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
    function signWithRSA(
        uint256 public_key,
        uint256 n,
        uint256 d
    ) private view returns (uint256) {
        uint256 signature = public_key**d % n;
        return signature;
    }

    // verification using RSA
    function verifyWithRSA(
        uint256 public_key,
        uint256 signature,
        uint256 e,
        uint256 n
    ) public view returns (bool) {
        uint256 result = signature**e % n;
        return result == public_key;
    }

    function getName() public view returns (string memory) {
        return nameToCertificate[msg.sender].name;
    }

    function getSignedPublicKey(uint256 n, uint256 d)
        public
        view
        returns (uint256)
    {
        return signWithRSA(nameToCertificate[msg.sender].public_key, n, d);
    }

    function getTimestamp() public view returns (uint256) {
        return nameToCertificate[msg.sender].timestamp;
    }
}
