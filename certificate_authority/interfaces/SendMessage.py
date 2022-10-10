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
        self.EncryptAndSignButton = QtWidgets.QPushButton(SendMessage)
        self.EncryptAndSignButton.setGeometry(QtCore.QRect(220, 510, 255, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.EncryptAndSignButton.setFont(font)
        self.EncryptAndSignButton.setObjectName("EncryptAndSignButton")
        self.EncryptAndSignButton.setStyleSheet(self.css_pushButton())
        self.SendAMessage = QtWidgets.QLabel(SendMessage)
        self.SendAMessage.setGeometry(QtCore.QRect(225, 20, 451, 51))
        font.setPointSize(24)
        self.SendAMessage.setFont(font)
        self.SendAMessage.setObjectName("SendAMessage")
        self.textMessage = QtWidgets.QTextEdit(SendMessage)
        self.textMessage.setGeometry(QtCore.QRect(90, 220, 511, 160))
        font.setPointSize(16)
        self.textMessage.setFont(font)
        self.textMessage.setObjectName("textMessage")
        self.EncryptButton = QtWidgets.QPushButton(SendMessage)
        self.EncryptButton.setGeometry(QtCore.QRect(220, 580, 255, 51))
        self.EncryptButton.setFont(font)
        self.EncryptButton.setObjectName("EncryptButton")
        self.EncryptButton.setStyleSheet(self.css_pushButton())
        self.SignatureButton = QtWidgets.QPushButton(SendMessage)
        self.SignatureButton.setGeometry(QtCore.QRect(220, 650, 255, 51))
        self.SignatureButton.setFont(font)
        self.SignatureButton.setObjectName("SignatureButton")
        self.SignatureButton.setStyleSheet(self.css_pushButton())
        self.Sender = QtWidgets.QLabel(SendMessage)
        self.Sender.setGeometry(QtCore.QRect(180, 90, 91, 41))
        font.setPointSize(14)
        self.Sender.setFont(font)
        self.Sender.setObjectName("Sender")
        self.Receiver = QtWidgets.QLabel(SendMessage)
        self.Receiver.setGeometry(QtCore.QRect(180, 150, 91, 41))
        self.Receiver.setFont(font)
        self.Receiver.setObjectName("Receiver")
        self.SenderName = QtWidgets.QLabel(SendMessage)
        self.SenderName.setGeometry(QtCore.QRect(340, 90, 171, 41))
        self.SenderName.setFont(font)
        self.SenderName.setObjectName("SenderName")
        font.setPointSize(16)
        self.comboBoxReceiver = QtWidgets.QComboBox(SendMessage)
        self.comboBoxReceiver.setGeometry(QtCore.QRect(340, 150, 181, 31))
        self.comboBoxReceiver.setFont(font)
        self.comboBoxReceiver.setObjectName("comboBoxReceiver")
        self.privateKeyLabel = QtWidgets.QLabel(SendMessage)
        self.privateKeyLabel.setGeometry(QtCore.QRect(160, 370, 400, 61))
        self.privateKeyLabel.setFont(font)
        self.privateKeyLabel.setObjectName("privateKeyLabel")
        self.privateKeyLabel.setStyleSheet("color: rgb(0, 0, 255);")
        self.privateKeyPath = QtWidgets.QPlainTextEdit(SendMessage)
        self.privateKeyPath.setGeometry(QtCore.QRect(145, 430, 400, 60))
        self.privateKeyPath.setFont(font)
        self.privateKeyPath.setObjectName("privateKeyPath")
        self.privateKeyPath.textChanged.connect(self.privKeyChanged)
        self.EncryptAndSignButton.setEnabled(False)
        self.SignatureButton.setEnabled(False)

        self.retranslateUi(SendMessage)
        QtCore.QMetaObject.connectSlotsByName(SendMessage)

    def retranslateUi(self, SendMessage):
        _translate = QtCore.QCoreApplication.translate
        SendMessage.setWindowTitle(_translate("SendMessage", "Send a message page"))
        self.EncryptAndSignButton.setText(_translate("SendMessage", "Encrypt, Sign and Send"))
        self.SendAMessage.setText(_translate("SendMessage", "Send a message"))
        self.EncryptButton.setText(_translate("SendMessage", "Encrypt and Send"))
        self.SignatureButton.setText(_translate("SendMessage", "Sign and Send"))
        self.Sender.setText(_translate("SendMessage", "Sender"))
        self.Receiver.setText(_translate("SendMessage", "Receiver"))
        self.SenderName.setText(_translate("SendMessage", "SenderName"))
        self.privateKeyLabel.setText(_translate("MessageBoard", "Type Your private key path to sign the message"))

    def showStudentName(self, user):
        self.SenderName.setText(user.getStudentName())

    def showReceiverStudents(self, user, database):
        studentList = database.getAllStudents() 
        studentList.remove(user.getStudentName())
        self.comboBoxReceiver.clear()
        self.comboBoxReceiver.addItems(studentList)
    
    def clear(self):
        self.textMessage.setText("")
        self.comboBoxReceiver.clear()
    
    def getUserInputForPlainText(self):
        return self.SenderName.text(), self.comboBoxReceiver.currentText(), self.textMessage.toPlainText()

    def getSenderPrivateKeyAndMessage(self):
        path = self.privateKeyPath.toPlainText()
        privKey = load_priv_key(path)

        return privKey, self.textMessage.toPlainText()

    def privKeyChanged(self):
        if self.privateKeyPath.toPlainText():
            self.EncryptAndSignButton.setEnabled(True)
            self.SignatureButton.setEnabled(True)
        else:
            self.EncryptAndSignButton.setEnabled(False)
            self.SignatureButton.setEnabled(False)

    def css_pushButton(self):
        css = '''
            QPushButton {
                        background-color: blue;
                        color: white;
                        }
            QPushButton:hover {
                            opacity: 0.7;
                        }
            QPushButton:enabled{
                            background-color: blue;
                            }
            QPushButton:disabled {
                            background-color: gray;              
                        }
            '''
        return css
        