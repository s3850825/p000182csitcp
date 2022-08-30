from brownie import accounts, config, RSACertification, network
from scripts.account import get_account
from Crypto.Hash import SHA256
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme

def verify_signature(user_public_key, KeyPair):
    # get account
    account = get_account()

    # get the most recent contract deployed
    certification = RSACertification[-1]

    # show certificate information
    name = certification.getName({"from": account})

    # get the array of signature from the certificate and convert to bytes
    signed_public_key = certification.getSignedPublicKey({"from": account})
    signature = b''
    for s in signed_public_key:
        signature += s
        
    # verify user's public key by using CA's public key
    user_publick_key_bytes = str.encode(str(user_public_key))
    verifier = PKCS115_SigScheme(KeyPair.public_key())
    hash = SHA256.new(user_publick_key_bytes)
    try:
        verifier.verify(hash, signature)
        verification = certification.verifyWithRSA(True)
        print("Signature is valid.")
    except:
        verification = certification.verifyWithRSA(False)
        print("Signature is Invalid.")

    # verify RSA signature
    # verification = certification.verifyWithRSA(public_key, signed_public_key, KeyPair.e, KeyPair.n)
    print("------------------------------------")
    print("signature verification: ", verification)
    print("------------------------------------")
