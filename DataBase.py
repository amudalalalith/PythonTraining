import sqlite3

conn = sqlite3.connect('test.db')


conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")



conn.commit()

cursor = conn.execute("SELECT id, name, age, address, salary from COMPANY where ID = 1")
for row in cursor:
print "ID = ", row[0]
print "NAME = ", row[1]
print "Age = ", row[2] 
print "ADDRESS = ", row[3]
print "SALARY = ", row[4], "\n"
