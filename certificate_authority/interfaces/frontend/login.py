# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(808, 523)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 70, 300, 400))
        self.label.setStyleSheet("border-image: url(:/login/image/login.png);\n"
"borde-top-left-radius:30px;\n"
"borde-botton-left-radius:30px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(400, 70, 361, 400))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"borde-top-right-radius:30px;\n"
"borde-botton-right-radius:30px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(460, 120, 221, 71))
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 181, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("#pushButton{\n"
"    border:none;\n"
"\n"
"}\n"
"#pushButton:focus{\n"
"    color: rgb(168, 168, 168);\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"    border:none;\n"
"\n"
"}\n"
"#pushButton_2:focus{\n"
"    color: rgb(168, 168, 168);\n"
"\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(420, 210, 301, 231))
        self.widget_2.setObjectName("widget_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 100, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 170, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("#pushButton_3{\n"
"    \n"
"    background-color: rgb(135, 126, 114);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:15px;\n"
"\n"
"}\n"
"#pushButton_3:hover{\n"
"    \n"
"    background-color: rgb(195, 195, 195);\n"
"    color: rgb(2, 2, 2);\n"
"    border-radius:15px;\n"
"\n"
"}\n"
"#pushButton_3:pressed{\n"
"    \n"
"    padding-top:5px;\n"
"    padding-left:5px;        \n"
"\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(710, 80, 41, 31))
        self.pushButton_4.setStyleSheet("border:none;")
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName("pushButton_4")
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setGeometry(QtCore.QRect(420, 200, 301, 251))
        self.widget_3.setObjectName("widget_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 20, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(30, 80, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 180, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("#pushButton_6{\n"
"    \n"
"    background-color: rgb(135, 126, 114);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:15px;\n"
"\n"
"}\n"
"#pushButton_6:hover{\n"
"    \n"
"    background-color: rgb(195, 195, 195);\n"
"    color: rgb(2, 2, 2);\n"
"    border-radius:15px;\n"
"\n"
"}\n"
"#pushButton_6:pressed{\n"
"    \n"
"    padding-top:5px;\n"
"    padding-left:5px;        \n"
"\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(30, 130, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px;")
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.retranslateUi(Form)
        self.pushButton_4.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "sign in"))
        self.pushButton_2.setText(_translate("Form", "sign up"))
        self.lineEdit.setPlaceholderText(_translate("Form", "username:"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "password:"))
        self.pushButton_3.setText(_translate("Form", "sign in"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "username:"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "password:"))
        self.pushButton_6.setText(_translate("Form", "sign up"))
        self.lineEdit_7.setPlaceholderText(_translate("Form", "password:"))
import interfaces.frontend.resource_rc
