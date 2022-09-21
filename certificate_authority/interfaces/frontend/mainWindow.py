# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 824)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 531, 71))
        self.widget.setStyleSheet("background-color: rgb(148, 60, 255);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 10, 51, 51))
        self.label.setStyleSheet("image: url(:/logo/image/logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(90, 30, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(220, 18, 281, 35))
        self.widget_2.setStyleSheet("background-color: rgb(194, 151, 255);\n"
"border-radius:10px;\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(10, 4, 25, 25))
        self.label_3.setStyleSheet("image: url(:/search/image/search.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(50, 5, 221, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border:none;")
        self.lineEdit.setObjectName("lineEdit")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(0, 80, 531, 401))
        self.widget_3.setObjectName("widget_3")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(200, 20, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(148, 60, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setGeometry(QtCore.QRect(230, 70, 60, 60))
        self.label_5.setStyleSheet("image: url(:/avatar/image/avatar.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(220, 140, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(21)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(210, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(210, 210, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        self.label_9.setGeometry(QtCore.QRect(70, 240, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setGeometry(QtCore.QRect(210, 270, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setGeometry(QtCore.QRect(160, 330, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius:10px;\n"
"color:rgb(148, 60, 255);\n"
"border:3px solid rgb(255, 178, 242);")
        self.pushButton.setObjectName("pushButton")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(0, 480, 531, 341))
        self.widget_4.setObjectName("widget_4")
        self.label_11 = QtWidgets.QLabel(self.widget_4)
        self.label_11.setGeometry(QtCore.QRect(150, 50, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("image: url(:/tip/image/document1.png);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.widget_4)
        self.label_12.setGeometry(QtCore.QRect(210, 50, 171, 40))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.widget_4)
        self.label_13.setGeometry(QtCore.QRect(210, 100, 171, 40))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.widget_4)
        self.label_14.setGeometry(QtCore.QRect(150, 100, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("image: url(:/tip/image/document1.png);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.widget_4)
        self.label_15.setGeometry(QtCore.QRect(210, 150, 171, 40))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(18)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.widget_4)
        self.label_16.setGeometry(QtCore.QRect(150, 150, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("image: url(:/tip/image/document2.png);")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.widget_4)
        self.label_17.setGeometry(QtCore.QRect(210, 200, 171, 40))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(18)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.widget_4)
        self.label_18.setGeometry(QtCore.QRect(150, 200, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("image: url(:/tip/image/document1.png);")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Hi!"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Search"))
        self.label_4.setText(_translate("MainWindow", "My Profile"))
        self.label_6.setText(_translate("MainWindow", "nikhil"))
        self.label_7.setText(_translate("MainWindow", "My Address"))
        self.label_8.setText(_translate("MainWindow", "New York"))
        self.label_9.setText(_translate("MainWindow", "70 Washington Square South New York, NY"))
        self.label_10.setText(_translate("MainWindow", "Good place"))
        self.pushButton.setText(_translate("MainWindow", "VIEW PROFILE"))
        self.label_12.setText(_translate("MainWindow", "My Documents"))
        self.label_13.setText(_translate("MainWindow", "Give Access"))
        self.label_15.setText(_translate("MainWindow", "Free Access"))
        self.label_17.setText(_translate("MainWindow", "Change Institute"))
import interfaces.frontend.resource_rc
