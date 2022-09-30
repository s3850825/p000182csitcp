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

    # connect to DB
    database = Database()

    # Logged in user
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

def checkPlainMessage(database, ui_send_message, widget_send_message):
    # take what student has typed
    sender, receiver, message = ui_send_message.getUserInputForPlainText()
    # only send a message when the message is not null 
    if message != "":
        # save the message into DB as plain text
        database.insertMessage(sender, receiver, message, None, "PLAIN")
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
        # save the message into DB as encrypted text
        database.insertMessage(sender, receiver, encryptedMessage, None, "ENCRYPT")
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
        # save the message into DB as signed text
        database.insertMessage(sender, receiver, signedMessage, message, "SIGN")
        widget_send_message.close()
        ui_send_message.clear()

def validateSignedMessage(database, ui_message):
    # take what student has typed
    sender, signedMessage, og_message = ui_message.getSignedMessage()
    # verify the signed message and take the result
    result = verify_message(database, sender, signedMessage, og_message)
    # show the vefirication result
    ui_message.showVerificationResult(result)