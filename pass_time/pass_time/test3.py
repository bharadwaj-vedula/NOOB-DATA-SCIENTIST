import tkinter
from tkinter import *
import datetime
import sqlite3 as sql
import sys 
window=tkinter.Tk()
window.title("NMIMS LOGIN PAGE")
window.geometry('350x250')
username = StringVar()
password = StringVar()

con=sql.connect("login.db")
with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS login_user(username TEXT,password TEXT)")
    con.commit()
def createl():
    var = username.get()
    war=password.get()
    if (var == ''):
        if (war == ''):
            win5=tkinter.Tk()
            win5.title=("***Login***")
            win5.geometry('250x150+500+150')
            tkinter.Label(win5,text='ERROR!!').pack()
            win5.mainloop()
    else:
        cur.execute("INSERT INTO login_user VALUES(?,?)",[var,war])
        con.commit()
def login():
    var = username.get()
    war = password.get()
    if (var == ''):
        if (war == ''):
            win4=tkinter.Tk()
            win4.title=("***Login***")
            win4.geometry('250x150+500+150')
            tkinter.Label(win4,text='ERROR!!').pack()
            win4.mainloop()
    else:
        win3=tkinter.Tk()
        win3.title=("***Login***")
        win3.geometry('250x150+500+150')
        y = datetime.datetime.now()
        #print(y.strftime("%b %d %Y,%I %p"))
        tkinter.Label(win3,text='You tried to login on '+(y.strftime("%b %d %Y,%I %p"))).pack()
        win3.mainloop()
Label(window,text="Username").grid(row=0,column=0)
Entry(window, textvariable=username).grid(row=0,column=1)
Label(window,text="Password").grid(row=1,column=0)
Entry(window, textvariable=password).grid(row=1,column=1)
Entry(window).grid(row=1,column=1)
Button(window,text="Create Login",width=25,command=createl).grid(row=5,column=0,columnspan=2)
Button(window,text='Login',width=25,command=login).grid(row=5,column=2,columnspan=2)
 
window.mainloop()
cur.execute("SELECT * FROM login_user")
rows = cur.fetchall()
print("hello")

for row in rows:
    print(row)

