# tkinter is an inbuild library used to develop window based applications
from tkinter import *
from PIL import Image,ImageTk 
from tkinter import messagebox
from tkinter import ttk
top=Tk()
top.geometry('1500x700')
top.title('registration')
top.iconbitmap(r"c:\Users\DELL\Desktop\chatgpt_logo_chatgpt_logo_square_green_gpt_ia_openai_icon_264977.ico")
def showpassword():
    if e4.cget('show')=="*":
        e4.config(show='')
    else:
        e4.config(show='*')
def insert():
    k=e1.get()
    k2=int(e2.get())
    k3=int(e3.get())
    k4=e4.get()
    k5=e5.get()
    import pymysql as sql 
    db=sql.connect(host='localhost',user='root',password='Mysql2024',database='project')
    cursor=db.cursor()
    s="insert into emp values('%s','%s','%s','%s','%s')"%(k,k2,k3,k4,k5)
    result=cursor.execute(s)
    if(result>0):
        messagebox.showinfo('result','data inserted successfully')
    else:
        messagebox.showinfo('result','data not inserted')
    db.commit()
    e1.delete(0,'end')
    e2.delete(0,'end')
    e3.delete(0,'end')
    e4.delete(0,'end')
    e5.delete(0,'end')
    
def delete():
    k=e1.get()
    import pymysql as sql 
    db=sql.connect(host='localhost',user='root',password='Mysql2024',database='project')
    cursor=db.cursor()
    s="delete from emp where name=%s"
    result=cursor.execute(s,k)
    if(result>0):
        messagebox.showinfo('result','data deleted successfully')
    else:
        messagebox.showinfo('result','data not deleted')
    db.commit()
def search():
    k=e1.get()
    import pymysql as sql 
    db=sql.connect(host='localhost',user='root',password='Mysql2024',database='project')
    cursor=db.cursor()
    s="select * from emp where name=%s"
    t=cursor.execute(s,k)
    result=cursor.fetchall()
    if(t>0):
        for col in result:
            name=col[0]
            age=col[1]
            contact=col[2]
            password=col[3]
            email=col[4]
            print(name,age,contact,password,email)
    else:
        messagebox.showinfo('result','record not found')
    db.commit()
def show():
    import pymysql as sql 
    db=sql.connect(host='localhost',user='root',password='Mysql2024',database='project')
    cursor=db.cursor()
    s="select * from emp"
    t=cursor.execute(s)
    result=cursor.fetchall()
    if(t>0):
        for col in result:
            name=col[0]
            age=col[1]
            contact=col[2]
            password=col[3]
            email=col[4]
            tv.insert("",'end',values=(name,age,contact,password,email))
            # print(name,age,contact,password,email)
    else:
        messagebox.showinfo('result','record not found')
    db.commit()
def Login():
    # top.destroy() #this will close the back page and only shows the new page
    # import login
    import os
    os.system('python login.py') #this will show both the pages without closing the first page
img=ImageTk.PhotoImage(Image.open(r"c:\Users\DELL\Desktop\Yoga.jpg"))
L=Label(top,image=img)
L.pack()
tv = ttk.Treeview(top)
tv['columns']=('name', 'age','contact','password','email')
tv.column('#0', width=0, stretch=NO)
tv.column('name', anchor=CENTER, width=100)
tv.column('age', anchor=CENTER, width=100)
tv.column('contact', anchor=CENTER, width=100)
tv.column('password', anchor=CENTER, width=100)
tv.column('email', anchor=CENTER, width=100)
tv.heading('name', text='name', anchor=CENTER)
tv.heading('age', text='age', anchor=CENTER)
tv.heading('contact', text='contact', anchor=CENTER)
tv.heading('password', text='password', anchor=CENTER)
tv.heading('email', text='email', anchor=CENTER)
tv.place(x=850,y=150)
L1=Label(top,text='registration',fg='white', bg='green',font=('arial',20,'bold'))
L1.place(x=600,y=30)
L2=Label(top,text='name',fg='white',bg='green',font=('arial',20,'bold'))
L2.place(x=300,y=200)
e1=Entry(top,font=('arial',20,'bold'))
e1.place(x=450,y=200)
L3=Label(top,text='age',fg='white',bg='green',font=('arial',20,'bold'))
L3.place(x=300,y=250)
e2=Entry(top,font=('arial',20,'bold'))
e2.place(x=450,y=250)
L4=Label(top,text='contact',fg='white',bg='green',font=('arial',20,'bold'))
L4.place(x=300,y=300)
e3=Entry(top,font=('arial',20,'bold'))
e3.place(x=450,y=300)
L5=Label(top,text='password',fg='white',bg='green',font=('arial',20,'bold'))
L5.place(x=300,y=350)
e4=Entry(top,font=('arial',20,'bold'),show="*")
e4.place(x=450,y=350)
L6=Label(top,text='email',fg='white',bg='green',font=('arial',20,'bold'))
L6.place(x=300,y=400)
e5=Entry(top,font=('arial',20,'bold'))
e5.place(x=450,y=400)
B1=Button(top,text="submit",font=('arial',20,'bold'),command=insert)
B1.place(x=450,y=450)
B2=Button(top,text="delete",font=('arial',20,'bold'),command=delete)
B2.place(x=600,y=450)
B3=Button(top,text="search",font=('arial',20,'bold'),command=search)
B3.place(x=750,y=450)
B4=Button(top,text="show",font=('arial',20,'bold'),command=show)
B4.place(x=900,y=450)
B5=Button(top,text="login",font=('arial' ,20, 'bold'),command=Login)
B5.place(x=1000,y=450)
c1=Checkbutton(top,command=showpassword)
c1.place(x=800,y=350)
#top.config(bg='green')
top.mainloop()