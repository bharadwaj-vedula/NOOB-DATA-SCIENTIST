
"""
Phone book  database storage and retrieval
"""
import tkinter
from tkinter import *
import sqlite3 as lite
import sys
con = lite.connect('phone.db')
class phonebook(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        self.master = master
        self.load_gui()
        self.load_db()

    def load_db(self):
        with con:
            cur = con.cursor()    
            cur.execute("CREATE TABLE IF NOT EXISTS Users(FName TEXT, LName TEXT,Cellno TEXT ,Email TEXT )")
            
    def onClear(self):
    #clears the textboxes
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_phone.delete(0,END)
        self.txt_email.delete(0,END)

    def addToList(self):
        
        self.lstList1.insert(END,str(self.txt_fname.get()))#+str(self.txt_lname.get())))
        with con:
            cur = con.cursor()    
            cur.execute("INSERT INTO Users VALUES(?,?,?,?)",(str(self.txt_fname.get()),str(self.txt_lname.get()),str(self.txt_phone.get()),str(self.txt_email.get())))
            
    def on_select(self):
        with con:
            rows=[]
            cur=con.cursor()
            cur.execute("SELECT * FROM users")
            rows = cur.fetchall()
        self.lstList1=Listbox(self.master,width=40)
        for i in range(0,len(rows)):
            self.lstList1.insert(END,rows[i][0:2])
        self.lstList1.grid(row = 1, column = 2, rowspan = 7, columnspan = 3, sticky = 'nsew')

                

    def on_close(self):
        """
        Closes the window
        """
        self.master.destroy()
        
        
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
        self.txt_fname = Entry(self.master, text = '')
        self.txt_fname.grid(row = 1, column = 0, columnspan = 2, padx = (30,40), pady = (0,0), sticky = 'new')
        self.txt_lname = Entry(self.master, text = '')
        self.txt_lname.grid(row = 3, column = 0, columnspan = 2, padx = (30,40), pady = (0,0), sticky = 'new')
        self.txt_phone = Entry(self.master, text = '')
        self.txt_phone.grid(row = 5, column = 0, columnspan = 2, padx = (30,40), pady = (0,0), sticky = 'new')
        self.txt_email = Entry(self.master, text = '')
        self.txt_email.grid(row = 7, column = 0, columnspan = 2, padx = (30,40), pady = (0,0), sticky = 'new')
        #setting up listbox and the scrollbar
        self.scrollbar1 = Scrollbar(self.master, orient = VERTICAL)
        self.lstList1 = Listbox(self.master, exportselection = 0, yscrollcommand = self.scrollbar1.set)
        self.lstList1.bind('<<ListboxSelect>>', self.on_select)
        self.scrollbar1.config(command = self.lstList1.yview)
        self.scrollbar1.grid(row = 1, column = 5, rowspan = 7, sticky = 'nes')
        self.lstList1.grid(row = 1, column = 2, rowspan = 7, columnspan = 3, sticky = 'nsew')
        #setting up buttons
        self.btn_add = Button(self.master, width = 12, height = 2, text = 'Add', command = lambda: self.addToList())
        self.btn_add.grid(row = 8, column = 0, padx = (25,0), pady = (45,10), sticky = 'w')
        self.btn_update = Button(self.master, width = 12, height = 2, text = 'Update')
        self.btn_update.grid(row = 8, column = 1, padx = (15,0), pady = (45,10), sticky = 'w')
        self.btn_delete = Button(self.master, width = 12, height = 2, text = 'Delete', command = lambda: self.onClear())
        self.btn_delete.grid(row = 8, column = 2, padx = (15,0), pady = (45,10), sticky = 'w')
        self.btn_close = Button(self.master, width = 12, height = 2, text = 'Close', command = lambda:self.on_close())
        self.btn_close.grid(row = 8, column = 4, padx = (15,0), pady = (45,10), sticky = 'e')
if __name__ == "__main__":
    root = Tk()
    ph = phonebook(root)
    root.mainloop()
with con:
    cur = con.cursor() 
    cur.execute("SELECT * FROM Users")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def create_win():
    win=Tk.toplevel(root)
root=tk.Tk()
b=Tk.Button(root,text="",command=create_win)
b.pack()
root.mainloop()
