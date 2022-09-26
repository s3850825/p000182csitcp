import sqlite3

class Database():
    def __init__(self):
        self.DATABASE_FILE = 'test.db'
        # isolation_level=None is for auto commit
        self.conn = sqlite3.connect(self.DATABASE_FILE, isolation_level=None)
        self.c = self.conn.cursor()

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
        query = "INSERT INTO student VALUES('" + username + "', '" + password + "', '" + walletPassword + "')"
        self.c.execute(query)

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
        print(result)
        if (result != []):
            return True
        return False

    def backupDB(self):
        with self.conn:
            with open('dump.sql', 'w') as f:
                for line in self.conn.iterdump():
                    f.write('%s\n' % line)
                print('Back up is complted.')

    def init(self):
        # add first student to test
        executeQuery("INSERT INTO student VALUES('s123456', 'abcd', 'walletpassword')")

        # add new student account into DB when a student creates an account
        insertNewStudent("s12345", "abcd", "walletPassword") 

        # delete existent student account from DB
        deleteExistentStudent("s123456")

        # backup database before close
        backupDB()