import tkinter
from tkinter import *
import sqlite3 as sql
import sys

master =tkinter.Tk()
firstname=StringVar()
lastname=StringVar()
email=StringVar()
phonenum=StringVar()

lbl_fname = Label(master, text = 'First Name: ')
lbl_fname.grid(row = 0, column = 0, padx = (27,0), pady = (10,0), sticky = 'nw')
lbl_lname = Label(master, text = 'Last Name: ')
lbl_lname.grid(row = 2, column = 0, padx = (27,0), pady = (10,0), sticky = 'nw')
lbl_phone = Label(master, text = 'Phone: ')
lbl_phone.grid(row = 4, column = 0, padx = (27,0), pady = (10,0), sticky = 'nw')
lbl_email = Label(master, text = 'Email: ')
lbl_email.grid(row = 6, column = 0, padx = (27,0), pady = (10,0), sticky = 'nw')
lbl_user = Label(master, text = 'User: ')
lbl_user.grid(row = 0, column = 2, padx = (0,0), pady = (10,0), sticky = 'nw')

txt_Firstname = Entry(master, textvariable =firstname)
txt_Firstname.grid(row = 1, column = 0, columnspan = 2, padx = (30,40), pady = (0,0), sticky = 'new')
txt_Lastname = Entry(master, textvariable = lastname)
txt_Lastname.grid(row = 3, column = 0, columnspan = 2, padx = (30,40), pady = (0,0), sticky = 'new')
txt_Phone = Entry(master, textvariable = phonenum)
txt_Phone.grid(row = 5, column = 0, columnspan = 2, padx = (30,40), pady = (0,0), sticky = 'new')
txt_email = Entry(master, textvariable =email)
txt_email.grid(row = 7, column = 0, columnspan = 2, padx = (30,40), pady = (0,0), sticky = 'new')

scrollbar1 = Scrollbar(master, orient = VERTICAL)
lb= Listbox(master, exportselection = 0)
#lstList1.bind('<<ListboxSelect>>', self.on_select)
#scrollbar1.config(command =lstList1.yview)
scrollbar1.grid(row = 1, column = 5, rowspan = 7, sticky = 'nes')
lb.grid(row = 1, column = 2, rowspan = 7, columnspan = 3, sticky = 'nsew')

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
    master.destroy()

def display_list():
    with con:
        cur=con.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
    lb=Listbox(master,width=40)
    for i in range(0,len(rows)):
        lb.insert(END,rows[i])
    lb.grid(row = 1, column = 2, rowspan = 7, columnspan = 3, sticky = 'nsew')

    
btn_add = Button(master, width = 12, height = 2, text = 'Add', command =add)
btn_add.grid(row = 8, column = 0, padx = (25,0), pady = (45,10), sticky = 'w')
btn_update = Button(master, width = 12, height = 2, text = 'Update', command = update)
btn_update.grid(row = 8, column = 1, padx = (15,0), pady = (45,10), sticky = 'w')
btn_delete = Button(master, width = 12, height = 2, text = 'Delete', command = delete)
btn_delete.grid(row = 8, column = 2, padx = (15,0), pady = (45,10), sticky = 'w')
btn_close = Button(master, width = 12, height = 2, text = 'Close', command =close)
btn_close.grid(row = 8, column = 3, padx = (15,0), pady = (45,10), sticky = 'e')
mainloop()
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)
print(len(rows))

