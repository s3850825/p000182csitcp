import sqlite3

print(sqlite3.version)

# isolation_level=None is for auto commit
conn = sqlite3.connect("test.db", isolation_level=None)

# create cursor to read and write in Python
c = conn.cursor()

# add student table to add student's account info
c.execute("CREATE TABLE IF NOT EXISTS student \
            (id text PRIMARY KEY, password text)")

# add first student to test
c.execute("INSERT INTO student \
            VALUES('s123456', 'abcd')")

