from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5, PKCS1_OAEP
import zlib
import base64
import os

# # Use RSA to generate CA's key pairs
# KeyPair = RSA.generate(bits=1024)

# privKey = KeyPair.exportKey('PEM')
# pubKey = KeyPair.publickey().exportKey('PEM')


# filepath = input(r'Path: ')

# with open(filepath, 'rb') as file:
#     original = file.read()

# encrypted_blob = encrypt_blob(original, pubKey)

# filepath2 = input(r'Paht2: ')
# with open(filepath2, 'wb') as file:
#     file.write(decrypt_blob(encrypted_blob, privKey))

filepath = r"F:\Project files\p000182csitcp\certificate_authority\alice_private.pem"
with open (filepath, 'rb') as file:
    original = file.read()

print(original)