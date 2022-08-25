from brownie import accounts, config, RSACertification, network
from scripts.account import get_account
from Crypto.Hash import SHA256
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme

def deploy_certification():
    # get account
    account = get_account()

    # deploy RSA certificate contract
    certification = RSACertification.deploy({"from": account})


def create_certificate(name, user_public_key, KeyPair):
    # get account
    account = get_account()

    # get the most recent contract deployed
    certification = RSACertification[-1]

    user_public_key_bytes = str.encode(str(user_public_key))
    hash = SHA256.new(user_public_key_bytes)
    signer = PKCS115_SigScheme(KeyPair)
    signature = signer.sign(hash)

    # create a transaction
    transaction = certification.createCertificate(name, str(user_public_key), str(signature), {"from": account})
    transaction.wait(1)


def get_certificate(KeyPair):
    # get account
    account = get_account()

    # get the most recent contract deployed
    certification = RSACertification[-1]

    # show certificate information
    name = certification.getName({"from": account})

    signed_public_key = certification.getSignedPublicKey({"from": account})
    timestamp = certification.getTimestamp({"from": account})
    print("------------------------------------")
    print("\t  certificate")
    print("name: ", name)
    print("signed_public_key: ", signed_public_key)
    print("timestamp: ", timestamp)
    print("------------------------------------")
