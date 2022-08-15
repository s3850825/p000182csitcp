from brownie import accounts, config, RSACertification, network
from scripts.account import get_account


def deploy_certification():
    # get account
    account = get_account()

    # deploy RSA certificate contract
    certification = RSACertification.deploy({"from": account})


def create_certificate(name, public_key):
    # get account
    account = get_account()

    # get the most recent contract deployed
    certification = RSACertification[-1]

    # create a transaction
    transaction = certification.createCertificate(name, public_key, {"from": account})
    transaction.wait(1)


def get_certificate(KeyPair):
    # get account
    account = get_account()

    # get the most recent contract deployed
    certification = RSACertification[-1]

    # show certificate information
    name = certification.getName({"from": account})
    signed_public_key = certification.getSignedPublicKey(KeyPair.n, KeyPair.d, {"from": account})
    timestamp = certification.getTimestamp({"from": account})
    print("------------------------------------")
    print("\t  certificate")
    print("name: ", name)
    print("signed_public_key: ", signed_public_key)
    print("timestamp: ", timestamp)
    print("------------------------------------")
