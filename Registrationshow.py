import tkinter
from tkinter import *
import pymysql
t=tkinter.Tk()
t.geometry('600x700')
def showdata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='my56')
    cur=db.cursor()
    sql='select*from Registration'
    records=''
    cur.execute(sql)
    data=cur.fetchall()
    for m in data:
        records=str(records)+str(m)+'\n'
    db.close()
    ta.insert("1.0",records)
ta=Text(t,width=90,height=20)
ta.place(x=50,y=50)
btn=Button(t,text='Showdata',command=showdata)
btn.place(x=200,y=300)
t.mainloop()
