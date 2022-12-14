# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MessageBoard.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir, QTimer
from PyQt5.QtWidgets import QApplication, QInputDialog, QFileDialog
from scripts.crypto import *

class Ui_MessageBoard(object):
    def setupUi(self, MessageBoard):
        MessageBoard.setObjectName("MessageBoard")
        MessageBoard.resize(858, 838)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        MessageBoard.setFont(font)
        self.label = QtWidgets.QLabel(MessageBoard)
        self.label.setGeometry(QtCore.QRect(220, 10, 451, 71))
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        font.setPointSize(16)
        self.scrollArea_2 = QtWidgets.QScrollArea(MessageBoard)
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
        self.SenderLabel = QtWidgets.QLabel(MessageBoard)
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
        self.Message = QtWidgets.QPlainTextEdit(MessageBoard)
        self.Message.setGeometry(QtCore.QRect(230, 640, 401, 101))
        font.setPointSize(15)
        self.Message.setFont(font)
        self.Message.setObjectName("Message")
        self.labelMessage = QtWidgets.QLabel(MessageBoard)
        self.labelMessage.setGeometry(QtCore.QRect(380, 580, 111, 51))
        self.labelMessage.setFont(font)
        self.labelMessage.setObjectName("labelMessage")
        self.decryptButton = QtWidgets.QPushButton(MessageBoard)
        self.decryptButton.setGeometry(QtCore.QRect(180, 520, 171, 51))
        self.decryptButton.setFont(font)
        self.decryptButton.setObjectName("decryptButton")
        self.validateButton = QtWidgets.QPushButton(MessageBoard)
        self.validateButton.setGeometry(QtCore.QRect(500, 520, 171, 51))
        self.validateButton.setFont(font)
        self.validateButton.setObjectName("validateButton")
        self.privateKeyLabel = QtWidgets.QLabel(MessageBoard)
        self.privateKeyLabel.setGeometry(QtCore.QRect(55, 370, 400, 61))
        self.privateKeyLabel.setFont(font)
        self.privateKeyLabel.setObjectName("privateKeyLabel")
        self.privateKeyLabel.setStyleSheet("color: rgb(0, 0, 255);")
        self.privateKeyPath = QtWidgets.QPlainTextEdit(MessageBoard)
        self.privateKeyPath.setGeometry(QtCore.QRect(55, 430, 400, 60))
        self.privateKeyPath.setFont(font)
        self.privateKeyPath.setObjectName("privateKeyPath")
        self.validationLabel = QtWidgets.QLabel(MessageBoard)
        self.validationLabel.setGeometry(QtCore.QRect(570, 390, 200, 61))
        self.validationLabel.setFont(font)
        self.validationLabel.setObjectName("validationLabel")
        
        self.listWidget.itemDoubleClicked.connect(self.showSelectedMessage)
        self.receivedMessages = []
        self.retranslateUi(MessageBoard)
        QtCore.QMetaObject.connectSlotsByName(MessageBoard)

    def retranslateUi(self, MessageBoard):
        _translate = QtCore.QCoreApplication.translate
        MessageBoard.setWindowTitle(_translate("MessageBoard", "Message board page"))
        self.label.setText(_translate("MessageBoard", "Received messages"))
        self.labelMessage.setText(_translate("MessageBoard", "Message"))
        self.decryptButton.setText(_translate("MessageBoard", "Decrypt"))
        self.validateButton.setText(_translate("MessageBoard", "Validate"))
        self.privateKeyLabel.setText(_translate("MessageBoard", "Type Your private key path for decryption"))
        self.validationLabel.setText(_translate("MessageBoard", ""))
        self.NumberLabel.setText(_translate("MessageBoard", "#"))
        self.SenderLabel.setText(_translate("MessageBoard", "Sender"))
        self.TimeLabel.setText(_translate("MessageBoard", "Time"))
        self.MessageTypeLabel.setText(_translate("MessageBoard", "Message type"))
        
    def showReceivedMessages(self, database, user):
        self.database = database
        self.user = user
        self.refreshTimer()
        self.listWidget.clear()
        self.Message.clear()
        self.privateKeyPath.clear()
        if user.getPrivateKeyPath() != '':
            self.privateKeyPath.clear()
            self.privateKeyPath.insertPlainText(user.getPrivateKeyPath())
        self.privateKeyLabel.setHidden(True)
        self.decryptButton.setEnabled(False)
        self.validateButton.setEnabled(False)
        self.privateKeyPath.setDisabled(True)
        messages = database.getReceivedMessages(user.getStudentName())
        startNum = 1
        self.receivedMessages = messages

        for message in messages:
            messageType = message[3].lower()
            number = "[" + str(startNum) + "]"
            title = number.ljust(5, ' ') + message[0].ljust(14, ' ') + message[2] + "    " + messageType
            self.listWidget.addItem(title)
            startNum += 1
    
    def showSelectedMessage(self, item):
        self.Message.clear()
        self.validationLabel.setText("")
        self.privateKeyPath.setDisabled(True)
        messageList = (item.text()).split(' ')

        date = ''
        time = ''
        for message in messageList:
            if len(message) == 10 and message.startswith("2"):
                date = message
            if len(message) == 8 and ":" in message:
                time = message

        selectedMessage = None
        for message in self.receivedMessages:
            if message[2] == date + " " + time:
                selectedMessage = message
                break

        if selectedMessage[3] == 'ENCRYPTED_AND_SIGNED':
            self.decryptButton.setEnabled(True)
            self.privateKeyLabel.setHidden(False)
            self.validateButton.setEnabled(True)
            self.privateKeyPath.setDisabled(False)
        elif selectedMessage[3] == 'ENCRYPTED':
            self.privateKeyLabel.setHidden(False)
            self.decryptButton.setEnabled(True)
            self.validateButton.setEnabled(False)
            self.privateKeyPath.setDisabled(False)
        elif selectedMessage[3] == 'SIGNED':
            self.privateKeyLabel.setHidden(True)
            self.decryptButton.setEnabled(False)
            self.validateButton.setEnabled(True)
            self.privateKeyPath.setDisabled(True)
            self.showPlainMessage(selectedMessage[4])

    def showPlainMessage(self, message):
        self.Message.clear()
        self.Message.insertPlainText(message)
    
    def uploadPrivateKey(self, database, user):
        # file_name = QFileDialog.getOpenFileName()
        path = self.privateKeyPath.toPlainText()
        
        if user.getPrivateKeyPath() == '':
            user.privateKeyPath = path

        messageList = (self.listWidget.currentItem().text()).split(' ')

        date = ''
        time = ''
        for message in messageList:
            if len(message) == 10 and message.startswith("2"):
                date = message
            if len(message) == 8 and ":" in message:
                time = message

        selectedMessage = None
        for message in self.receivedMessages:
            if message[2] == date + " " + time:
                selectedMessage = message
                break

        decryptMessage = decrypt_message(path, selectedMessage[5])
        self.showPlainMessage(decryptMessage)
    
    def getSignedMessage(self):
        messageList = (self.listWidget.currentItem().text()).split(' ')

        date = ''
        time = ''
        for message in messageList:
            if len(message) == 10 and message.startswith("2"):
                date = message
            if len(message) == 8 and ":" in message:
                time = message

        selectedMessage = None
        for message in self.receivedMessages:
            if message[2] == date + " " + time:
                selectedMessage = message
                break

        sender = selectedMessage[0]
        messageType = selectedMessage[3]
        ogMessage = selectedMessage[4]
        encryptedMessage = selectedMessage[5]
        signedMessage = selectedMessage[6]
        signedEncryptedMessage = selectedMessage[7]
        return sender, messageType, ogMessage, encryptedMessage, signedMessage, signedEncryptedMessage

    def showVerificationResult(self, result):
        self.Message.clear()
        if result:
            self.Message.insertPlainText("True")
        else:
            self.Message.insertPlainText("False")

    def refreshTimer(self):
        # Repeating timer, calls random_pick over and over.
        self.picktimer = QTimer()
        self.picktimer.setInterval(500)
        self.picktimer.timeout.connect(self.updateMessages)
        self.picktimer.start()

    def updateMessages(self):
        messages = self.database.getReceivedMessages(self.user.getStudentName())
        if len(messages) != len(self.receivedMessages):
            self.showReceivedMessages(self.database, self.user)

    def privateKeyPathclear(self):
        self.privateKeyPath.clear()