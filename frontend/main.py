import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidgetItem, QWidget
from login import Ui_Form
from mainWindow import Ui_MainWindow
import pickle
import os


class MainWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.switchingToLoginView()
        self.pushButton.clicked.connect(lambda: self.switchingToLoginView())
        self.pushButton_2.clicked.connect(lambda: self.switchingToRegisterView())
        self.pushButton_3.clicked.connect(lambda: self.login())
        self.pushButton_6.clicked.connect(lambda: self.register())
        self.userFile = 'users.pkl'
        self.child_window = SubWindow()

    def switchingToLoginView(self):
        self.widget_3.hide()
        self.widget_2.show()

    def switchingToRegisterView(self):
        self.widget_3.show()
        self.widget_2.hide()

    def save_user(self, users_dict):
        with open(self.userFile, 'wb') as f:
            pickle.dump(users_dict, f)

    def loadUser(self):
        """

        :return:
        """
        try:
            with open(self.userFile, 'rb') as f:
                user_dict = pickle.load(f)
            return user_dict
        except Exception as e:
            print(e)

    def register(self):
        if os.path.exists(self.userFile):
            user_dict = self.loadUser()
        else:
            user_dict = {}

        username = self.lineEdit_5.text()
        password_1 = self.lineEdit_6.text()
        password_2 = self.lineEdit_7.text()
        if username in user_dict:
            # the account already existed
            QMessageBox.warning(self, "warning", "the account already existed")
            return
        elif password_1 != password_2:
            # same password
            QMessageBox.warning(self, "warning", "two passwords not the same")
        else:
            user_dict[username] = password_1
            self.save_user(user_dict)
            self.switchingToLoginView()

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        user_dict = self.loadUser()
        if user_dict:
            if password == user_dict.get(username):
                # jump to main page
                self.show_child()
                pass
            else:
                QMessageBox.warning(self, "warning", "account or password not correct")
        else:
            QMessageBox.warning(self, "warning", "no user information, please register")
            self.switchingToRegisterView()

    def show_child(self):
        self.close()
        self.child_window.show()


class SubWindow(QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super(SubWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = MainWindow()
    view.show()
    sys.exit(app.exec_())
