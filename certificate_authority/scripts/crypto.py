from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Signature import PKCS1_v1_5 as PK
from Crypto.Hash import SHA256
from scripts.deploy import *
from scripts.account import *

def encrypt_message(database, receiver, message):
    # This is from DB
    # pubKey1 = database.getStudentPublicKey(receiver)
    # This is from Blockchain
    walletPassword = database.getStudentWalletPassword(receiver)
    pubKey = get_public_key(walletPassword)
    cipher = PKCS1_v1_5.new(RSA.importKey(pubKey))
    encrypt_message = cipher.encrypt(message.encode())
    return encrypt_message

def decrypt_message(database, privKey, encryptedMessage):
    try:
        decipher = PKCS1_v1_5.new(RSA.importKey(privKey))
        decryptMessage = decipher.decrypt(encryptedMessage, None).decode()
    except:
        print("Invalid private key")
        return ""

    return decryptMessage

def sign_message(database, privKey, message):
    digest = SHA256.new()
    digest.update(message.encode('utf-8'))

    signer = PK.new(RSA.importKey(privKey))
    signature = signer.sign(digest)
    print(signature)
    return signature