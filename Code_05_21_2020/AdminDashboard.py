import tkinter as tk
import pymysql
import sys
import os
import gc
from tkinter.filedialog import askopenfile
from subprocess import Popen
from tkinter import messagebox
from subprocess import call
mydb=pymysql.connect(host="localhost",user="root",password="root",database="maliciousurl")
mycursor=mydb.cursor()

top1=tk.Tk()
top1.title("Admin Dashboard")
width = 1300
height = 700
screen_width = top1.winfo_screenwidth()
screen_height = top1.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
top1.geometry("%dx%d+%d+%d" % (width, height, x, y))
top1.config(bg="#129876")


def addvehicle():
    call('python AddVehicle.py', shell=True)
    #os.system("ViewUsers.py")
def addvehicle():
    call('python AddVehicle.py', shell=True)
    #os.system("ViewUsers.py")
def viewvehicles():
    call('python ViewVehicles.py', shell=True)
    #os.system("ViewAllSearches.py")
def addkeyword():
    call('python AddWordDictionary.py', shell=True)
    #os.system("AddWordDictionary.py")
def searchvehicle():
    call('python ByImageDetection.py', shell=True)
    #os.system("loadimage.py")
def cardetection():
    call('python Vehicles_detection.py', shell=True)
    #print("Click")
    #os.system("loadimage.py")
def logout():
    top1.destroy()
    call('python index.py', shell=True)
    #os.system("index.py")
    
        



    
L= tk.Label(top1, width=30, font=('arial', 20),bg="black",fg="green", text = "   Licence Plate Recognisation & Verification",bd=5)
L.grid(row=1,column=1)
L= tk.Label(top1, width=30, font=('arial', 20),bg="black",fg="red", text = "--Easy and quick search",bd=5)
L.grid(row=1,column=2)
L= tk.Label(top1, width=30, font=('arial', 20),bg="black",fg="green", text = "",bd=5)
L.grid(row=1,column=3)

photo = tk.PhotoImage(file = r"D:\Abstract and Details 2017\Licence Plate Recognisation using Python\images\addvehicle.png")
photoimage = photo.subsample(4, 4) 
b2= tk.Button(top1,bg="white",fg="green",text="Add Vehicle",bd=8,command=addvehicle,image = photoimage,compound ="top")  
b2.config(width="100")
b2.config(height="100")
b2.grid(row=2,column=1,padx=30,pady=30)


photo2 = tk.PhotoImage(file = r"D:\Abstract and Details 2017\Licence Plate Recognisation using Python\images\viewregister.png")
photoimage2 = photo2.subsample(4, 4) 
b3= tk.Button(top1,bg="white",fg="green",text="View All Vehicles",bd=8,command=viewvehicles,image = photoimage2,compound ="top" )
b3.config(width="100")
b3.config(height="100")  
b3.grid(row=2,column=2)


photo3 = tk.PhotoImage(file = r"D:\Abstract and Details 2017\Malicious URL detection System Python\images\addword.png")
photoimage3 = photo3.subsample(4, 4) 
b4= tk.Button(top1,bg="white",fg="green",text="Verify Licence Live",bd=8,command=searchvehicle,image = photoimage3,compound ="top")
b4.config(width="100")
b4.config(height="100") 
b4.grid(row=4,column=1)


photo4 = tk.PhotoImage(file = r"D:\Abstract and Details 2017\Malicious URL detection System Python\images\blacklink.png")
photoimage4 = photo4.subsample(4, 4)
b5= tk.Button(top1,bg="white",fg="green",text="Car Detection",bd=8,command=cardetection,image = photoimage4,compound ="top" )
b5.config(width="100")
b5.config(height="100")   
b5.grid(row=4,column=2)


photo5 = tk.PhotoImage(file = r"D:\Abstract and Details 2017\Malicious URL detection System Python\images\viewuser.png")
photoimage5 = photo5.subsample(4, 4)
b6= tk.Button(top1,bg="white",fg="green",text="Search Vehicles",bd=8,command=searchvehicle,image = photoimage5,compound ="top"  )
b6.config(width="100")
b6.config(height="100")  
b6.grid(row=2,column=3)

photo6 = tk.PhotoImage(file = r"D:\Abstract and Details 2017\Malicious URL detection System Python\images\logout.png")
photoimage6 = photo6.subsample(4, 4)
b7= tk.Button(top1,bg="white",fg="green",text="Log Out",bd=8,command=logout,image = photoimage6,compound ="top"  )
b7.config(width="100")
b7.config(height="100")  
b7.grid(row=4,column=3)

top1.mainloop()
