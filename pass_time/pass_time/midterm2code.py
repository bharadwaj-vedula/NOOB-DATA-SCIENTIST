import re
import sqlite3 as lite
import sys 


##pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.(com|in|net|edu)+")
pattern1 = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.(com)+")
pattern2 = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.(in)+")
pattern3 = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.(net)+")
pattern4 = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.(edu)+")
#matches = pattern.findall()
with open('emailids.txt','r') as f:
    contents = f.read()
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    matches1= pattern1.findall(contents)
    
    matches2 = pattern2.findall(contents)
    matches3 = pattern3.findall(contents)
    matches4 = pattern4.findall(contents)
##    for match in matches:
##        if (match == "com"):
##            count1 = count1 + 1
##        elif (match == "in"):
##            count2 = count2 + 1
##        elif (match == "net"):
##            count3 = count3 + 1
##        else:
##            count4 = count4 + 1
        
    count1=matches1.count('com')
    count2=matches2.count('in')
    count3=matches3.count('net')
    count4=matches4.count('edu')
         
      
         
#with open('emailids.txt','r') as f:
    #contents = f.read()
    #count = 0
    #matches = pattern.findall(contents)
    #for match in matches:
        #count=count+1
        #print("The total emails are" +str(count))
##    print("The total emails ending in com are " + str(count1))
##    print("The total emails ending in in are " + str(count2))
##    print("The total emails ending in net are " + str(count3))
##    print("The total emails ending in edu are " + str(count4))
con = lite.connect('usermail.db')

with con:
            cur=con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS mail_data(Srno TEXT, Domain_name TEXT, Count TEXT)")
            
            cur.execute("INSERT INTO mail_data VALUES(?,?,?)",("1","com",str(count1)))
            cur.execute("INSERT INTO mail_data VALUES(?,?,?)",("2","in",str(count2)))
            cur.execute("INSERT INTO mail_data VALUES(?,?,?)",("3","net",str(count3)))
            cur.execute("INSERT INTO mail_data VALUES(?,?,?)",("4","edu",str(count4)))

            cur.execute("SELECT * FROM mail_data")
            rows = cur.fetchall()
            for row in rows:
                print(row)
                #print("\n")
  
