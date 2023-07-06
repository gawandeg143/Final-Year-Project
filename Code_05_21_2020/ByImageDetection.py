import tkinter as tk
import pymysql
import sys
import os
import gc
from tkinter.filedialog import askopenfile
from subprocess import Popen
from tkinter import messagebox
import cv2
import numpy as np
import pytesseract
from tkinter import filedialog
        
mydb=pymysql.connect(host="localhost",user="root",password="root",database="LicencePlate")
mycursor=mydb.cursor()
top1=tk.Tk()
top1.title("View Vehicles")

error1=tk.StringVar()
url= tk.StringVar()

width = 500
height = 350
screen_width = top1.winfo_screenwidth()
screen_height = top1.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
top1.geometry("%dx%d+%d+%d" % (width, height, x, y))
top1.config(bg="grey")

#----------------------Number Plate Recognisation using Images
f=filedialog.askopenfilename(initialdir="F:/guicar/",title="select image",filetype=[("png files",".jpg"),("all files","*.*")])                         
print(f)

if(f!=''):
    img=cv2.imread(f)
    gray = cv2.cvtColor(img, 0)
    cv2.imshow('img', gray)
    
plates_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml') #gives me error
plates = plates_cascade.detectMultiScale(gray, 1.2, 4)
for (x,y,w,h) in plates:
    plates_rec = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 1)
    gray_plates = gray[y:y+h, x:x+w]
    color_plates = img[y:y+h, x:x+w]
    height, width, chanel = gray_plates.shape
    print(height, width)

cv2.imshow('img', img)
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract'
text=pytesseract.image_to_string(gray_plates,lang='eng')
v = tk.StringVar()
print(text)
text=text.replace(" ","")
v.set(text)




name=tk.StringVar()
contact=tk.StringVar()
email=tk.StringVar()


mycursor.execute("select * from vehiclesdata where vehnumber=%s",text)
myresult = mycursor.fetchall()
isfound="0"
for x in myresult:
    name.set("Owner Name : "+x[1])
    contact.set("Owner Contact : "+x[2]) 
    email.set("Email : "+x[3])
    isfound="1"
    
if(isfound=="0"):
    name.set("Name : Not Found")
    contact.set("Contact : Not Found")
    email.set("Email : Not Found")
    
    

def search():
    mycursor.execute("select * from vehiclesdata where vehnumber=%s",E11.get())
    myresult = mycursor.fetchall()
    for x in myresult:
        data="Owner Name : "+x[1]+" | Owner Contact : "+x[2]+" | Veh Number : "+x[4]+" | Email : "+x[3]
        #print(data)
        name.set("Owner Name : "+x[1])
        contact.set("Owner Contact : "+x[2])
        email.set("Email : "+x[3])
    
        
          
L= tk.Label(top1, width=30, font=('arial', 20),bg="black",fg="green", text = "   View Vehicles   ",bd=5)
L.grid(row=1,column=1)

L1= tk.Label(top1, width=30,bg="grey",fg="green", text = "  Vehicles Listed Below  ")
L1.grid(row=2,column=1)


E11=tk.Entry(top1,font=(14),bd=5,textvariable=v)
E11.grid(row=3,column=1)


ErL1=tk.Label(top1,text="",fg="white",justify=tk.LEFT,padx = 10,bg="grey")
ErL1.grid(row=4,column=1)



b6= tk.Button(top1,bg="black",fg="green",text="Exit",bd=8,command=search)
b6.config(width="30")  
b6.grid(row=5,column=1)


name1=tk.Label(top1,text="",fg="white",justify=tk.LEFT,padx = 10,bg="grey",font=('arial', 15),textvariable=name)
name1.grid(row=6,column=1)

contact1=tk.Label(top1,text="",fg="white",justify=tk.LEFT,padx = 10,bg="grey",font=('arial', 15),textvariable=contact)
contact1.grid(row=7,column=1)

email1=tk.Label(top1,text="",fg="white",justify=tk.LEFT,padx = 10,bg="grey",font=('arial', 15),textvariable=email)
email1.grid(row=8,column=1)






top1.mainloop()
