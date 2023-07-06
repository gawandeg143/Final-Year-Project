# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:00:28 2020

@author: Lenovo
"""
from tkinter import *
import pymysql
import os
root=Tk()
root.geometry('500x500')

lbl_title = Label(root, text = "Car NumberPlate Detection",fg="red", font=('arial', 16))
lbl_title.place(x=120,y=60)

def reg():
    os.system("python registration.py")
    
   
btn1=Button(root, text="Register Car", width=20,fg="black",bd=5,font=('arial',12),command=reg)
btn1.place(x=80,y=120)
btn2=Button(root, text="Recognize Name", width=20,fg="black",bd=5,font=('arial',12))
btn2.place(x=300,y=120)



btn3=Button(root, text="View Car", width=20,fg="black",bd=5,font=('arial',12))
btn3.place(x=80,y=200)
btn4=Button(root, text="Live stream", width=20,fg="black",bd=5,font=('arial',12))
btn4.place(x=300,y=200)
def load():
    os.system("python loadimage.py")
btn5=Button(root, text="Load Image", width=20,fg="black",bd=5,font=('arial',12),command=load)
btn5.place(x=170,y=270)

    
root.mainloop()