from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5, PKCS1_OAEP
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Signature import PKCS1_v1_5 as PK
import zlib
import base64
import os
from Crypto.Hash import SHA256

def sign_blob(blob, private_key):
    #compress the data first
    blob = zlib.compress(blob)

    #In determining the chunk size, determine the private key length used in bytes
    #and subtract 42 bytes (when using PKCS1_OAEP). The data will be in encrypted
    #in chunks
    chunk_size = 86
    offset = 0
    end_loop = False
    signed =  b""

    # sign the message by using sender's private key
    signer = PK.new(RSA.importKey(private_key))
    
    while not end_loop:
        #The chunk
        chunk = blob[offset:offset + chunk_size]
        digest = SHA256.new()
        digest.update(chunk)
        
        #If the data chunk is less then the chunk size, then we need to add
        #padding with " ". This indicates the we reached the end of the file
        #so we end loop here
        if len(chunk) % chunk_size != 0:
            end_loop = True
            chunk += b" " * (chunk_size - len(chunk))

        #Append the encrypted chunk to the overall encrypted file
        signed += signer.sign(digest)

        #Increase the offset by chunk size
        offset += chunk_size

    print("[ The file is signed ]")

    return signed

def verify_blob(signed_blob, original, public_key):
    original = zlib.compress(original)

    #In determining the chunk size, determine the private key length used in bytes.
    #The data will be in decrypted in chunks
    chunk_size = 128
    offset = 0
    verification = True

    og_chunk_size = 86
    og_offset = 0

    verifier = PKCS115_SigScheme(RSA.importKey(public_key))

    #keep loop going as long as we have chunks to decrypt
    while offset < len(signed_blob):
        #The chunk
        chunk = signed_blob[offset: offset + chunk_size]
        #The og chunk
        og_chunk = original[og_offset:og_offset + og_chunk_size]

        hash = SHA256.new(og_chunk)
        try:
            # verify the signed message
            verifier.verify(hash, chunk)
        except:
            print("[ Signature is Invalid. ]")
            verification = False

        #Increase the offset by chunk size
        offset += chunk_size
        og_offset += og_chunk_size

    #return the decompressed decrypted data
    return verification

# Use RSA to generate CA's key pairs
KeyPair = RSA.generate(bits=1024)

privKey = KeyPair.exportKey('PEM')
pubKey = KeyPair.publickey().exportKey('PEM')

filepath = input(r'')

with open(filepath, 'rb') as file:
        original = file.read()

signed_blob = sign_blob(original, privKey)
verification = verify_blob(signed_blob, original, pubKey)
print(verification)