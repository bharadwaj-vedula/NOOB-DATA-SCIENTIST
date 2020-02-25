import tkinter
from tkinter import *
import sqlite3 as sql
import sys

window=tkinter.Tk()
window.title("PHONE BOOK")
window.geometry('720x720')

firstname=StringVar()
lastname=StringVar()
email=StringVar()
phonenum=StringVar()
rows=StringVar()
var=StringVar()
i=int(0)
lstList1=[]

Label(window,text="First Name").grid(row = 0, column = 0, padx = (27,0), pady = (10,0), sticky = 'nw')
e1=Entry(window,textvariable=firstname).grid(row = 1, column = 0, columnspan = 2, padx = (30,40), pady = (0,0), sticky = 'new')

Label(window,text="Last Name").grid(row = 2, column = 0, padx = (27,0), pady = (10,0), sticky = 'nw')
e2=Entry(window,textvariable=lastname).grid(row = 3, column = 0, columnspan = 2, padx = (30,40), pady = (0,0), sticky = 'new')

Label(window,text="Phone Number").grid(row = 4, column = 0, padx = (27,0), pady = (10,0), sticky = 'nw')
e3=Entry(window,textvariable=phonenum).grid(row = 5, column = 0, columnspan = 2, padx = (30,40), pady = (0,0), sticky = 'new')

Label(window,text="Email").grid(row = 6, column = 0, padx = (27,0), pady = (10,0), sticky = 'nw')
e4=Entry(window,textvariable=email).grid(row = 7, column = 0, columnspan = 2, padx = (30,40), pady = (0,0), sticky = 'new')

Label(window,text="User:-").grid(row = 0, column = 2, padx = (0,0), pady = (10,0), sticky = 'nw')
lb=Listbox(window,width=40).grid(row=1,column=6)

#Label(window,text=item).grid(row=8,column=4)
con=sql.connect('phone_book.db')
with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(first_name TEXT,last_name TEXT,phone_number INT,email TEXT)")


def add():
    
    with con:
        cur=con.cursor()
        cur.execute("INSERT INTO users VALUES(?,?,?,?)",[firstname.get(),lastname.get(),phonenum.get(),email.get()])
        con.commit()
        rows=cur.fetchall()
        display_list()
def update():
    with con:
        cur=con.cursor()
        cur.execute("UPDATE users SET last_name=?,phone_number=?,email=? where first_name=?",[lastname.get(),phonenum.get(),email.get(),firstname.get()])
        con.commit()
        display_list()

def delete():
    with con:
        cur=con.cursor()
        cur.execute("DELETE FROM users WHERE first_name=?",[firstname.get()])
        con.commit()
        display_list()
def close():
    window.destroy()

def display_list():
    with con:
        cur=con.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
    lb=Listbox(window,width=40)
    for i in range(0,len(rows)):
        lb.insert(END,rows[i])
    lb.grid(row=1,column=6)

Button(window,text="Add",command=add).grid(row = 8, column = 0, padx = (25,0), pady = (45,10), sticky = 'w')
Button(window,text="Update",command=update).grid(row = 8, column = 1, padx = (15,0), pady = (45,10), sticky = 'w')
Button(window,text="Delete",command=delete).grid(row = 8, column = 2, padx = (15,0), pady = (45,10), sticky = 'w')
Button(window,text="Close",command=close).grid(row = 8, column = 3, padx = (15,0), pady = (45,10), sticky = 'e')
mainloop()
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)
print(len(rows))

