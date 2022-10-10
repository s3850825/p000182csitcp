# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SendFile.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir, Qt
from PyQt5.QtWidgets import QApplication, QInputDialog, QFileDialog
from scripts.crypto import *
import os

class Ui_Send_File(object):
    def setupUi(self, SendFile):
        SendFile.setObjectName("SendFile")
        SendFile.resize(681, 743)
        self.EncryptAndSignButton = QtWidgets.QPushButton(SendFile)
        self.EncryptAndSignButton.setGeometry(QtCore.QRect(220, 510, 255, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.EncryptAndSignButton.setFont(font)
        self.EncryptAndSignButton.setObjectName("EncryptAndSignButton")
        self.EncryptAndSignButton.setStyleSheet(self.css_pushButton())
        self.SendFile = QtWidgets.QLabel(SendFile)
        self.SendFile.setGeometry(QtCore.QRect(260, 20, 451, 51))
        font.setPointSize(24)
        self.SendFile.setFont(font)
        self.SendFile.setObjectName("SendFile")
        font.setPointSize(16)
        self.filePathLabel = QtWidgets.QLabel(SendFile)
        self.filePathLabel.setGeometry(QtCore.QRect(0, 240, 681, 60))
        self.filePathLabel.setFont(font)
        self.filePathLabel.setObjectName("filePathLabel")
        self.filePathLabel.setStyleSheet("color: rgb(0, 0, 255);")
        self.filePathLabel.setAlignment(Qt.AlignCenter)
        self.ChooseAFileButton = QtWidgets.QPushButton(SendFile)
        self.ChooseAFileButton.setGeometry(QtCore.QRect(220, 300, 255, 51))
        self.ChooseAFileButton.setFont(font)
        self.ChooseAFileButton.setObjectName("ChooseAFileButton")
        self.ChooseAFileButton.clicked.connect(self.chooseAFile)
        self.EncryptButton = QtWidgets.QPushButton(SendFile)
        self.EncryptButton.setGeometry(QtCore.QRect(220, 580, 255, 51))
        self.EncryptButton.setFont(font)
        self.EncryptButton.setObjectName("EncryptButton")
        self.EncryptButton.setStyleSheet(self.css_pushButton())
        self.SignatureButton = QtWidgets.QPushButton(SendFile)
        self.SignatureButton.setGeometry(QtCore.QRect(220, 650, 255, 51))
        self.SignatureButton.setFont(font)
        self.SignatureButton.setObjectName("SignatureButton")
        self.SignatureButton.setStyleSheet(self.css_pushButton())
        self.Sender = QtWidgets.QLabel(SendFile)
        self.Sender.setGeometry(QtCore.QRect(180, 90, 91, 41))
        font.setPointSize(14)
        self.Sender.setFont(font)
        self.Sender.setObjectName("Sender")
        self.Receiver = QtWidgets.QLabel(SendFile)
        self.Receiver.setGeometry(QtCore.QRect(180, 150, 91, 41))
        self.Receiver.setFont(font)
        self.Receiver.setObjectName("Receiver")
        self.SenderName = QtWidgets.QLabel(SendFile)
        self.SenderName.setGeometry(QtCore.QRect(340, 90, 171, 41))
        self.SenderName.setFont(font)
        self.SenderName.setObjectName("SenderName")
        font.setPointSize(16)
        self.comboBoxReceiver = QtWidgets.QComboBox(SendFile)
        self.comboBoxReceiver.setGeometry(QtCore.QRect(340, 150, 181, 31))
        self.comboBoxReceiver.setFont(font)
        self.comboBoxReceiver.setObjectName("comboBoxReceiver")
        self.privateKeyLabel = QtWidgets.QLabel(SendFile)
        self.privateKeyLabel.setGeometry(QtCore.QRect(150, 370, 440, 61))
        self.privateKeyLabel.setFont(font)
        self.privateKeyLabel.setObjectName("privateKeyLabel")
        self.privateKeyLabel.setStyleSheet("color: rgb(0, 0, 255);")
        self.privateKeyPath = QtWidgets.QPlainTextEdit(SendFile)
        self.privateKeyPath.setGeometry(QtCore.QRect(145, 430, 400, 60))
        self.privateKeyPath.setFont(font)
        self.privateKeyPath.setObjectName("privateKeyPath")
        self.privateKeyPath.textChanged.connect(self.privKeyChanged)
        self.EncryptAndSignButton.setEnabled(False)
        self.SignatureButton.setEnabled(False)

        self.retranslateUi(SendFile)
        QtCore.QMetaObject.connectSlotsByName(SendFile)

    def retranslateUi(self, SendFile):
        _translate = QtCore.QCoreApplication.translate
        SendFile.setWindowTitle(_translate("SendFile", "Send a file page"))
        self.EncryptAndSignButton.setText(_translate("SendFile", "Encrypt, Sign and Send"))
        self.SendFile.setText(_translate("SendFile", "Send a file"))
        self.EncryptButton.setText(_translate("SendFile", "Encrypt and Send"))
        self.SignatureButton.setText(_translate("SendFile", "Sign and Send"))
        self.Sender.setText(_translate("SendFile", "Sender"))
        self.Receiver.setText(_translate("SendFile", "Receiver"))
        self.SenderName.setText(_translate("SendFile", "SenderName"))
        self.privateKeyLabel.setText(_translate("MessageBoard", "Type Your private key path to sign the file"))
        self.ChooseAFileButton.setText(_translate("SendFile", "Choose a file to send"))
        self.filePathLabel.setText(_translate("SendFile", ""))

    def showStudentName(self, user):
        self.SenderName.setText(user.getStudentName())

    def showReceiverStudents(self, user, database):
        studentList = database.getAllStudents() 
        studentList.remove(user.getStudentName())
        self.comboBoxReceiver.clear()
        self.comboBoxReceiver.addItems(studentList)
    
    def clear(self):
        self.comboBoxReceiver.clear()
        self.filePathLabel.setText("")
    
    def getUserInputForPlainText(self):
        return self.SenderName.text(), self.comboBoxReceiver.currentText(), self.filePathLabel.text()

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

    def privateKeyPathclear(self):
        self.privateKeyPath.clear()

    def chooseAFile(self):
        file_name = QFileDialog.getOpenFileName()
        if file_name[0] != '':
            print(os.path.splitext(file_name[0])[1])
            self.filePathLabel.setText(file_name[0])
        