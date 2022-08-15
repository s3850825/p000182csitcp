from scripts.deploy import deploy_certification, create_certificate, get_certificate
from scripts.verification import verify_signature
from scripts.keyGeneration import generate_CA_key_pairs
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

def main():
    KeyPair = generate_CA_key_pairs()

    # publickey = "1234"
    # digest = SHA256.new()
    # digest.update(publickey.encode('utf-8'))

    # signer = PKCS1_v1_5.new(keyPair)
    # signature = signer.sign(digest)

    # print(signature)

    deploy_certification()
    create_certificate("Alice", 123)
    get_certificate(KeyPair)
    verify_signature(123, 30, KeyPair)