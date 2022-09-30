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
from scripts.crypto import *
from scripts.deploy import *
from db.database import *
from scripts.keyGeneration import *

def frontend_UI():
    app = QApplication([])
    widget_login = QWidget()
    ui = Ui_Login()
    ui.setupUi(widget_login)
    widget_login.show()

    ui_mainPage = Ui_MainPage()
    widget_MainPage = QWidget()
    ui_mainPage.setupUi(widget_MainPage)

    ui_keyPairsPage = Ui_KeyPairs()
    widget_keyPairs = QWidget()
    ui_keyPairsPage.setupUi(widget_keyPairs)

    widget_sign = QWidget()
    ui_sign = Ui_Sign_Up()
    ui_sign.setupUi(widget_sign)

    widget_message = QWidget()
    ui_message = Ui_MessageBoard()
    ui_message.setupUi(widget_message)

    widget_send_message = QWidget()
    ui_send_message = Ui_Send_Message()
    ui_send_message.setupUi(widget_send_message)

    # connect to DB
    database = Database()
    user = User()

    # Message board button event
    ui_mainPage.LinkBtnMessageBoard.clicked.connect(
        lambda: {
            ui_message.showReceivedMessages(database, user),
            widget_message.show()
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
    ui_message.SendMessageButton.clicked.connect(
        lambda: {
            sendMessage(database, user, ui_send_message, widget_send_message)
        }
    )
    # Plain text button event
    ui_send_message.PlainButton.clicked.connect(
        lambda: {
            checkPlainMessage(database, ui_send_message, widget_send_message)
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

    sys.exit(app.exec_())

def checkStudentInfo(database, studentInfo, ui_sign, widget_sign):
    studentName, studentPassword, studentPassword2, studentWalletPassword = studentInfo
    if database.checkUniqueStudentName(studentInfo[0]) and studentPassword == studentPassword2:
        database.insertNewStudent(studentName, studentPassword, studentWalletPassword)
        
        ui_sign.reset()
        widget_sign.close()
        print("[", studentName, 'is registered! ]')
        
        # We need to generate key pairs for the user and then save into DB
        privKey, pubKey = generate_RSA_key_pairs(studentName)
        database.updateNewStudentKeyPairs(privKey, pubKey, studentName)

        # Blockchain
        deploy_certification(studentWalletPassword)
        create_certificate(studentName, pubKey, studentWalletPassword)
    else:
        ui_sign.reset()
        print("[", studentInfo[0], " is already registered ]")

def checkLoginInfo(database, studentInfo, ui, widget_login, widget_MainPage, user, ui_mainPage):
    studentName, studentPassword = studentInfo
    if database.checkStudentInfo(studentInfo[0], studentInfo[1]):
        ui.reset()
        # Once user logged in all the information is saved into user object 
        user.setStudentInfo(studentName, database)
        ui_mainPage.showStudentName(user)
        widget_login.close()
        widget_MainPage.show()
    else:
        ui.reset()
        print("[ Log in information is not correct ]")

def sendMessage(database, user, ui_send_message, widget_send_message):
    ui_send_message.showStudentName(user)
    ui_send_message.showReceiverStudents(user, database)
    widget_send_message.show()

def checkPlainMessage(database, ui_send_message, widget_send_message):
    sender, receiver, message = ui_send_message.getUserInputForPlainText()
    if message != "":
        database.insertMessage(sender, receiver, message, None, "PLAIN")
        widget_send_message.close()
        ui_send_message.clear()
    else:
        print("[ Message must not be null ]")
        
def checkEncryptMessage(database, ui_send_message, widget_send_message):
    sender, receiver, message = ui_send_message.getUserInputForPlainText()
    if message != "":
        # Encrypt message
        encryptedMessage = encrypt_message(database, receiver, message)
        database.insertMessage(sender, receiver, encryptedMessage, None, "ENCRYPT")
        widget_send_message.close()
        ui_send_message.clear()
    else:
        print("[ Message must not be null ]")

def getSenderPrivateKey(database, ui_send_message, widget_send_message):
    sender, receiver, message = ui_send_message.getUserInputForPlainText()
    privKey, message = ui_send_message.getSenderPrivateKeyAndMessage()
    signedMessage = sign_message(database, privKey, message)
    database.insertMessage(sender, receiver, signedMessage, message, "SIGN")
    widget_send_message.close()
    ui_send_message.clear()

def validateSignedMessage(database, ui_message):
    sender, signedMessage, og_message = ui_message.getSignedMessage()
    result = verify_message(database, sender, signedMessage, og_message)
    ui_message.showVerificationResult(result)