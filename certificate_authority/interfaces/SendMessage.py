# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SendMessage.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QApplication, QInputDialog, QFileDialog
from scripts.crypto import *

class Ui_Send_Message(object):
    def setupUi(self, SendMessage):
        SendMessage.setObjectName("SendMessage")
        SendMessage.resize(681, 743)
        self.PlainButton = QtWidgets.QCommandLinkButton(SendMessage)
        self.PlainButton.setGeometry(QtCore.QRect(270, 450, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.PlainButton.setFont(font)
        self.PlainButton.setObjectName("PlainButton")
        self.SendAMessage = QtWidgets.QLabel(SendMessage)
        self.SendAMessage.setGeometry(QtCore.QRect(180, 40, 451, 51))
        font.setPointSize(24)
        self.SendAMessage.setFont(font)
        self.SendAMessage.setObjectName("SendAMessage")
        self.textMessage = QtWidgets.QTextEdit(SendMessage)
        self.textMessage.setGeometry(QtCore.QRect(90, 240, 511, 201))
        font.setPointSize(16)
        self.textMessage.setFont(font)
        self.textMessage.setObjectName("textMessage")
        self.EncryptButton = QtWidgets.QCommandLinkButton(SendMessage)
        self.EncryptButton.setGeometry(QtCore.QRect(270, 500, 141, 51))
        self.EncryptButton.setFont(font)
        self.EncryptButton.setObjectName("EncryptButton")
        self.SignatureButton = QtWidgets.QCommandLinkButton(SendMessage)
        self.SignatureButton.setGeometry(QtCore.QRect(270, 670, 141, 51))
        self.SignatureButton.setFont(font)
        self.SignatureButton.setObjectName("SignatureButton")
        self.Sender = QtWidgets.QLabel(SendMessage)
        self.Sender.setGeometry(QtCore.QRect(180, 110, 91, 41))
        font.setPointSize(14)
        self.Sender.setFont(font)
        self.Sender.setObjectName("Sender")
        self.Receiver = QtWidgets.QLabel(SendMessage)
        self.Receiver.setGeometry(QtCore.QRect(180, 170, 91, 41))
        self.Receiver.setFont(font)
        self.Receiver.setObjectName("Receiver")
        self.SenderName = QtWidgets.QLabel(SendMessage)
        self.SenderName.setGeometry(QtCore.QRect(340, 110, 171, 41))
        self.SenderName.setFont(font)
        self.SenderName.setObjectName("SenderName")
        font.setPointSize(16)
        self.comboBoxReceiver = QtWidgets.QComboBox(SendMessage)
        self.comboBoxReceiver.setGeometry(QtCore.QRect(340, 170, 181, 31))
        self.comboBoxReceiver.setFont(font)
        self.comboBoxReceiver.setObjectName("comboBoxReceiver")
        self.label = QtWidgets.QLabel(SendMessage)
        self.label.setGeometry(QtCore.QRect(20, 590, 151, 41))
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(SendMessage)
        QtCore.QMetaObject.connectSlotsByName(SendMessage)

    def retranslateUi(self, SendMessage):
        _translate = QtCore.QCoreApplication.translate
        SendMessage.setWindowTitle(_translate("SendMessage", "SendMessage"))
        self.PlainButton.setText(_translate("SendMessage", "Plain"))
        self.SendAMessage.setText(_translate("SendMessage", "Send a message"))
        self.EncryptButton.setText(_translate("SendMessage", "Encrypt"))
        self.SignatureButton.setText(_translate("SendMessage", "Signature"))
        self.Sender.setText(_translate("SendMessage", "Sender"))
        self.Receiver.setText(_translate("SendMessage", "Receiver"))
        self.SenderName.setText(_translate("SendMessage", "SenderName"))
        self.label.setText(_translate("SendMessage", "Your private key"))

    def showStudentName(self, user):
        self.SenderName.setText(user.getStudentName())

    def showReceiverStudents(self, user, database):
        studentList = database.getAllStudents() 
        studentList.remove(user.getStudentName())
        self.comboBoxReceiver.addItems(studentList)
    
    def clear(self):
        self.textMessage.setText("")
        self.comboBoxReceiver.clear()
    
    def getUserInputForPlainText(self):
        return self.SenderName.text(), self.comboBoxReceiver.currentText(), self.textMessage.toPlainText()

    def getSenderPrivateKeyAndMessage(self):
        file_name = QFileDialog.getOpenFileName()
        path = file_name[0]
        privKey = load_priv_key(path)

        return privKey, self.textMessage.toPlainText()