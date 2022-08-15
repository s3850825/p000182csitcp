from brownie import accounts, config, RSACertification, network


def verify_signature(public_key, signed_public_key, KeyPair):
    # get the most recent contract deployed
    certification = RSACertification[-1]

    # verify RSA signature
    verification = certification.verifyWithRSA(public_key, signed_public_key, KeyPair.e, KeyPair.n)
    print("------------------------------------")
    print("signature verification: ", verification)
    print("------------------------------------")
