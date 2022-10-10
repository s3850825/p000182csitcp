from Crypto.PublicKey import RSA

def generate_RSA_key_pairs(studentName):
    # Use RSA to generate CA's key pairs
    KeyPair = RSA.generate(bits=1024)

    privKey = KeyPair.exportKey('PEM')
    pubKey = KeyPair.publickey().exportKey('PEM')

    #save PEM key into the file
    with open(studentName + '_private.pem', 'wb') as file:
        file.write(privKey)

    with open(studentName+ '_public.pem', 'wb') as file:
        file.write(pubKey)

    return privKey, pubKey