import sqlite3
from certificate_authority.db.Database import bcDB

def main():

    db = bcDB(filename='BlockChain.db', table='User')
    db.__connect__()


    cur = db.cursor()
    print('create')
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY, string TEXT, number INTEGER
        )
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('one', 1)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('two', 2)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('three', 3)
        """)
    print('commit')
    db.commit()
    print('count')
    cur.execute("SELECT COUNT(*) FROM test")
    count = cur.fetchone()[0]
    print(f'there are {count} rows in the table.')
    print('read')
    for row in cur.execute("SELECT * FROM test"):
        print(row)
    print('drop')
    cur.execute("DROP TABLE test")
    print('close')
    db.close()

if __name__ == '__main__': main()


## 打开数据库连接
conn = sqlite3.connect('py-sqlite.db')
print ("Opened db successfully")

## 清除已存在的表 - company
conn.execute('''DROP TABLE company''');
conn.commit()

## 创建一个表 - company
conn.execute('''CREATE TABLE company
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print ("Table created successfully");

conn.commit()

## 插入数据
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Maxsu', 27, 'Haikou', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 26, 'Shenzhen', 35000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Weiwang', 23, 'Guangzhou', 22000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Marklee', 25, 'Beijing', 45000.00 )");

conn.commit()

## 删除ID值小于等于2的数据
conn.execute("DELETE from COMPANY where ID<=2;")
conn.commit()

print ("Total number of rows updated :", conn.total_changes)

## 更新数据
conn.execute("UPDATE COMPANY set SALARY = 29999.00 where ID=1")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)

print ("Records Insert successfully");
print ('--------------------------- start fetch data from company --------------------------');

## 查询数据
cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Select Operation done successfully.");

conn.close()

