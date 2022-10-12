# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FileBoard.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir, QTimer
from PyQt5.QtWidgets import QApplication, QInputDialog, QFileDialog
from scripts.crypto import *
import os

class Ui_FileBoard(object):
    def setupUi(self, FileBoard):
        FileBoard.setObjectName("FileBoard")
        FileBoard.resize(858, 800)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        FileBoard.setFont(font)
        self.label = QtWidgets.QLabel(FileBoard)
        self.label.setGeometry(QtCore.QRect(300, 10, 451, 71))
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        font.setPointSize(16)
        self.scrollArea_2 = QtWidgets.QScrollArea(FileBoard)
        self.scrollArea_2.setGeometry(QtCore.QRect(20, 80, 811, 291))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 809, 259))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        font.setPointSize(16)
        self.NumberLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.NumberLabel.setGeometry(QtCore.QRect(56, 20, 64, 15))
        self.NumberLabel.setFont(font)
        self.NumberLabel.setObjectName("NumberLabel")
        self.SenderLabel = QtWidgets.QLabel(FileBoard)
        self.SenderLabel.setGeometry(QtCore.QRect(110, 100, 68, 15))
        self.SenderLabel.setFont(font)
        self.SenderLabel.setObjectName("SenderLabel")
        self.TimeLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.TimeLabel.setGeometry(QtCore.QRect(200, 20, 64, 15))
        self.TimeLabel.setFont(font)
        self.TimeLabel.setObjectName("TimeLabel")
        self.MessageTypeLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.MessageTypeLabel.setGeometry(QtCore.QRect(430, 10, 150, 31))
        self.MessageTypeLabel.setFont(font)
        self.MessageTypeLabel.setObjectName("MessageTypeLabel")
        font.setPointSize(16)
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        self.listWidget.setGeometry(QtCore.QRect(50, 50, 701, 221))
        font.setPointSize(16)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        font.setPointSize(15)
        self.decryptButton = QtWidgets.QPushButton(FileBoard)
        self.decryptButton.setGeometry(QtCore.QRect(180, 520, 171, 51))
        self.decryptButton.setFont(font)
        self.decryptButton.setObjectName("decryptButton")
        self.validateButton = QtWidgets.QPushButton(FileBoard)
        self.validateButton.setGeometry(QtCore.QRect(500, 520, 171, 51))
        self.validateButton.setFont(font)
        self.validateButton.setObjectName("validateButton")
        self.privateKeyLabel = QtWidgets.QLabel(FileBoard)
        self.privateKeyLabel.setGeometry(QtCore.QRect(55, 370, 400, 61))
        self.privateKeyLabel.setFont(font)
        self.privateKeyLabel.setObjectName("privateKeyLabel")
        self.privateKeyLabel.setStyleSheet("color: rgb(0, 0, 255);")
        self.privateKeyPath = QtWidgets.QPlainTextEdit(FileBoard)
        self.privateKeyPath.setGeometry(QtCore.QRect(55, 430, 400, 60))
        self.privateKeyPath.setFont(font)
        self.privateKeyPath.setObjectName("privateKeyPath")
        self.validationLabel = QtWidgets.QLabel(FileBoard)
        self.validationLabel.setGeometry(QtCore.QRect(570, 390, 200, 61))
        self.validationLabel.setFont(font)
        self.validationLabel.setObjectName("validationLabel")
        
        self.listWidget.itemDoubleClicked.connect(self.showSelectedFile)
        self.receivedFiles = []
        self.retranslateUi(FileBoard)
        QtCore.QMetaObject.connectSlotsByName(FileBoard)

    def retranslateUi(self, FileBoard):
        _translate = QtCore.QCoreApplication.translate
        FileBoard.setWindowTitle(_translate("FileBoard", "File board page"))
        self.label.setText(_translate("FileBoard", "Received files"))
        self.decryptButton.setText(_translate("FileBoard", "Decrypt"))
        self.validateButton.setText(_translate("FileBoard", "Validate"))
        self.privateKeyLabel.setText(_translate("FileBoard", "Type Your private key path for decryption"))
        self.validationLabel.setText(_translate("FileBoard", ""))
        self.NumberLabel.setText(_translate("FileBoard", "#"))
        self.SenderLabel.setText(_translate("FileBoard", "Sender"))
        self.TimeLabel.setText(_translate("FileBoard", "Time"))
        self.MessageTypeLabel.setText(_translate("FileBoard", "File type"))
        
    def showReceivedFiles(self, database, user):
        self.database = database
        self.user = user
        self.refreshTimer()
        self.listWidget.clear()
        self.privateKeyLabel.setHidden(True)
        self.decryptButton.setEnabled(False)
        self.validateButton.setEnabled(False)
        self.privateKeyPath.setDisabled(True)
        files = database.getReceivedFiles(user.getStudentName())
        startNum = 1
        self.receivedFiles = files

        for aFile in files:
            fileType = aFile[3].lower()
            number = "[" + str(startNum) + "]"
            title = number.ljust(5, ' ') + aFile[0].ljust(14, ' ') + aFile[2] + "    " + fileType
            self.listWidget.addItem(title)
            startNum += 1
    
    def showSelectedFile(self, item):
        self.validationLabel.setText("")
        self.privateKeyPath.setDisabled(True)
        fileList = (item.text()).split(' ')

        date = ''
        time = ''
        for aFile in fileList:
            if len(aFile) == 10 and aFile.startswith("2"):
                date = aFile
            if len(aFile) == 8 and ":" in aFile:
                time = aFile

        selectedaFile = None
        for aFile in self.receivedFiles:
            if aFile[2] == date + " " + time:
                selectedFile = aFile
                break

        if selectedFile[3] == 'ENCRYPTED_AND_SIGNED':
            self.decryptButton.setEnabled(True)
            self.privateKeyLabel.setHidden(False)
            self.validateButton.setEnabled(True)
            self.privateKeyPath.setDisabled(False)
        elif selectedFile[3] == 'ENCRYPTED':
            self.privateKeyLabel.setHidden(False)
            self.decryptButton.setEnabled(True)
            self.validateButton.setEnabled(False)
            self.privateKeyPath.setDisabled(False)
        elif selectedFile[3] == 'SIGNED':
            self.privateKeyLabel.setHidden(True)
            self.decryptButton.setEnabled(False)
            self.validateButton.setEnabled(True)
            self.privateKeyPath.setDisabled(True)
            self.downloadOriginalFile(selectedFile[4], selectedFile[8])
    
    def uploadPrivateKey(self, database):
        path = self.privateKeyPath.toPlainText()

        fileList = (self.listWidget.currentItem().text()).split(' ')

        date = ''
        time = ''
        for aFile in fileList:
            if len(aFile) == 10 and aFile.startswith("2"):
                date = aFile
            if len(aFile) == 8 and ":" in aFile:
                time = aFile

        selectedFile = None
        for aFile in self.receivedFiles:
            if aFile[2] == date + " " + time:
                selectedFile = aFile
                break
                
        decrypt_file(path, selectedFile[5], selectedFile[8])
    
    def getSignedFile(self):
        fileList = (self.listWidget.currentItem().text()).split(' ')

        date = ''
        time = ''
        for aFile in fileList:
            if len(aFile) == 10 and aFile.startswith("2"):
                date = aFile
            if len(aFile) == 8 and ":" in aFile:
                time = aFile

        selectedFile = None
        for aFile in self.receivedFiles:
            if aFile[2] == date + " " + time:
                selectedFile = aFile
                break

        sender = selectedFile[0]
        fileType = selectedFile[3]
        ogFile = selectedFile[4]
        encryptedFile = selectedFile[5]
        signedFile = selectedFile[6]
        signedEncryptedFile = selectedFile[7]
        return sender, fileType, ogFile, encryptedFile, signedFile, signedEncryptedFile

    def showVerificationResult(self, result):
        if result:
            self.validationLabel.setText("True")
        else:
            self.validationLabel.setText("False")

    def refreshTimer(self):
        # Repeating timer, calls random_pick over and over.
        self.picktimer = QTimer()
        self.picktimer.setInterval(500)
        self.picktimer.timeout.connect(self.updateFiles)
        self.picktimer.start()

    def updateFiles(self):
        files = self.database.getReceivedFiles(self.user.getStudentName())
        if len(files) != len(self.receivedFiles):
            self.showReceivedFiles(self.database, self.user)

    def privateKeyPathclear(self):
        self.privateKeyPath.clear()

    def downloadOriginalFile(self, originalBinary, filename):
        filepath = os.getcwd() + "\\" + filename

        with open(filepath, 'wb') as file:
            file.write(originalBinary)
