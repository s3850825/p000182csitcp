import sqlite3

class Database():
    def __init__(self):
        self.DATABASE_FILE = 'test.db'
        # isolation_level=None is for auto commit
        self.conn = sqlite3.connect(self.DATABASE_FILE, isolation_level=None)
        self.c = self.conn.cursor()
        self.executeQuery("CREATE TABLE IF NOT EXISTS student (id integer PRIMARY KEY AUTOINCREMENT, username text, password text, walletPassword text, publicKey blob, privateKey blob)")
        self.executeQuery("CREATE TABLE IF NOT EXISTS message (sender text, receiver text, type text, message blob, og_message text)")

    def database(self):
        # connect to DB
        try:
            print("Database created and successfully connected to SQLite!")

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)

    def executeQuery(self, query):
        # execute the query
        self.c.execute(query)

    def insertNewStudent(self, username, password, walletPassword):
        query = "INSERT INTO student (id, username, password, walletPassword, publicKey, privateKey) VALUES (?, ?, ?, ?, ?, ?)"
        self.c.execute(query, (None, username, password, walletPassword, None, None,))

    def updateNewStudentKeyPairs(self, privKey, pubKey, username):
        query = "UPDATE student set privateKey = ?,  publicKey = ? WHERE username = ?"
        self.c.execute(query, (privKey, pubKey, username))

    def deleteExistentStudent(self, username):
        query = "DELETE FROM student WHERE username=:username" 
        self.c.execute(query, {'username': username})

    def checkUniqueStudentName(self, username):
        query = "SELECT count(*) FROM student WHERE username=:username"
        self.c.execute(query, {'username': username})
        result = self.c.fetchall()
        if result[0][0] == 0:
            return True
        return False

    def checkStudentInfo(self, username, password):
        query = "SELECT * FROM student WHERE username=:username AND password=:password"
        self.c.execute(query, {'username': username, 'password': password})
        result = self.c.fetchall()
        if (result != []):
            return True
        return False
    
    def getStudentWalletPassword(self, username):
        query = "SELECT walletPassword FROM student WHERE username=:username"
        self.c.execute(query, {'username': username})
        walletPW = self.c.fetchall()
        return walletPW[0][0]
    
    def getStudentPrivateKey(self, username):
        query = "SELECT privateKey FROM student WHERE username=:username"
        self.c.execute(query, {'username': username})
        privKey = self.c.fetchall()
        return privKey[0][0]

    def getStudentPublicKey(self, username):
        query = "SELECT publicKey FROM student WHERE username=:username"
        self.c.execute(query, {'username': username})
        pubKey = self.c.fetchall()
        return pubKey[0][0]
    
    def getAllStudents(self):
        query = "SELECT username FROM student"
        self.c.execute(query)
        result = self.c.fetchall()
        studentList = []
        for student in result:
            studentList.append(student[0])
        return studentList

    def insertMessage(self, sender, receiver, message, og_message, messageType):
        query = "INSERT INTO message VALUES('" + sender + "', '" + receiver + "', '" + messageType + "', ?, ?)"
        self.c.execute(query, (message, og_message,))

    def getReceivedMessages(self, username):
        query = "SELECT * FROM message WHERE receiver=:username"
        self.c.execute(query, {'username': username})
        allMessages = self.c.fetchall()
        return allMessages
    
    def getUserIndexUsingWalletPassword(self, walletPassword):
        query = "SELECT id FROM student WHERE walletPassword=:walletPassword"
        self.c.execute(query, {'walletPassword': walletPassword})
        userIndex = self.c.fetchall()

        query = "SELECT count(*) FROM student"
        self.c.execute(query)
        totalUserNumber = self.c.fetchall()
 
        return userIndex[0][0] - totalUserNumber[0][0] - 1

    def backupDB(self):
        with self.conn:
            with open('dump.sql', 'w') as f:
                for line in self.conn.iterdump():
                    f.write('%s\n' % line)
                print('Back up is complted.')