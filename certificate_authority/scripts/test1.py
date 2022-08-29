from Crypto.Hash import SHA256
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.PublicKey import RSA
import sys
import binascii
from binascii import unhexlify
import codecs 


public_key = 1234

KeyPair = RSA.generate(bits=1024)
pb_bytes = str.encode(str(public_key))
hash = SHA256.new(pb_bytes)
signer = PKCS115_SigScheme(KeyPair)
signature = signer.sign(hash)

signature1 = signature[0:32]
signature2 = signature[32:64]
signature3 = signature[64:96]
signature4 = signature[96:128]

user_publick_key_bytes = str.encode(str(public_key))
verifier = PKCS115_SigScheme(KeyPair.public_key())
hash = SHA256.new(user_publick_key_bytes)

try:
    verifier.verify(hash, signature1 + signature2 + signature3 + signature4)
    print("Signature is valid.")
except:
    print("Signature is Invalid.")

# print("--- Original Signature ---\n", signature)
# print("\n")
# # Passed as string in Solidity
# str_signature = str(signature)
# print("--- String of Signature ---\n", str_signature)
# print("\n")
# str_siganture_bytes = str.encode(str_signature)
# print("--- String to bytes signature\n", str_siganture_bytes)
# print("\n")
