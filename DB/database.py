import sqlite3

DATABASE_FILE = 'test.db'

# connect to DB
try:
    # isolation_level=None is for auto commit
    conn = sqlite3.connect(DATABASE_FILE, isolation_level=None)

    # create cursor to read and write in Python
    c = conn.cursor()

    print("Database created and successfully connected to SQLite!")


except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

def executeQuery(query):
    # execute the query
    c.execute(query)

def insertNewStudent(id, password):
    query = "INSERT INTO student VALUES('" + id + "', '" + password + "')"
    c.execute(query)

def deleteExistentStudent(id):
    query = "DELETE FROM student WHERE id=:id" 
    c.execute(query, {'id': id})

def backupDB():
    with conn:
        with open('dump.sql', 'w') as f:
            for line in conn.iterdump():
                f.write('%s\n' % line)
            print('Back up is complted.')

# add student table to add student's account info
executeQuery("CREATE TABLE IF NOT EXISTS student (id text PRIMARY KEY, password text)")

# add first student to test
executeQuery("INSERT INTO student VALUES('s123456', 'abcd')")

# add new student account into DB when a student creates an account
insertNewStudent("s12345", "abcd") 

# delete existent student account from DB
deleteExistentStudent("s123456")

# backup database before close
backupDB()