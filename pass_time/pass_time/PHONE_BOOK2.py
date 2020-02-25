import tkinter
from tkinter import *
import sqlite3 as lite
import sys

con = lite.connect('users123.db')
class phonebook(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        self.master = master
        #self.Firstname=""

        self.Firstname = StringVar()
        self.Lastname = StringVar()
        self.Phone = StringVar()
        self.email = StringVar()
        self.load_gui()
        self.load_db()
        self.display_list()

    def load_db(self):
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Users(FirstName TEXT, LastName TEXT, Phone INT, Email TEXT)")

    def display_list(self):
        with con:
            rows=[]
            cur=con.cursor()
            cur.execute("SELECT * FROM users")
            rows = cur.fetchall()
        self.lstList1=Listbox(self.master,width=40)
        for i in range(0,len(rows)):
            self.lstList1.insert(END,rows[i][0:2])
        self.lstList1.grid(row = 1, column = 2, rowspan = 7, columnspan = 3, sticky = 'nsew')


    def onClear(self):
    #clears the textboxes
        self.txt_Firstname.delete(0,END)
        self.txt_Lastname.delete(0,END)
        self.txt_Phone.delete(0,END)
        self.txt_email.delete(0,END)

    def add(self):
        for item in [self.txt_Firstname.get(),self.txt_Lastname.get(),self.txt_Phone.get(),self.txt_email.get()]:
            self.lstList1.insert(END,str(item))
        with con:
            cur = con.cursor()
        cur.execute("INSERT INTO Users VALUES(?,?,?,?)",((self.txt_Firstname.get()),(self.Lastname.get()),(self.Phone.get()),(self.email.get())))
        con.commit()
        cur.execute("SELECT * FROM Users")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        

    def on_close(self):
        self.master.destroy() #Closes
       
    def update(self):
        with con:
            cur=con.cursor()
            cur.execute("UPDATE users SET Lastname=?,Phone=?,email=? where Firstname=?",((self.Firstname.get()),(self.Lastname.get()),(self.Phone.get()),(self.email.get())))
            con.commit()

        
    def load_gui(self):
    #setting up gui labels
        self.lbl_fname = Label(self.master, text = 'First Name: ')
        self.lbl_fname.grid(row = 0, column = 0, padx = (27,0), pady = (10,0), sticky = 'nw')
        self.lbl_lname = Label(self.master, text = 'Last Name: ')
        self.lbl_lname.grid(row = 2, column = 0, padx = (27,0), pady = (10,0), sticky = 'nw')
        self.lbl_phone = Label(self.master, text = 'Phone: ')
        self.lbl_phone.grid(row = 4, column = 0, padx = (27,0), pady = (10,0), sticky = 'nw')
        self.lbl_email = Label(self.master, text = 'Email: ')
        self.lbl_email.grid(row = 6, column = 0, padx = (27,0), pady = (10,0), sticky = 'nw')
        self.lbl_user = Label(self.master, text = 'User: ')
        self.lbl_user.grid(row = 0, column = 2, padx = (0,0), pady = (10,0), sticky = 'nw')
        #setting up gui entry fields
        self.txt_Firstname = Entry(self.master, text = self.Firstname)
        self.txt_Firstname.grid(row = 1, column = 0, columnspan = 2, padx = (30,40), pady = (0,0), sticky = 'new')
        self.txt_Lastname = Entry(self.master, text = self.Lastname)
        self.txt_Lastname.grid(row = 3, column = 0, columnspan = 2, padx = (30,40), pady = (0,0), sticky = 'new')
        self.txt_Phone = Entry(self.master, text = self.Phone)
        self.txt_Phone.grid(row = 5, column = 0, columnspan = 2, padx = (30,40), pady = (0,0), sticky = 'new')
        self.txt_email = Entry(self.master, text = self.email)
        self.txt_email.grid(row = 7, column = 0, columnspan = 2, padx = (30,40), pady = (0,0), sticky = 'new')
         #setting up listbox and the scrollbar
        self.scrollbar1 = Scrollbar(self.master, orient = VERTICAL)
        self.lstList1 = Listbox(self.master, exportselection = 0)
        #self.lstList1.bind('<<ListboxSelect>>', self.on_select)
        #self.scrollbar1.config(command = self.lstList1.yview)
        self.scrollbar1.grid(row = 1, column = 5, rowspan = 7, sticky = 'nes')
        self.lstList1.grid(row = 1, column = 2, rowspan = 7, columnspan = 3, sticky = 'nsew')
        #setting up buttons
        self.btn_add = Button(self.master, width = 12, height = 2, text = 'Add', command = self.add)
        self.btn_add.grid(row = 8, column = 0, padx = (25,0), pady = (45,10), sticky = 'w')
        self.btn_update = Button(self.master, width = 12, height = 2, text = 'Update', command = self.update)
        self.btn_update.grid(row = 8, column = 1, padx = (15,0), pady = (45,10), sticky = 'w')
        self.btn_delete = Button(self.master, width = 12, height = 2, text = 'Clear', command = lambda: self.onClear())
        self.btn_delete.grid(row = 8, column = 2, padx = (15,0), pady = (45,10), sticky = 'w')
        self.btn_close = Button(self.master, width = 12, height = 2, text = 'Close', command = self.on_close)
        self.btn_close.grid(row = 8, column = 3, padx = (15,0), pady = (45,10), sticky = 'e')
if __name__ == "__main__":
    root = Tk()
    ph = phonebook(root)
    root.mainloop()
