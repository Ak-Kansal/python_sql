from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk

top = Tk()
top.geometry("1500x800")
top.title("COFFEE SHOP")
top.iconbitmap(r"c:\Users\DELL\Downloads\coffee_icon-icons.com_50414.ico")
top.configure(bg="black")

f1 = Frame(top, width=1500, height=100, bg="white") 
f1.place(x=0, y=10)
f2 = Frame(top, width=740, height=475, bg="white")
f2.place(x=0, y=115)
f3 = Frame(top, width=1500, height=95, bg="white")
f3.place(x=0, y=595)
f4 = Frame(top, width=740, height=475, bg="chocolate")
f4.place(x=750, y=115)
image = Image.open(r"C:\Users\DELL\Desktop\coffee.jpg")
resized_image = image.resize((740, 471))
img = ImageTk.PhotoImage(resized_image)
L = Label(f2, image=img)
L.pack()
image=Image.open(r"C:\Users\DELL\Desktop\python\coffee_proj\heading.jpg")
resized_image=image.resize((1500,95))
img1=ImageTk.PhotoImage(resized_image)
L=Label(f1,image=img1)
L.pack()
Lhead=Label(f1,text="Velvet Bean",font=("arial",30,"bold"),bg="white smoke")
Lhead.place(x=580,y=30)
Lreg=Label(f4,text="Register Now",font=("arial",30,"bold"))
Lreg.place(x=200,y=10)
Lname=Label(f4,text="Name",font=("arial",20,"bold"))
Lname.place(x=100,y=100)
ename=Entry(f4,font=("arial",20,"bold"),bg="white")
ename.place(x=250,y=100)
top.mainloop()