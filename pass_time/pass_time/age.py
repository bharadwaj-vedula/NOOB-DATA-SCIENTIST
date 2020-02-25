import tkinter
from tkinter import *
import datetime as dt

x=dt.datetime.now().date()
print(x)
print(type(x))

y=dt.datetime(2020,2,27).date()

print(y-x)


win=tkinter.Tk()
win.geometry("480x480")
win.title("AGE CALCULATOR")
year=StringVar()
month=StringVar()
day=StringVar()
dob=""

def cal():
    dob=dt.date(int(year.get()),int(month.get()),int(day.get()))
    display_date=dob-x
    print(display_date)
    newwin=Toplevel(win)
    newwin.title("new window ")
    newwin.geometry("360x360")
    Label(newwin,text="the age is ").grid(row=0,column=0)
    Label(newwin,text=display_date).grid(row=0,column=1)

Label(win,text="enter your year").grid(row=0,column=0)
e1=Entry(win,textvariable=year).grid(row=1,column=0)

Label(win,text="enter your month").grid(row=2,column=0)
e2=Entry(win,textvariable=month).grid(row=3,column=0)

Label(win,text="enter your day").grid(row=4,column=0)
e1=Entry(win,textvariable=day).grid(row=5,column=0)

b1=Button(win,text="calculate",command=cal).grid(row=6,column=0)


win.mainloop()

print(dob)
