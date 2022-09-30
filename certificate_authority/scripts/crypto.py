from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Signature import PKCS1_v1_5 as PK
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
from scripts.deploy import *
from scripts.account import *

def encrypt_message(database, receiver, message):
    # This is from DB
    # pubKey1 = database.getStudentPublicKey(receiver)
    # This is from Blockchain
    walletPassword = database.getStudentWalletPassword(receiver)
    print("[ Retrieve", receiver, "'s public key from Blockchain ]")

    pubKey = get_public_key(walletPassword, database)
    cipher = PKCS1_v1_5.new(RSA.importKey(pubKey))
    encrypt_message = cipher.encrypt(message.encode())
    print("[ A message is encrypted ]")
    return encrypt_message

def decrypt_message(path, encryptedMessage):
    try:
        PrivKeyFile = open(path, 'rb')
        privKey = PrivKeyFile.read()
        decipher = PKCS1_v1_5.new(RSA.importKey(privKey))
        decryptMessage = decipher.decrypt(encryptedMessage, None).decode()
        print("[ Encrypted message is decrypted ]")
    except:
        print("[ Invalid private key ]")
        return ""

    return decryptMessage

def load_priv_key(path):
    PrivKeyFile = open(path, 'rb')
    privKey = PrivKeyFile.read()

    return privKey

def sign_message(database, privKey, message):
    digest = SHA256.new()
    digest.update(message.encode('utf-8'))

    signer = PK.new(RSA.importKey(privKey))
    signature = signer.sign(digest)
    print("[ A message is signed ]")

    return signature

def verify_message(database, sender, signedMessage, og_message):
    walletPassword = database.getStudentWalletPassword(sender)
    print("[ Retrieve", sender, "'s public key from Blockchain ]")
    pubKey = get_public_key(walletPassword, database)

    # verify the signed message by using sender's public key
    verifier = PKCS115_SigScheme(RSA.importKey(pubKey))
    hash = SHA256.new(str.encode(og_message))
    try:
        verifier.verify(hash, signedMessage)
        print("Signature is valid.")
        return True
    except:
        print("Signature is Invalid.")
        return False