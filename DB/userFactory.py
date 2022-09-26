from user import User
from customerError import CustomError
import sqlite3
import customerError


class UserFactory:
    DATABASE_FILE = 'test.db'
    TABLE_NAME = 'student'
    def __init__(self, DATABASE_FILE = 'test.db'):
        try:
            # isolation_level=None is for auto commit
            self.conn = sqlite3.connect(DATABASE_FILE, isolation_level=None)
            # create cursor to read and write in Python
            self.c = self.conn.cursor()
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        else:
            print("Database created and successfully connected to SQLite!")

    def getUser(self, userName: str, password: str, DATABASE_FILE = 'test.db', TABLE_NAME = 'student'):
        user = User(userName, password)
        try:
            query = "SELECT * FROM {0} WHERE username = '{1}' AND password = '{2}'".format(TABLE_NAME, user.getUserName(),
                                                                                       user.getPassword())
            self.c.execute(query)
            result = self.c.fetchall()
            if len(result) <= 0:
                raise CustomError
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        except CustomError as error:
            print("Wrong username or password", error)
        else:
            return user

    # Justify whether is the userName unique or not
    def existUserName(self, userName: str, TABLE_NAME = 'student'):

        query = "SELECT * FROM {0} WHERE username = '{1}'".format(TABLE_NAME, userName)
        self.c.execute(query)
        result = self.c.fetchall()

        if len(result) <= 0:
            return False
        else:
            return True

    def createUser(self, userName: str, password: str, TABLE_NAME = 'student'):
        user = User(userName, password)
        # search in database
        query = "INSERT INTO {0} VALUES('{1}', '{2}')".format(TABLE_NAME, user.getUserName(), user.getPassword())
        self.c.execute(query)

        return user


