from Crypto.Hash import SHA256
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.PublicKey import RSA
import sys
import binascii
from binascii import unhexlify
import codecs 
KeyPair = RSA.generate(bits=1024)

k = 'wn\x04\x03\xd7\xf6\xca\x7fyT\xd0z\x1b\xb2\xb1'
k_byte = str.encode(k)

hash = SHA256.new(k_byte)
signer = PKCS115_SigScheme(KeyPair)
signature = signer.sign(hash)
print(signature)
str_sig = str(signature)
s = str_sig[2:-1]
print(s)
alist = s.split("\\")
print("--------------")
newList = []
for x in alist:
    if x != '':
        # print(str.encode(x))
        newList.append(str.encode(x))
print(newList)
print("--------------")
a = b' \\'.join(newList)
print(a)
print(type(a))

