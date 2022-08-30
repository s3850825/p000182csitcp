from Crypto.PublicKey import RSA

def generate_CA_key_pairs():
    # Use RSA to generate CA's key pairs
    KeyPair = RSA.generate(bits=1024)

    return KeyPair