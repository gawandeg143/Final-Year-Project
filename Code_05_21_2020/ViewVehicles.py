import tkinter as tk
import pymysql
import sys
import os
import gc
from html.parser import HTMLParser
from tkinter.filedialog import askopenfile
from subprocess import Popen
from tkinter import messagebox
import urllib.request
from bs4 import BeautifulSoup

        
mydb=pymysql.connect(host="localhost",user="root",password="root",database="LicencePlate")
mycursor=mydb.cursor()
top1=tk.Tk()
top1.title("View Vehicles")

error1=tk.StringVar()
url= tk.StringVar()

width = 900
height = 350
screen_width = top1.winfo_screenwidth()
screen_height = top1.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
top1.geometry("%dx%d+%d+%d" % (width, height, x, y))
top1.config(bg="grey")




Lb1 = tk.Listbox(top1,width=120,bd=3,font=("arial",12))


mycursor.execute("select * from vehiclesdata")
myresult = mycursor.fetchall()
k=1
for x in myresult:
    data="Owner Name : "+x[1]+" | Owner Contact : "+x[2]+" | Veh Number : "+x[4]+" | Email : "+x[3]
    Lb1.insert(k, data)

Lb1.grid(row=12, column=1)




def search():
    os.system("AdminDashboard.py")
    top1.destroy()
    
          
L= tk.Label(top1, width=30, font=('arial', 20),bg="black",fg="green", text = "   View Vehicles   ",bd=5)
L.grid(row=1,column=1)

L1= tk.Label(top1, width=30,bg="grey",fg="green", text = "  Vehicles Listed Below  ")
L1.grid(row=2,column=1)



ErL1=tk.Label(top1,text="",fg="white",justify=tk.LEFT,padx = 10,bg="grey",textvariable=error1)
ErL1.grid(row=4,column=1)



b6= tk.Button(top1,bg="black",fg="green",text="Exit",bd=8,command=search)
b6.config(width="30")  
b6.grid(row=5,column=1)

top1.mainloop()
