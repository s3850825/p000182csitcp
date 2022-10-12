import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap
from interfaces.login import *
from interfaces.sign_up import *
from interfaces.MainPage import *
from interfaces.MessageBoard import *
from interfaces.KeyPairs import *
from interfaces.user import *
from interfaces.SendMessage import *
from interfaces.FileBoard import *
from interfaces.SendFile import *
from scripts.crypto import *
from scripts.deploy import *
from db.database import *
from db.databaseOracle import *
from scripts.keyGeneration import *
import datetime

def frontend_UI():
    app = QApplication([])
    # Log in page widget
    widget_login = QWidget()
    ui = Ui_Login()
    ui.setupUi(widget_login)
    widget_login.show()

    # Main page widget
    ui_mainPage = Ui_MainPage()
    widget_MainPage = QWidget()
    ui_mainPage.setupUi(widget_MainPage)

    # Sign up page widget
    widget_sign = QWidget()
    ui_sign = Ui_Sign_Up()
    ui_sign.setupUi(widget_sign)

    # Message board page widget
    widget_message = QWidget()
    ui_message = Ui_MessageBoard()
    ui_message.setupUi(widget_message)

    # Send a message page widget
    widget_send_message = QWidget()
    ui_send_message = Ui_Send_Message()
    ui_send_message.setupUi(widget_send_message)

    # File board page widget
    widget_file = QWidget()
    ui_file = Ui_FileBoard()
    ui_file.setupUi(widget_file)

    # Send a file page widget
    widget_send_file = QWidget()
    ui_send_file = Ui_Send_File()
    ui_send_file.setupUi(widget_send_file)

    # connect to DB
    # database = Database()
    database = DatabaseOracle()

    # Logged in user
    user = User()

    # Message board button event
    ui_mainPage.LinkBtnMessageBoard.clicked.connect(
        lambda: {
            ui_message.showReceivedMessages(database, user),
            widget_message.show()
        }
    )
    # Log out button event
    ui_mainPage.LogOutButton.clicked.connect(
        lambda: {
            ui_mainPage.logout(user, widget_MainPage, widget_login),
            ui_send_message.privateKeyPathclear(),
            ui_message.privateKeyPathclear()
        }
    )    
    # Download key pairs button event
    ui_mainPage.DownloadKeyButton.clicked.connect(
        lambda: {
            ui_mainPage.downloadKeyPairs(database, user)
        }
    ) 
    # Register button event
    ui.LinkBtnRegister.clicked.connect(
        lambda: {
            widget_sign.show()
        }
    )
    # Login button event
    ui.LoginButton.clicked.connect(
        lambda: {
            checkLoginInfo(database, ui.returnStudentInfo(), ui, widget_login, widget_MainPage, user, ui_mainPage)
        }
    )
    # Sign up button event
    ui_sign.SignUpButton.clicked.connect(
        lambda: {
            checkStudentInfo(database, ui_sign.returnStudentInfo(), ui_sign, widget_sign)
        }
    )
    # Send a message button event
    ui_mainPage.SendMessageButton.clicked.connect(
        lambda: {
            sendMessage(database, user, ui_send_message, widget_send_message)
        }
    )
    # Encrypt and Sign text button event
    ui_send_message.EncryptAndSignButton.clicked.connect(
        lambda: {
            checkEncryptAndSignMessage(database, ui_send_message, widget_send_message)
        }
    )
    # Encrypt text button event
    ui_send_message.EncryptButton.clicked.connect(
        lambda: {
            checkEncryptMessage(database, ui_send_message, widget_send_message)
        }
    )
    # Decrypt text button event
    ui_message.decryptButton.clicked.connect(
        lambda: {
            ui_message.uploadPrivateKey(database)
        }
    )
    # Signature text button event
    ui_send_message.SignatureButton.clicked.connect(
        lambda: {
            getSenderPrivateKey(database, ui_send_message, widget_send_message)
        }
    )
    # Validate text button event
    ui_message.validateButton.clicked.connect(
        lambda: {
            validateSignedMessage(database, ui_message)
        }
    )
    # File board button event
    ui_mainPage.CheckFilesButton.clicked.connect(
        lambda: {
            ui_file.showReceivedFiles(database, user),
            widget_file.show()
        }
    )
    # Send a file button event
    ui_mainPage.SendFileButton.clicked.connect(
        lambda: {
            sendFile(database, user, ui_send_file, widget_send_file)
        }
    )
    # Encrypt a file button event
    ui_send_file.EncryptButton.clicked.connect(
        lambda: {
            checkEncryptFile(database, ui_send_file, widget_send_file)
        }
    )
    # Decrypt a file button event
    ui_file.decryptButton.clicked.connect(
        lambda: {
            ui_file.uploadPrivateKey(database)
        }
    )
    # Sign a file button event
    ui_send_file.SignatureButton.clicked.connect(
        lambda: {
            checkSignFile(database, ui_send_file, widget_send_file)
        }
    )
    # verify a signed file button event
    ui_file.validateButton.clicked.connect(
        lambda: {
            verifySignedFile(database, ui_file, widget_file)
        }
    )
    # Encrypt and sign a file button event
    ui_send_file.EncryptAndSignButton.clicked.connect(
        lambda: {
            checkEncryptAndSignFile(database, ui_send_file, widget_send_file)
        }
    )
    # Verify the encrypted file button event

    sys.exit(app.exec_())


def currentTime():
    # check current time
    x = datetime.datetime.now()
    time = str(x.year)+"-"+str(x.month).rjust(2, '0')+"-"+str(x.day).rjust(2, '0')+" "+ str(x.hour).rjust(2, '0')+":"+str(x.minute).rjust(2, '0')+":"+str(x.second).rjust(2, '0')
    return time

def checkStudentInfo(database, studentInfo, ui_sign, widget_sign):
    studentName, studentPassword, studentPassword2, studentWalletPassword = studentInfo
    # check if student name already exists in DB, and password and password check are same
    if database.checkUniqueStudentName(studentInfo[0]) and studentPassword == studentPassword2:
        database.insertNewStudent(studentName, studentPassword, studentWalletPassword)
        
        # generate key pairs
        privKey, pubKey = generate_RSA_key_pairs(studentName)

        # Blockchain
        deploy_certification(studentWalletPassword)
        create_certificate(studentName, pubKey, studentWalletPassword)
        
        # save into DB
        database.updateNewStudentKeyPairs(privKey, pubKey, studentName)

        # reset all the textboxes
        ui_sign.reset()
        widget_sign.close()
        print("[", studentName, 'is registered! ]')
    else:
        # reset all the textboxes
        ui_sign.reset()
        print("[", studentInfo[0], " is already registered ]")

def checkLoginInfo(database, studentInfo, ui, widget_login, widget_MainPage, user, ui_mainPage):
    studentName, studentPassword = studentInfo
    # check if student name exists in DB
    if database.checkStudentInfo(studentInfo[0], studentInfo[1]):
        ui.reset()
        # once user logged in all the information is saved into user object 
        user.setStudentInfo(studentName, database)
        # show student name on main page
        ui_mainPage.showStudentName(user)
        widget_login.close()
        widget_MainPage.show()
    else:
        # reset all the textboxes
        ui.reset()
        print("[ Log in information is not correct ]")

def sendMessage(database, user, ui_send_message, widget_send_message):
    # show sender's name
    ui_send_message.showStudentName(user)
    # show all the messages that current student got
    ui_send_message.showReceiverStudents(user, database)
    widget_send_message.show()

def checkEncryptAndSignMessage(database, ui_send_message, widget_send_message):
    # take what student has typed
    sender, receiver, og_message = ui_send_message.getUserInputForPlainText()
    # only send a message when the message is not null 
    if og_message != "":
        # encrypt message
        encryptedMessage = encrypt_message(database, receiver, og_message)

        # take student's private key and message
        privKey, _ = ui_send_message.getSenderPrivateKeyAndMessage()
        if privKey != None:
            # sign message
            signedEncryptedMessage = sign_encrypted_message(database, privKey, encryptedMessage)
            # signedMessage = sign_message(database, privKey, encryptedMessage)
            
            time = currentTime()

            # save the message into DB as plain text
            database.insertMessage(sender, receiver, time, "ENCRYPTED_AND_SIGNED", None, encryptedMessage, None, signedEncryptedMessage)
            widget_send_message.close()
            ui_send_message.clear()
    else:
        print("[ Message must not be null ]")
        
def checkEncryptMessage(database, ui_send_message, widget_send_message):
    # take what student has typed
    sender, receiver, message = ui_send_message.getUserInputForPlainText()
    # only send a message when the message is not null 
    if message != "":
        # encrypt message
        encryptedMessage = encrypt_message(database, receiver, message)

        time = currentTime()

        # save the message into DB as encrypted text
        database.insertMessage(sender, receiver, time, "ENCRYPTED", None, encryptedMessage, None, None)
        widget_send_message.close()
        ui_send_message.clear()
    else:
        print("[ Message must not be null ]")

def getSenderPrivateKey(database, ui_send_message, widget_send_message):
    # take what student has typed
    sender, receiver, message = ui_send_message.getUserInputForPlainText()
    # take student's private key and message
    privKey, message = ui_send_message.getSenderPrivateKeyAndMessage()
    # only sign the message when student chooses valid private key
    if privKey != None:
        # sign message
        signedMessage = sign_message(database, privKey, message)
        
        time = currentTime()  

        # save the message into DB as signed text
        database.insertMessage(sender, receiver, time, "SIGNED", message, None, signedMessage, None)
        widget_send_message.close()
        ui_send_message.clear()

def validateSignedMessage(database, ui_message):
    # take what student has typed
    sender, messageType, ogMessage, encryptedMessage, signedMessage, signedEncryptedMessage = ui_message.getSignedMessage()
    if messageType == "ENCRYPTED_AND_SIGNED":
        result = verify_encryptedMessage(database, sender, signedEncryptedMessage, encryptedMessage)
    else:
        # verify the signed message and take the result
        result = verify_message(database, sender, signedMessage, ogMessage)
    # show the vefirication result
    ui_message.showVerificationResult(result)

def sendFile(database, user, ui_send_file, widget_send_file):
    # show sender's name
    ui_send_file.showStudentName(user)
    # show all the messages that current student got
    ui_send_file.showReceiverStudents(user, database)
    widget_send_file.show()

def checkEncryptFile(database, ui_send_file, widget_send_file):
    # take what student has typed
    sender, receiver, filepath = ui_send_file.getUserInput()
    filepathArray = filepath.split("/")
    filename = filepathArray[-1]

    # encrypt file
    encryptedFile = encrypt_file(database, receiver, filepath)

    time = currentTime()
    
    # save the file into DB as encrypted file
    database.insertFile(sender, receiver, time, "ENCRYPTED", None, encryptedFile, None, None, filename)
    widget_send_file.close()
    ui_send_file.clear()

def checkSignFile(database, ui_send_file, widget_send_file):
    # take what student has typed
    sender, receiver, filepath = ui_send_file.getUserInput()
    filepathArray = filepath.split("/")
    filename = filepathArray[-1]

    privKey = ui_send_file.getSenderPrivateKey()

    # original file
    originalFile = open_original_file(filepath)

    # sign file
    signedFile = sign_file(privKey, filepath)

    time = currentTime()
    
    # save the file into DB as signed file
    database.insertFile(sender, receiver, time, "SIGNED", originalFile, None, signedFile, None, filename)
    widget_send_file.close()
    ui_send_file.clear()

def verifySignedFile(database, ui_file, widget_file):
    # get all the information
    sender, fileType, ogFile, encryptedFile, signedFile, signedEncryptedFile = ui_file.getSignedFile()
    if fileType == "ENCRYPTED_AND_SIGNED":
        result = verify_encryptedFile(database, sender, encryptedFile, signedEncryptedFile)
    else:
        result = verify_file(database, sender, ogFile, signedFile)

    # show the result
    ui_file.showVerificationResult(result)

def checkEncryptAndSignFile(database, ui_send_file, widget_send_file):
    # take what student has typed
    sender, receiver, filepath = ui_send_file.getUserInput()
    filepathArray = filepath.split("/")
    filename = filepathArray[-1]

    # encrypt file
    encryptedFile = encrypt_file(database, receiver, filepath)

    time = currentTime()

    privKey = ui_send_file.getSenderPrivateKey()

    # sign encrypted file
    signedEncryptedFile = sign_encrypted_File(database, privKey, encryptedFile)
    
    # save the file into DB as signed file
    database.insertFile(sender, receiver, time, "ENCRYPTED_AND_SIGNED", None, encryptedFile, None, signedEncryptedFile, filename)
    widget_send_file.close()
    ui_send_file.clear()