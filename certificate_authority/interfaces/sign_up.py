# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign_up.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sign_Up(object):
    def setupUi(self, Sign_Up):
        Sign_Up.setObjectName("Sign_Up")
        Sign_Up.resize(556, 656)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        Sign_Up.setFont(font)
        self.label = QtWidgets.QLabel(Sign_Up)
        self.label.setGeometry(QtCore.QRect(230, 20, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Sign_Up)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 101, 41))
        self.label_2.setObjectName("label_2")
        self.textStudentName = QtWidgets.QTextEdit(Sign_Up)
        self.textStudentName.setGeometry(QtCore.QRect(40, 140, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textStudentName.setFont(font)
        self.textStudentName.setObjectName("textStudentName")
        self.textPassword1 = QtWidgets.QTextEdit(Sign_Up)
        self.textPassword1.setGeometry(QtCore.QRect(40, 250, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textPassword1.setFont(font)
        self.textPassword1.setObjectName("textPassword1")
        self.label_3 = QtWidgets.QLabel(Sign_Up)
        self.label_3.setGeometry(QtCore.QRect(40, 210, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btnSignUp = QtWidgets.QPushButton(Sign_Up)
        self.btnSignUp.setGeometry(QtCore.QRect(40, 580, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.btnSignUp.setFont(font)
        self.btnSignUp.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);")
        self.btnSignUp.setObjectName("btnSignUp")
        self.label_4 = QtWidgets.QLabel(Sign_Up)
        self.label_4.setGeometry(QtCore.QRect(40, 320, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textPassword2 = QtWidgets.QTextEdit(Sign_Up)
        self.textPassword2.setGeometry(QtCore.QRect(40, 360, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textPassword2.setFont(font)
        self.textPassword2.setObjectName("textPassword2")
        self.label_5 = QtWidgets.QLabel(Sign_Up)
        self.label_5.setGeometry(QtCore.QRect(40, 430, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.walletPassword = QtWidgets.QTextEdit(Sign_Up)
        self.walletPassword.setGeometry(QtCore.QRect(40, 470, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.walletPassword.setFont(font)
        self.walletPassword.setObjectName("walletPassword")

        self.retranslateUi(Sign_Up)
        QtCore.QMetaObject.connectSlotsByName(Sign_Up)

    def retranslateUi(self, Sign_Up):
        _translate = QtCore.QCoreApplication.translate
        Sign_Up.setWindowTitle(_translate("Sign_Up", "Form"))
        self.label.setText(_translate("Sign_Up", "Sign Up"))
        self.label_2.setText(_translate("Sign_Up", "Student Name"))
        self.label_3.setText(_translate("Sign_Up", "Password"))
        self.btnSignUp.setText(_translate("Sign_Up", "Sign Up"))
        self.label_4.setText(_translate("Sign_Up", "Check password"))
        self.label_5.setText(_translate("Sign_Up", "User wallet private key"))

    def returnStudentInfo(self):
        return self.textStudentName.toPlainText(), self.textPassword1.toPlainText(), self.textPassword2.toPlainText(), self.walletPassword.toPlainText()
    
    def reset(self):
        self.textStudentName.setText("")
        self.textPassword1.setText("")
        self.textPassword2.setText("")
        self.walletPassword.setText("")