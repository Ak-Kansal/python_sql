from tkinter import *
from PIL import Image,ImageTk 
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from time import *
top=Tk()
top.geometry('1500x700')
top.title('home')
def show():
    t=cal.get()
    print(t)
def time():
    s=strftime('%H:%M:%S %p')
    lt.config(text=s)
    lt.after(1000,time)

img=ImageTk.PhotoImage(Image.open(r"c:\Users\DELL\Desktop\Yoga.jpg"))
L=Label(top,image=img)
L.pack()
L1=Label(top,text='registration',fg='white', bg='green',font=('arial',20,'bold'))
L1.place(x=600,y=30)
L1=Label(top,text='welcome to the home page',fg='white', bg='green',font=('arial',20,'bold'))
L1.place(x=600,y=30)
lt=Label(top,width=20,font=('arial',20,'bold'))
lt.place(x=600,y=100)
time()
cal=DateEntry(top,width=12,background='darkblue',foreground='white',borderwidth=2,year=2010)
cal.place(x=600,y=200)
b=Button(top,text='submit',command=show)
b.place(x=600,y=250)
top.mainloop()

