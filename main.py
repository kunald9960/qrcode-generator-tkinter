from tkinter import *
import tkinter as tk
import os
from tkinter import messagebox
import pyqrcode

window=tk.Tk()
window.title("QR Code Generator")
window.geometry("720x400")

def generate():
    if len(Subject.get())!=0 :
        global qr,photo
        qr= pyqrcode.create(Subject.get())
        photo= BitmapImage(data=qr.xbm(scale=8))
    else:
        messagebox.showinfo("Please enter some subject")
    try:
        showcode()
    except:
        pass

def showcode():
    imageLabel.config(image= photo)
    subLabel.config(text="QR of " + Subject.get())

def save():
    dir= os.getcwd()+ "\\QR Codes"
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get())!=0:
            qr.png(os.path.join(dir,name.get()+ ".png"),scale=8)
        else:
            messagebox.showinfo("Enter a file name")
    except:
        messagebox.showinfo("Generate QR code first")

heading_title=tk.Label(text='QR Code Generator',bg='#D7E9F7',font=('poppins,sans-serif',30))
heading_title.place(x=180,y=18)        

Sub= Label(window,text="Enter subject: ",font=('poppins,sans-serif',18))
Sub.grid(row=1,column=0,sticky='W')

FName= Label(window,text="Enter file name: ",font=('poppins,sans-serif',18))
FName.grid(row=2,column=0,sticky='W')

Subject= StringVar()
SubEntry= Entry(window,textvariable= Subject,font=('poppins,sans-serif',15))
SubEntry.grid(row=1,column=1,sticky='W')

name= StringVar()
nameEntry= Entry(window,textvariable= name,font=('poppins,sans-serif',15))
nameEntry.grid(row=2,column=1,sticky='W')

button= Button(window,text="Generate",width= 15,font=('poppins,sans-serif',18),command= generate)
button.grid(row=1,column=3)

imageLabel= Label(window)
imageLabel.grid(row=3,column=0,)

subLabel= Label(window,text="")
subLabel.grid(row=4,column=1,)

saveB= Button(window,text="Save as PNG",width=15,font=('poppins,sans-serif',18),command= save)
saveB.grid(row=2,column=3)

Rows = 3
Columns = 3

for row in range(Rows+1):
    window.grid_rowconfigure(row,weight=1)

for col in range(Columns+1):
    window.grid_columnconfigure(col,weight=1)

window.mainloop()