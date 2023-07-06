from tkinter import *
import os
import cv2
import numpy as np
import pytesseract
from tkinter import filedialog
# Read image
a=Tk()
a.geometry('500x500')
a.title("Form")
f=filedialog.askopenfilename(initialdir="F:/guicar/",title="select image",filetype=[("png files",".jpg"),("all files","*.*")])                         
print(f)
if(f!=''):
        img=cv2.imread(f)
        gray = cv2.cvtColor(img, 0)
        cv2.imshow('img', gray)
        cv2.waitKey(0)
#read haarcascade
#plates_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml') #does not give me error, but result is not correct
plates_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml') #gives me error
plates = plates_cascade.detectMultiScale(gray, 1.2, 4)


for (x,y,w,h) in plates:

    #detect plate with rectangle
    #rec. start point (x,y), rec. end point (x+w, y+h), blue color(255,0,0), line width 1

    plates_rec = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 1)        
    #cv2.putText(plates_rec, 'Text', (x, y-3), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

    gray_plates = gray[y:y+h, x:x+w]
    color_plates = img[y:y+h, x:x+w]


    #cv2.imshow('img', gray_plates)
    #cv2.waitKey(0)

    height, width, chanel = gray_plates.shape
    print(height, width)

cv2.imshow('img', img)

pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract'

text=pytesseract.image_to_string(gray_plates,lang='eng')

Label(a,text=text,fg="green", font=('arial', 14), bd=5).pack()
print(text)
def fix():
        os.system("python car.py")
Button(a, text='Back', width=20,fg="green",bg="black",bd=5,font=('arial',12),command=fix).pack()

cv2.waitKey(0)
a.mainloop()
