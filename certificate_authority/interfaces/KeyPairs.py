# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_KeyParis.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KeyPairs(object):
    def setupUi(self, KeyPairs):
        KeyPairs.setObjectName("KeyPairs page")
        KeyPairs.resize(555, 620)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.privKey = QtWidgets.QTextEdit(KeyPairs)
        self.privKey.setGeometry(QtCore.QRect(40, 90, 471, 311))
        self.privKey.setObjectName("privKey")
        self.pubKey = QtWidgets.QTextEdit(KeyPairs)
        self.pubKey.setGeometry(QtCore.QRect(40, 460, 471, 121))
        self.pubKey.setObjectName("pubKey")
        self.privKeyLabel = QtWidgets.QLabel(KeyPairs)
        self.privKeyLabel.setGeometry(QtCore.QRect(50, 40, 261, 31))
        font.setPointSize(16)
        self.privKeyLabel.setFont(font)
        self.privKeyLabel.setObjectName("privKeyLabel")
        self.pubKeyLabel = QtWidgets.QLabel(KeyPairs)
        self.pubKeyLabel.setGeometry(QtCore.QRect(50, 410, 261, 31))
        self.pubKeyLabel.setFont(font)
        self.pubKeyLabel.setObjectName("pubKeyLabel")

        self.retranslateUi(KeyPairs)
        QtCore.QMetaObject.connectSlotsByName(KeyPairs)

    def retranslateUi(self, KeyPairs):
        _translate = QtCore.QCoreApplication.translate
        KeyPairs.setWindowTitle(_translate("KeyPairs", "KeyPairs"))
        self.privKeyLabel.setText(_translate("KeyPairs", "Private Key"))
        self.pubKeyLabel.setText(_translate("KeyPairs", "Public Key"))
    
    def showStudentKeyPairs(self, user):
        privKeyStr = str(user.getPrivateKey())
        privKeyStr = privKeyStr[2:len(privKeyStr) - 1]
        print("--\n" + privKeyStr +"--\n")
        privKey = privKeyStr.replace(r"\n", '').replace(r"\r", '')
        print("--\n" +privKey + "--\n")

        pubKeyStr = str(user.getPublicKey())
        pubKeyStr = pubKeyStr[2:len(pubKeyStr) - 1]
        print("--\n", pubKeyStr, "--\n")
        pubKey = pubKeyStr.replace(r"\n", '').replace(r"\r", '')
        print("--\n" +pubKey + "--\n")
        
        self.privKey.setText(privKey)
        self.pubKey.setText(pubKey)
