# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 17:55:30 2020

@author: Lenovo
"""

from tkinter import *

import pymysql
import os



root = Tk()
root.geometry('500x500')
root.title("Registration Form")

mydb=pymysql.connect(host="localhost",user="root",password="root",database="carreg")
mycursor=mydb.cursor()
NAME = StringVar()
EMAIL= StringVar()
CONTACT= StringVar()
VEVICAL= StringVar()
def regg():
        nam=n1.get()
        ema=n2.get()
        con=n3.get()
        veh=n4.get()
        sql="insert into user (name,email,contact,vname)values(%s,%s,%s,%s)"
        values=(nam,ema,con,veh)
        mycursor.execute(sql,values)
        mydb.commit()
lbl_title = Label(root, text = "Registration Page",fg="green", font=('arial', 16))
lbl_title.pack(fill=X)




n11 = Label(root, text = " OWNER NAME    :",fg="green", font=('arial', 14), bd=5)
n11.pack()
n1 = Entry(root, textvariable=NAME, font=(14),bd=5)
n1.pack()
n12 = Label(root, text = "OWNER EMAIL    :",fg="green",font=('arial', 14), bd=5)
n12.pack()
n2 = Entry(root, textvariable=EMAIL, font=(14),bd=5)
n2.pack()
n13 = Label(root, text = "OWNER CONTACT    :",fg="green", font=('arial', 14), bd=5)
n13.pack()
n3 = Entry(root, textvariable=CONTACT, font=(14),bd=5)
n3.pack()
n14 = Label(root, text = "VEHICLE NAME    :",fg="green", font=('arial', 14), bd=5)
n14.pack()
n4 = Entry(root, textvariable=VEVICAL, font=(14),bd=5)
n4.pack()


btn=Button(root, text="Register", width=20,fg="green",bg="black",bd=5,font=('arial',12),command=regg)
btn.pack()
def fix():
        os.system("python car.py")
Button(root, text='Back', width=20,fg="green",bg="black",bd=5,font=('arial',12),command=fix).pack()

root.mainloop()

