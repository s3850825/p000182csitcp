from brownie import accounts, config, RSACertification, network
from scripts.account import get_account
from Crypto.Hash import SHA256
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme

def deploy_certification(walletPassword):
    # get account
    account = get_account(walletPassword)

    # deploy RSA certificate contract
    certification = RSACertification.deploy({"from": account})


def create_certificate(name, user_public_key, walletPassword):
    # get account
    account = get_account(walletPassword)

    # get the most recent contract deployed
    certification = RSACertification[-1]
    user_public_key1 = user_public_key[0:32]
    user_public_key2 = user_public_key[32:64]
    user_public_key3 = user_public_key[64:96]
    user_public_key4 = user_public_key[96:128]
    user_public_key5 = user_public_key[128:160]
    user_public_key6 = user_public_key[160:192]
    user_public_key7 = user_public_key[192:224]
    user_public_key8 = user_public_key[224:256]
    user_public_key9 = user_public_key[256:]
    # create a transaction
    transaction = certification.createCertificate(name, user_public_key1, user_public_key2, user_public_key3, user_public_key4, user_public_key5, user_public_key6, user_public_key7, user_public_key8, user_public_key9, {"from": account})
    transaction.wait(1)


def get_public_key(walletPassword):
    # get account
    account = get_account(walletPassword)

    # get the most recent contract deployed
    certification = RSACertification[-1]

    # show certificate information
    name = certification.getName({"from": account})
    public_keys = certification.getPublicKey({"from": account})
    print(public_keys)
    publicKey = b''
    for p in public_keys:
        publicKey += p
    
    print(publicKey)

    timestamp = certification.getTimestamp({"from": account})

    print("------------------------------------")
    print("\t  certificate")
    print("name: ", name)
    print("public_key: ", publicKey)
    print("timestamp: ", timestamp)
    print("------------------------------------")

    return publicKey