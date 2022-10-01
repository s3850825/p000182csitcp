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
        self.WelcomeMessage.setGeometry(QtCore.QRect(150, 100, 210, 51))
        font.setPointSize(30)
        self.WelcomeMessage.setFont(font)
        self.WelcomeMessage.setObjectName("WelcomeMessage")
        self.StudentName = QtWidgets.QLabel(MainPage)
        self.StudentName.setGeometry(QtCore.QRect(380, 100, 130, 51))
        self.StudentName.setFont(font)
        self.StudentName.setObjectName("StudentName")
        self.LinkBtnMessageBoard = QtWidgets.QCommandLinkButton(MainPage)
        self.LinkBtnMessageBoard.setGeometry(QtCore.QRect(190, 300, 311, 61))
        font.setPointSize(20)
        self.LinkBtnMessageBoard.setFont(font)
        self.LinkBtnMessageBoard.setObjectName("LinkBtnMessageBoard")
        self.DownloadKeyButton = QtWidgets.QCommandLinkButton(MainPage)
        self.DownloadKeyButton.setGeometry(QtCore.QRect(190, 380, 370, 61))
        self.DownloadKeyButton.setFont(font)
        self.DownloadKeyButton.setObjectName("DownloadKeyButton")

        self.retranslateUi(MainPage)
        QtCore.QMetaObject.connectSlotsByName(MainPage)

    def retranslateUi(self, MainPage):
        _translate = QtCore.QCoreApplication.translate
        MainPage.setWindowTitle(_translate("MainPage", "Form"))
        self.WelcomeMessage.setText(_translate("MainPage", "Welcome"))
        self.StudentName.setText(_translate("MainPage", "Name"))
        self.LinkBtnMessageBoard.setText(_translate("MainPage", "Message  board"))
        self.DownloadKeyButton.setText(_translate("MainPage", "Download key pairs"))


    def showStudentName(self, user):
        self.StudentName.setText(user.getStudentName() + '!')

    def downloadKeyPairs(self, database, user):
        studentName = user.getStudentName()
        privKey = user.getPrivateKey()
        pubKey = user.getPublicKey()
        #save PEM key into the file
        with open(studentName + '_2_private.pem', 'wb') as file:
            file.write(privKey)

        with open(studentName + '_2_public.pem', 'wb') as file:
            file.write(pubKey)
        
        print("[ Keypairs are downloaded ]")