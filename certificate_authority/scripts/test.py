from scripts.deploy import deploy_certification, create_certificate, get_certificate
from scripts.verification import verify_signature
from scripts.keyGeneration import generate_CA_key_pairs
from Crypto.Hash import SHA256
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
import binascii
from interfaces.frontend.main import frontend_main

def main():
    KeyPair = generate_CA_key_pairs()

    # open frontend UI
    frontend_main()

    # we need to run these in frontend UI
    # deploy_certification()
    # user_publickey = 123
    # create_certificate("Alice", user_publickey, KeyPair)
    # get_certificate(KeyPair)
    # verify_signature(user_publickey, KeyPair)