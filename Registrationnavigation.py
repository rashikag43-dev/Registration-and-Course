import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
t=tkinter.Tk()
t.geometry('800x800') 
xa=[]
xb=[]
xc=[]
xd=[]
xe=[]
i=0
def filldata():
    global xa,xb,xc,xd,xe
    db=pymysql.connect(host='localhost',user='root',password='root',database='my56')
    cur=db.cursor()
    sql="select * from Registration"
    cur.execute(sql)
    data=cur.fetchall()
    for m in data:
        xa.append(m[0])
        xb.append(m[1])
        xc.append(m[2])
        xd.append(m[3])
        xe.append(m[4])
    db.close()
def firstdata():
    global xa,xb,xc,xd,xe
    i=0
    ea.delete(0,END)
    eb.delete(0,END)
    ec.delete(0,END)
    ed.delete(0,END)
    ee.delete(0,END)
    ea.insert(0,xa[i])
    eb.insert(0,xb[i])
    ec.insert(0,xc[i])
    ed.insert(0,xd[i])
    ee.insert(0,xe[i])
def nextdata():
    global xa,xb,xc,xd,xe,i
    i=i+1
    ea.delete(0,END)
    eb.delete(0,END)
    ec.delete(0,END)
    ed.delete(0,END)
    ee.delete(0,END)
    ea.insert(0,xa[i])
    eb.insert(0,xb[i])
    ec.insert(0,xc[i])
    ed.insert(0,xd[i])
    ee.insert(0,xe[i])
def previousdata():
    global xa,xb,xc,xd,xe,i
    i=i-1
    ea.delete(0,END)
    eb.delete(0,END)
    ec.delete(0,END)
    ed.delete(0,END)
    ee.delete(0,END)
    ea.insert(0,xa[i])
    eb.insert(0,xb[i])
    ec.insert(0,xc[i])
    ed.insert(0,xd[i])
    ee.insert(0,xe[i])
def lastdata():
    global xa,xb,xc,xd,xe,i
    i=len(xa)-1
    ea.delete(0,END)
    eb.delete(0,END)
    ec.delete(0,END)
    ed.delete(0,END)
    ee.delete(0,END)
    ea.insert(0,xa[i])
    eb.insert(0,xb[i])
    ec.insert(0,xc[i])
    ed.insert(0,xd[i])
    ee.insert(0,xe[i])
a=Label(t,text='regno')
a.place(x=50,y=50)
ea=Entry(t,width=20)
ea.place(x=400,y=50)
b=Label(t,text='name')
b.place(x=50,y=90)
eb=Entry(t,width=20)
eb.place(x=400,y=90)
c=Label(t,text='email')
c.place(x=50,y=130)
ec=Entry(t,width=20)
ec.place(x=400,y=130)
d=Label(t,text='phone')
d.place(x=50,y=170)
ed=Entry(t,width=20)
ed.place(x=400,y=170)
e=Label(t,text='courseid')
e.place(x=50,y=200)
ee=Entry(t,width=20)
ee.place(x=400,y=200)
btn=Button(t,text='First',command=firstdata)
btn.place(x=200,y=400)
btn1=Button(t,text='Last',command=lastdata)
btn1.place(x=350,y=400)
btn2=Button(t,text='Next',command=nextdata)
btn2.place(x=500,y=400)
btn3=Button(t,text='Previous',command=previousdata)
btn3.place(x=650,y=400)
filldata()
t.mainloop()
