import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
t=tkinter.Tk()
t.geometry("700x600")
def deletedata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='my56')
    cur=db.cursor()
    xa=int(ea.get())
    sql="delete from courses where courseid=%s"
    cur.execute(sql,(xa))
    db.commit()
    messagebox.showinfo('Hi','Data Deleted')
    ea.delete(0,END)
    db.close()
a=Label(t,text='courseid')
a.place(x=50,y=50)
ea=Entry(t,width=20)
ea.place(x=400,y=50)
b=Label(t,text='coursename')
b.place(x=50,y=90)
eb=Entry(t,width=20)
eb.place(x=400,y=90)
c=Label(t,text='durationindays')
c.place(x=50,y=130)
ec=Entry(t,width=20)
ec.place(x=400,y=130)
d=Label(t,text='fees')
d.place(x=50,y=170)
ed=Entry(t,width=20)
ed.place(x=400,y=170)
bt=Button(t,text='delete',command=deletedata)
bt.place(x=50,y=400)
t.mainloop()