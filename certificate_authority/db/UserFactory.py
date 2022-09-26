import sqlite3
import sys
from certificate_authority.db.User import User
from certificate_authority.db.Database import bcDB

class UserFactory:
    def __init__(self, **table: {str:list}):
        #generate a database connection
        try: self._db = bcDB(filename='BlockChain.db')
        except: #default except
            print(f'connection error: {sys.exc_info()[1]}')
        else: print ("Opened db successfully")
        #create the tables in database
        for t in table.keys():
            sql = 'CREATE TABLE IF NOT EXISTS {} \
                     ({} {}({}) NOT NULL,\
                     {} {}({}) NOT NULL,\
                     {} {}({}) NOT NULL,\
                     {} {}({}) NOT NULL,\
                     {} {} NOT NULL,\
                     PRIMARY KEY (USERNAME))'.format(t)
            self._db.sql_execute(sql, {})
        pass

    def get_user(self, username: str, password: str):
        pass

    def exist_account(self, username: str, password: str):
        pass
        return False

    def create_user(self, username: str, password: str):
        pass

    def update_username(self, username: str):
        pass

    def update_user_password(self, username: str, password: str):
        pass

    def create_certificate(self, certifcate):
        pass