# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainPage(object):
    def setupUi(self, MainPage):
        MainPage.setObjectName("MainPage")
        MainPage.resize(687, 592)
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainPage.setFont(font)
        self.WelcomeMessage = QtWidgets.QLabel(MainPage)
        self.WelcomeMessage.setGeometry(QtCore.QRect(140, 100, 210, 51))
        font.setPointSize(30)
        self.WelcomeMessage.setFont(font)
        self.WelcomeMessage.setObjectName("WelcomeMessage")
        self.StudentName = QtWidgets.QLabel(MainPage)
        self.StudentName.setGeometry(QtCore.QRect(395, 100, 130, 51))
        self.StudentName.setFont(font)
        self.StudentName.setObjectName("StudentName")
        self.LinkBtnMessageBoard = QtWidgets.QCommandLinkButton(MainPage)
        self.LinkBtnMessageBoard.setGeometry(QtCore.QRect(190, 300, 311, 61))
        font.setPointSize(20)
        self.LinkBtnMessageBoard.setFont(font)
        self.LinkBtnMessageBoard.setObjectName("LinkBtnMessageBoard")
        self.LinkBtnKeyPairs = QtWidgets.QCommandLinkButton(MainPage)
        self.LinkBtnKeyPairs.setGeometry(QtCore.QRect(190, 370, 311, 61))
        self.LinkBtnKeyPairs.setFont(font)
        self.LinkBtnKeyPairs.setObjectName("LinkBtnKeyPairs")

        self.retranslateUi(MainPage)
        QtCore.QMetaObject.connectSlotsByName(MainPage)

    def retranslateUi(self, MainPage):
        _translate = QtCore.QCoreApplication.translate
        MainPage.setWindowTitle(_translate("MainPage", "Form"))
        self.WelcomeMessage.setText(_translate("MainPage", "Welcome"))
        self.StudentName.setText(_translate("MainPage", "Name"))
        self.LinkBtnMessageBoard.setText(_translate("MainPage", "Message  board"))
        self.LinkBtnKeyPairs.setText(_translate("MainPage", "Key pairs"))


    def showStudentName(self, user):
        self.StudentName.setText(user.getStudentName() + '!')
