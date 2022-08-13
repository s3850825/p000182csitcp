from OpenSSL import crypto, SSL

def generate_CA_key_pairs():

    pkey = crypto.PKey()
    # 1024bit RSA type key pairs
    pkey.generate_key(crypto.TYPE_RSA, 1024)
    public_key = crypto.dump_publickey(crypto.FILETYPE_PEM, pkey)
    private_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, pkey)
    print(public_key, private_key)

    return public_key, private_key