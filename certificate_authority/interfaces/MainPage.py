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
        self.WelcomeMessage.setGeometry(QtCore.QRect(150, 50, 210, 51))
        font.setPointSize(30)
        self.WelcomeMessage.setFont(font)
        self.WelcomeMessage.setObjectName("WelcomeMessage")
        self.StudentName = QtWidgets.QLabel(MainPage)
        self.StudentName.setGeometry(QtCore.QRect(380, 50, 130, 51))
        self.StudentName.setFont(font)
        self.StudentName.setObjectName("StudentName")
        self.LinkBtnMessageBoard = QtWidgets.QCommandLinkButton(MainPage)
        self.LinkBtnMessageBoard.setGeometry(QtCore.QRect(40, 280, 250, 61))
        font.setPointSize(20)
        self.LinkBtnMessageBoard.setFont(font)
        self.LinkBtnMessageBoard.setObjectName("LinkBtnMessageBoard")
        self.DownloadKeyButton = QtWidgets.QCommandLinkButton(MainPage)
        self.DownloadKeyButton.setGeometry(QtCore.QRect(190, 200, 280, 61))
        self.DownloadKeyButton.setFont(font)
        self.DownloadKeyButton.setObjectName("DownloadKeyButton")
        self.SendMessageButton = QtWidgets.QCommandLinkButton(MainPage)
        self.SendMessageButton.setGeometry(QtCore.QRect(40, 360, 250, 61))
        self.SendMessageButton.setFont(font)
        self.SendMessageButton.setObjectName("SendMessageButton")
        self.LogOutButton = QtWidgets.QPushButton(MainPage)
        self.LogOutButton.setGeometry(QtCore.QRect(190, 510, 330, 61))
        self.LogOutButton.setFont(font)
        self.LogOutButton.setObjectName("LogOutButton")
        self.LogOutButton.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 85, 255);")
        self.CheckFilesButton = QtWidgets.QCommandLinkButton(MainPage)
        self.CheckFilesButton.setGeometry(QtCore.QRect(420, 280, 190, 61))
        self.CheckFilesButton.setFont(font)
        self.CheckFilesButton.setObjectName("CheckFilesButton")
        self.SendFileButton = QtWidgets.QCommandLinkButton(MainPage)
        self.SendFileButton.setGeometry(QtCore.QRect(420, 360, 190, 61))
        self.SendFileButton.setFont(font)
        self.SendFileButton.setObjectName("SendFileButton")

        self.retranslateUi(MainPage)
        QtCore.QMetaObject.connectSlotsByName(MainPage)

    def retranslateUi(self, MainPage):
        _translate = QtCore.QCoreApplication.translate
        MainPage.setWindowTitle(_translate("MainPage", "Main page"))
        self.WelcomeMessage.setText(_translate("MainPage", "Welcome"))
        self.StudentName.setText(_translate("MainPage", "Name"))
        self.LinkBtnMessageBoard.setText(_translate("MainPage", "Check messages"))
        self.DownloadKeyButton.setText(_translate("MainPage", "Download key pairs"))
        self.SendMessageButton.setText(_translate("MainPage", "Send a message"))
        self.LogOutButton.setText(_translate("MainPage", "Log out"))
        self.CheckFilesButton.setText(_translate("MainPage", "Check files"))
        self.SendFileButton.setText(_translate("MainPage", "Send a file"))

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

    def logout(self, user, widget_MainPage, widget_login):
        user = None
        widget_MainPage.close()
        widget_login.show()
