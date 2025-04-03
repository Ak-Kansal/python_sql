from tkinter import *
from PIL import Image,ImageTk 
from tkinter import messagebox
from tkinter import ttk
top=Tk()
top.geometry('1500x700')
top.title('login')
def showpassword():
    if e4.cget('show')=="*":
        e4.config(show='')
    else:
        e4.config(show='*')
def login():
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',passwd='Mysql2024',db='project')
    cur=db.cursor()
    cur.execute("select * from emp where name=%s and password=%s",(e1.get(),e4.get()))
    row=cur.fetchone()

    if row == None:
        messagebox.showinfo('error','login failed')
    else:
        top.destroy()
        import home
img=ImageTk.PhotoImage(Image.open(r"c:\Users\DELL\Desktop\Yoga.jpg"))
L=Label(top,image=img)
L.pack()
L1=Label(top,text='login',fg='white', bg='green',font=('arial',20,'bold'))
L1.place(x=600,y=30)
L2=Label(top,text='name',fg='white',bg='green',font=('arial',20,'bold'))
L2.place(x=300,y=200)
e1=Entry(top,font=('arial',20,'bold'))
e1.place(x=450,y=200)
L5=Label(top,text='password',fg='white',bg='green',font=('arial',20,'bold'))
L5.place(x=300,y=250)
e4=Entry(top,font=('arial',20,'bold'),show="*")
e4.place(x=450,y=250)
c1=Checkbutton(top,command=showpassword)
c1.place(x=800,y=250)
B5=Button(top,text="login",font=('arial' ,20, 'bold'),command=login)
B5.place(x=450,y=350)
top.mainloop()