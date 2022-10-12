from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5, PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5 as PK
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import zlib
import base64
from scripts.deploy import *
from scripts.account import *
import os

def encrypt_message(database, receiver, message):
    # This is from DB
    # pubKey1 = database.getStudentPublicKey(receiver)
    # This is from Blockchain
    walletPassword = database.getStudentWalletPassword(receiver)
    print("[ Retrieve", receiver, "'s public key from Blockchain ]")

    # get receiver's public key from Blockchain
    pubKey = get_public_key(walletPassword, database)
    # encrypt message
    cipher = PKCS1_v1_5.new(RSA.importKey(pubKey))
    encrypt_message = cipher.encrypt(message.encode())
    print("[ A message is encrypted ]")
    return encrypt_message

def decrypt_message(path, encryptedMessage):
    try:
        # read the private key by using the path
        PrivKeyFile = open(path, 'rb')
        privKey = PrivKeyFile.read()
        # decrypt message
        decipher = PKCS1_v1_5.new(RSA.importKey(privKey))
        decryptMessage = decipher.decrypt(encryptedMessage, None).decode()
        print("[ Encrypted message is decrypted ]")
    except:
        print("[ Invalid private key ]")
        return ""

    return decryptMessage

def load_priv_key(path):
    try:
        # read the private key by using the path
        PrivKeyFile = open(path, 'rb')
        privKey = PrivKeyFile.read()
    except:
        return None

    return privKey

def sign_message(database, privKey, message):
    # hash the message
    digest = SHA256.new()
    digest.update(message.encode('utf-8'))

    # sign the message by using sender's private key
    signer = PK.new(RSA.importKey(privKey))
    signature = signer.sign(digest)
    print("[ A message is signed ]")

    return signature

def sign_encrypted_message(database, privKey, encryptedMessage):
    # hash the message
    digest = SHA256.new()
    digest.update(encryptedMessage)
    
    # sign the message by using sender's private key
    signer = PK.new(RSA.importKey(privKey))
    signature = signer.sign(digest)
    print("[ A message is signed ]")

    return signature

def verify_message(database, sender, signedMessage, og_message):
    walletPassword = database.getStudentWalletPassword(sender)
    print("[ Retrieve", sender, "'s public key from Blockchain ]")
    
    # get receiver's public key from Blockchain
    pubKey = get_public_key(walletPassword, database)

    # verify the signed message by using sender's public key
    verifier = PKCS115_SigScheme(RSA.importKey(pubKey))
    hash = SHA256.new(str.encode(og_message))
    try:
        # verify the signed message
        verifier.verify(hash, signedMessage)
        print("[ Signature is valid. ]")
        return True
    except:
        print("[ Signature is Invalid. ]")
        return False

def verify_encryptedMessage(database, sender, signedEncryptedMessage, encryptedMessage):
    walletPassword = database.getStudentWalletPassword(sender)
    print("[ Retrieve", sender, "'s public key from Blockchain ]")
    
    # get receiver's public key from Blockchain
    pubKey = get_public_key(walletPassword, database)

    # verify the signed message by using sender's public key
    verifier = PKCS115_SigScheme(RSA.importKey(pubKey))
    hash = SHA256.new(encryptedMessage)
    try:
        # verify the signed message
        verifier.verify(hash, signedEncryptedMessage)
        print("[ Signature is valid. ]")
        return True
    except:
        print("[ Signature is Invalid. ]")
        return False

# ref: https://ismailakkila.medium.com/black-hat-python-encrypt-and-decrypt-with-rsa-cryptography-bd6df84d65bc
def encrypt_blob(blob, public_key):
    #Import the Public Key and use for encryption using PKCS1_OAEP
    rsa_key = RSA.importKey(public_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)

    #compress the data first
    blob = zlib.compress(blob)

    #In determining the chunk size, determine the private key length used in bytes
    #and subtract 42 bytes (when using PKCS1_OAEP). The data will be in encrypted
    #in chunks
    chunk_size = 86
    offset = 0
    end_loop = False
    encrypted =  b""

    while not end_loop:
        #The chunk
        chunk = blob[offset:offset + chunk_size]

        #If the data chunk is less then the chunk size, then we need to add
        #padding with " ". This indicates the we reached the end of the file
        #so we end loop here
        if len(chunk) % chunk_size != 0:
            end_loop = True
            chunk += b" " * (chunk_size - len(chunk))

        #Append the encrypted chunk to the overall encrypted file
        encrypted += rsa_key.encrypt(chunk)

        #Increase the offset by chunk size
        offset += chunk_size

    print("[ The file is encrypted ]")
    #Base 64 encode the encrypted file
    return base64.b64encode(encrypted)

def decrypt_blob(encrypted_blob, private_key):

    #Import the Private Key and use for decryption using PKCS1_OAEP
    rsakey = RSA.importKey(private_key)
    rsakey = PKCS1_OAEP.new(rsakey)

    #Base 64 decode the data
    encrypted_blob = base64.b64decode(encrypted_blob)

    #In determining the chunk size, determine the private key length used in bytes.
    #The data will be in decrypted in chunks
    chunk_size = 128
    offset = 0
    decrypted = b""

    #keep loop going as long as we have chunks to decrypt
    while offset < len(encrypted_blob):
        #The chunk
        chunk = encrypted_blob[offset: offset + chunk_size]

        #Append the decrypted chunk to the overall decrypted file
        decrypted += rsakey.decrypt(chunk)

        #Increase the offset by chunk size
        offset += chunk_size

    #return the decompressed decrypted data
    return zlib.decompress(decrypted)

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

def encrypt_file(database, receiver, filepath):
    walletPassword = database.getStudentWalletPassword(receiver)
    print("[ Retrieve", receiver, "'s public key from Blockchain ]")

    # get receiver's public key from Blockchain
    pubKey = get_public_key(walletPassword, database)

    with open(filepath, 'rb') as file:
        original = file.read()

    return encrypt_blob(original, pubKey)

def decrypt_file(filepath, encrypted_file, filename):
    try:
        # read the private key by using the path
        PrivKeyFile = open(filepath, 'rb')
        privKey = PrivKeyFile.read()

        # decrypt file and save
        # print(os.getcwd())
        filepath2 = os.getcwd() + "\\" + filename
        # print(filepath2)

        with open(filepath2, 'wb') as file:
            file.write(decrypt_blob(encrypted_file, privKey))

        print("[ Encrypted file is decrypted and saved]")
    except:
        print("[ Invalid private key ]")
        return ""
    
def sign_file(privKey, filepath):
    with open(filepath, 'rb') as file:
        original = file.read()

    return sign_blob(original, privKey)

def verify_file(database, sender, original, signed_blob):
    walletPassword = database.getStudentWalletPassword(sender)
    print("[ Retrieve", sender, "'s public key from Blockchain ]")

    # get receiver's public key from Blockchain
    pubKey = get_public_key(walletPassword, database)

    return verify_blob(signed_blob, original, pubKey)

def open_original_file(filepath):
    with open(filepath, 'rb') as file:
        original = file.read()

    return original
