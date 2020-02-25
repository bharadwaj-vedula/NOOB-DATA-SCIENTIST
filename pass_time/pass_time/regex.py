import re
import sqlite3 as sql
import sys

data=open("D:\Bharadwaj\SEM-4\PL\emailids.txt")
lines=data.read()

x1=re.findall(r'\.com',lines)
x2=re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.(in)',lines)
x3=re.findall(r'\.net',lines)
x4=re.findall(r'\.edu',lines)
print(len(x1))
print(len(x2))
print(len(x3))
print(len(x4))


con=sql.connect("regex.db")
cur=con.cursor()
with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE  IF NOT EXISTS entries(word TEXT, num NUMBER)")
    cur.execute("INSERT INTO entries VALUES(?,?)",["com",len(x1)])
    con.commit()

print("hi")
cur.execute("SELECT * FROM entries")
rows=cur.fetchall()
for row in rows:
    print(row)
