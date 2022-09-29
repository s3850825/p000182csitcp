from Crypto.PublicKey import RSA

def generate_RSA_key_pairs():
    # Use RSA to generate CA's key pairs
    KeyPair = RSA.generate(bits=1024)

    privKey = KeyPair.exportKey('PEM')
    pubKey = KeyPair.publickey().exportKey('PEM')
    return privKey, pubKey