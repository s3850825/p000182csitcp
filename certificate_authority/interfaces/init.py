import sys
from PyQt5.QtWidgets import QApplication, QWidget
from interfaces.login import *
from interfaces.sign_up import *
from interfaces.MainPage import *
from interfaces.MessageBoard import *

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
    jpg = QtGui.QPixmap(imgName).scaled(ui_mainPage.labelFace.width(), ui_mainPage.labelFace.height())
    ui_mainPage.labelFace.setPixmap(jpg)

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
            widget_login.close(),
            
            # login check

            widget_MainPage.show()
        }
    )
    ui_sign.btnSignUp.clicked.connect(
        lambda: {
            widget_sign.close(),
            print('register!')
        }
    )
    sys.exit(app.exec_())

