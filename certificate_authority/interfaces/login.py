# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(593, 474)
        font = QtGui.QFont()
        font.setFamily("Arial")
        Login.setFont(font)
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(250, 20, 111, 81))
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 111, 31))
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Login)
        self.label_3.setGeometry(QtCore.QRect(60, 210, 111, 31))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textStudentName = QtWidgets.QTextEdit(Login)
        self.textStudentName.setGeometry(QtCore.QRect(60, 150, 471, 51))
        font.setPointSize(20)
        self.textStudentName.setFont(font)
        self.textStudentName.setObjectName("textStudentName")
        self.textPassword = QtWidgets.QTextEdit(Login)
        self.textPassword.setGeometry(QtCore.QRect(60, 250, 471, 51))
        self.textPassword.setFont(font)
        self.textPassword.setObjectName("textPassword")
        self.LoginButton = QtWidgets.QPushButton(Login)
        self.LoginButton.setGeometry(QtCore.QRect(60, 340, 471, 51))
        font.setPointSize(14)
        self.LoginButton.setFont(font)
        self.LoginButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);")
        self.LoginButton.setObjectName("LoginButton")
        self.label_4 = QtWidgets.QLabel(Login)
        self.label_4.setGeometry(QtCore.QRect(160, 420, 191, 41))
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.LinkBtnRegister = QtWidgets.QCommandLinkButton(Login)
        self.LinkBtnRegister.setEnabled(True)
        self.LinkBtnRegister.setGeometry(QtCore.QRect(360, 420, 185, 41))
        self.LinkBtnRegister.setFont(font)
        self.LinkBtnRegister.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LinkBtnRegister.setObjectName("LinkBtnRegister")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.label.setText(_translate("Login", "Login"))
        self.label_2.setText(_translate("Login", "Student ID"))
        self.label_3.setText(_translate("Login", "Password"))
        self.LoginButton.setText(_translate("Login", "Login"))
        self.label_4.setText(_translate("Login", "Don\'t have an account? "))
        self.LinkBtnRegister.setText(_translate("Login", "Register"))

    
    def returnStudentInfo(self):
        return self.textStudentName.toPlainText(), self.textPassword.toPlainText()

    def reset(self):
        self.textStudentName.setText("")
        self.textPassword.setText("")
