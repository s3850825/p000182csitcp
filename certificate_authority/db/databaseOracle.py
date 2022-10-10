import cx_Oracle
import os

class DatabaseOracle():
    def __init__(self):
        path = os.getcwd() + "\db\instantclient-basic-windows.x64-21.6.0.0.0dbru\instantclient_21_6"
        cx_Oracle.init_oracle_client(lib_dir=path) 
        self.connection = cx_Oracle.connect(user='admin', password='P000182csitcp!', dsn='p000182csitcp_high')
        self.cursor = self.connection.cursor()
        self.connection.outputtypehandler = output_type_handler

    def insertNewStudent(self, username, password, walletPassword):
        query1 = "SELECT count(*) FROM student"
        self.cursor.execute(query1)
        studentId = self.cursor.fetchone()[0] + 1

        query2 = "INSERT INTO student (id, username, password, walletPassword, publicKey, privateKey) VALUES (:1, :2, :3, :4, :5, :6)"
        self.cursor.execute(query2, (studentId, username, password, walletPassword, None, None,))

    def updateNewStudentKeyPairs(self, privKey, pubKey, username):
        query = "UPDATE student set privateKey = :1, publicKey = :2 WHERE username = :3"
        self.cursor.execute(query, (privKey, pubKey, username))

    def deleteExistentStudent(self, username):
        query = "DELETE FROM student WHERE username=:1" 
        self.cursor.execute(query, (username,))

    def checkUniqueStudentName(self, username):
        query = "SELECT count(*) FROM student WHERE username=:1"
        self.cursor.execute(query, (username,))
        result = self.cursor.fetchall()
        if result[0][0] == 0:
            return True
        return False

    def checkStudentInfo(self, username, password):
        query = "SELECT * FROM student WHERE username=:1 AND password=:2"
        self.cursor.execute(query, (username, password))
        result = self.cursor.fetchall()
        if (result != []):
            return True
        return False
    
    def getStudentWalletPassword(self, username):
        query = "SELECT walletPassword FROM student WHERE username=:1"
        self.cursor.execute(query, (username,))
        walletPW = self.cursor.fetchall()
        return walletPW[0][0]
    
    def getStudentPrivateKey(self, username):
        query = "SELECT privateKey FROM student WHERE username=:1"
        self.cursor.execute(query, (username,))
        privKey = self.cursor.fetchall()
        return privKey[0][0]

    def getStudentPublicKey(self, username):
        query = "SELECT publicKey FROM student WHERE username=:1"
        self.cursor.execute(query, (username,))
        pubKey = self.cursor.fetchall()
        return pubKey[0][0]
    
    def getAllStudents(self):
        query = "SELECT username FROM student"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        studentList = []
        for student in result:
            studentList.append(student[0])
        return studentList

    def insertMessage(self, sender, receiver, time, messageType, message, encrypted_message, signed_message, signed_encrypted_message):
        query = "INSERT INTO message (sender, receiver, time, messagetype, message, encrypted_message, signed_message, signed_encrypted_message) VALUES (:1, :2, :3, :4, :5, :6, :7, :8)"
        self.cursor.execute(query, (sender, receiver, time, messageType, message, encrypted_message, signed_message, signed_encrypted_message))

    def getReceivedMessages(self, username):
        query = "SELECT * FROM message WHERE receiver=:1"
        self.cursor.execute(query, (username,))
        allMessages = self.cursor.fetchall()
        return allMessages
    
    def getUserIndexUsingWalletPassword(self, walletPassword):
        query = "SELECT id FROM student WHERE walletPassword=:1"
        self.cursor.execute(query, (walletPassword,))
        userIndex = self.cursor.fetchall()

        query = "SELECT count(*) FROM student"
        self.cursor.execute(query)
        totalUserNumber = self.cursor.fetchall()
 
        return userIndex[0][0] - totalUserNumber[0][0] - 1

def output_type_handler(cursor, name, default_type, size, precision, scale):
    if default_type == cx_Oracle.DB_TYPE_CLOB:
        return cursor.var(cx_Oracle.DB_TYPE_LONG, arraysize=cursor.arraysize)
    if default_type == cx_Oracle.DB_TYPE_BLOB:
        return cursor.var(cx_Oracle.DB_TYPE_LONG_RAW, arraysize=cursor.arraysize)