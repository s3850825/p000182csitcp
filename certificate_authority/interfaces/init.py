import sys
from PyQt5.QtWidgets import QApplication, QWidget
from interfaces.login import *
from interfaces.sign_up import *
from interfaces.MainPage import *
from interfaces.MessageBoard import *
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
    imgName = './American.png'
    jpg = QtGui.QPixmap(imgName).scaled(ui_mainPage.labelStudentFace.width(), ui_mainPage.labelStudentFace.height())
    ui_mainPage.labelStudentFace.setPixmap(jpg)

    widget_sign = QWidget()
    ui_sign = Ui_Sign_Up()
    ui_sign.setupUi(widget_sign)

    widget_message = QWidget()
    ui_message = Ui_MessageBoard()
    ui_message.setupUi(widget_message)

    imgName_1 = './American.png'
    imgName_2 = './homelander.png'
    jpg_1 = QtGui.QPixmap(imgName_1).scaled(ui_message.labelFace1.width(), ui_message.labelFace1.height())
    jpg_2 = QtGui.QPixmap(imgName_2).scaled(ui_message.labelFace2.width(), ui_message.labelFace2.height())
    ui_message.labelFace1.setPixmap(jpg_1)
    ui_message.labelFace2.setPixmap(jpg_2)
    ui_message.labelFace3.setPixmap(jpg_1)
    ui_message.labelFace4.setPixmap(jpg_2)

    # connect to DB
    database = Database()

    ui_mainPage.LinkBtnMessageBoard.clicked.connect(
        lambda: {
            widget_message.show()
        }
    )
    ui.LinkBtnRegister.clicked.connect(
        lambda: {
            widget_sign.show()
        }
    )
    ui.btnLogin.clicked.connect(
        lambda: {
            checkLoginInfo(database, ui.returnStudentInfo(), ui, widget_login, widget_MainPage)
        }
    )
    ui_sign.btnSignUp.clicked.connect(
        lambda: {
            checkStudentInfo(database, ui_sign.returnStudentInfo(), ui_sign, widget_sign),
        }
    )
    sys.exit(app.exec_())

def checkStudentInfo(database, studentInfo, ui_sign, widget_sign):
    studentName, studentPassword, studentPassword2, studentWalletPassword = studentInfo
    if database.checkUniqueStudentName(studentInfo[0]) and studentPassword == studentPassword2:
        database.insertNewStudent(studentName, studentPassword, studentWalletPassword)
        widget_sign.close()
        print(studentInfo, 'registered!')
        
        # We need to generate key pairs for the user and then save into DB
        privKey, pubKey = generate_RSA_key_pairs()
        database.updateNewStudentKeyPairs(privKey, pubKey, studentName)
    else:
        ui_sign.reset()
        print(studentInfo[0], " cannot be registered")

def checkLoginInfo(database, studentInfo, ui, widget_login, widget_MainPage):
    studentName, studentPassword = studentInfo
    if database.checkStudentInfo(studentInfo[0], studentInfo[1]):
        widget_login.close()
        widget_MainPage.show()
    else:
        ui.reset()
        print("Log in information is not correct")

