from atexit import register
from cgitb import text
from cmath import log
from logging import root
from re import A
from tkinter import *
from turtle import down
from PIL import Image,ImageTk
import tkinter as tk
import datetime
# import os                                                            
# import sys 
import pymysql
import messagebox 
from functools import partial
# import register
from tkinter import ttk
import random
def Log():
    username1=username.get()  
    password1=password.get()
    if username1 == "" or password1 == "":
        messagebox.showerror("Error", "All Fields are Required")
    else:
        con = pymysql.connect(host='localhost', user='root', password='', database='airport_management_system')
        cur = con.cursor()  
        cur.execute('select * from registration where Username =%s and Password =%s',(username1,password1))
        row = cur.fetchone()
        if row == None:
            messagebox.showinfo('Error', 'Invalid username and password')
        elif cmb.get() == row[5]:
            if cmb.get() == "Admin":
                loginsc.destroy()
                admain()
            if cmb.get() == "Standard User":
                loginsc.destroy()
                stamain()
            if cmb.get()   == "Supervisor":
                loginsc.destroy()
                supmain()
            messagebox.showinfo('Success', 'Login Successfully')
            con.commit()
            con.close()  
def flightdata(): 
    conn = pymysql.connect(host = "localhost",user = "root",password="",db   = "airport_management_system")
    cur = conn.cursor()
    f=flightnumber.get()
    t=timing.get()
    d=destination.get()
    c=source.get()
    s=status.get()
    args = (f,t,d,c,s)
    sql =   "insert into viewflights(flightnumber,timing,destination,source,status) values(%s, %s, %s, %s, %s)"
    try:
        cur.execute(sql, args)
        messagebox.showinfo("success","inserted successfully")
    except Exception as e: 
         messagebox.showerror("error",f"error due to {e}")
        # print("Something is wrong")
    conn.commit()
    conn.close() 
def getticket(): 
    conn = pymysql.connect(host = "localhost",user = "root",password="",db   = "airport_management_system")
    cur = conn.cursor()
    p=passengername.get()
    m=mobileno.get()
    i=flinumber.get()
    o=sourcee.get()
    a=destinationn.get()
    v=getseat.cget("text")

    args = (p,m,i,o,a,v)
    sql = "insert into book_ticket(passengername,mobileno,flinumber,sourcee,destinationn,getseat) values(%s, %s, %s, %s, %s, %s) "
    try:
        cur.execute(sql, args)
        messagebox.showinfo("success","ticket booked")
    except Exception as e: 
        messagebox.showerror("error",f"error due to {e}")
        # print("Something is wrong")
    conn.commit()
    conn.close()  
global Fetch2
def Fetch2():
    conn=pymysql.connect(host='localhost', user='root', password='', database='airport_management_system')
    cur= conn.cursor()
    x= seat.get()
    args = (x)
    sql="SELECT * from book_ticket where getseat=%s"
    cur.execute(sql% args)
    h=cur.fetchall()
    for i in h:
       print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4])
    #   print(h)
       conn.close() 
def insertfun():
    conn = pymysql.connect(host = "localhost",user = "root",password="",db   = "airport_management_system")
    cur = conn.cursor()
    n = firstname.get()
    l = lastname.get()
    u = username.get()
    e = email.get()
    p = password.get()
    r = cmb.get()
    print(r)
    args = (n,l,u,e,p,r)
    sql = "insert into registration(f_name,l_name,Username,Email,Password,role) values(%s, %s, %s, %s, %s, %s)"
    try:
        cur.execute(sql, args)
        messagebox.showinfo("success","inserted successfully")
        conn.commit()
        conn.close()
        # main.login()

    except Exception as e:
        messagebox.showerror("error",f"error due to {e}")
def update():    
      global updatesc,flightnumber,timing,destination,source,status,w,h
      updatesc=Tk()       
      updatesc.title("Add A Flight") 
      updatesc.geometry("600x550") 
      updatesc.configure(bg='purple')   
      flightnumber = Label(updatesc, text="Enter flight number").grid(row=1, column=2)
      flightnumber = StringVar()
      flightnumber = Entry(updatesc, textvariable=flightnumber)
      flightnumber.grid(row=1, column=3)  
      timing = Label(updatesc, text="Enter departure time").grid(row=2, column=2)
      timing = StringVar()
      timing = Entry(updatesc, textvariable=timing)
      timing.grid(row=2, column=3)  
      destination = Label(updatesc, text="Enter destination").grid(row=3, column=2)
      destination = StringVar()
      destination=Entry(updatesc, textvariable=destination)
      destination.grid(row=3, column=3)
      source = Label(updatesc, text="Enter source").grid(row=4, column=2)
      source= StringVar()
      source=Entry(updatesc, textvariable=source)
      source.grid(row=4, column=3) 
      status = Label(updatesc, text="Enter status").grid(row=5, column=2)
      status = StringVar()
      status=Entry(updatesc, textvariable=status)
      status.grid(row=5, column=3)
    #   update=partial(flightdata,flightnumber.get(),timing.get(),destination.get(),source.get(),status.get())  
    #   Button(text="Add",bg="green",fg="white",command=flightdata,cursor="hand2",pady=0).place(x=161,y=220)
      button=tk.Button(updatesc,text="add",command=flightdata)
      button.grid(row=6,column=3)
      updatesc.mainloop()
     
    # #password label and password entry box
    # passwordLabel = Label(loginsc,text="Password").grid(row=2, column=2)  
    # password = StringVar()
    # passwordEntry = Entry(loginsc, textvariable=password, show='*').grid(row=2, column=3)Label = Label(loginsc, text="User Name").grid(row=1, column=2)
    # username = StringVar()
    # usernameEntry = Entry(loginsc, textvariable=username).grid(row=1, column=3)  
    # #password label and password entry box
    # passwordLabel = Label(loginsc,text="Password").grid(row=2, column=2)  
    # password = StringVar()
    # passwordEntry = Entry(loginsc, textvariable=password, show='*').grid(row=2, column=3)   
    # tk.Label(master=updatesc,text="Enter The Flight Number",bg="red",fg="white").grid(row=1,column=0)
    # flightnum=tk.Entry(master=updatesc)
    # flightnum.grid(row=1,column=1)   
    # def updatebutton1():
    #     if flightnum.get() not in scheduled:
    #         scheduled[flightnum.get()]=["","",""]
    #     tk.Label(master=updatesc,text="Enter Departure Time",bg="red").grid(row=3,column=0)
    #     deptime=tk.Entry(master=updatesc)
    #     deptime.grid(row=3,column=1)
    #     tk.Label(master=updatesc,text="Enter Status",bg="pink").grid(row=4,column=0)
    #     status=tk.Entry(master=updatesc)
    #     status.grid(row=4,column=1)
    #     tk.Label(master=updatesc,text="Enter Destination",bg="green").grid(row=5,column=0)
    #     dest=tk.Entry(master=updatesc)
    #     dest.grid(row=5,column=1)
    #     tk.Label(master=updatesc,text="Enter Source",bg="green").grid(row=6,column=0)
    #     source=tk.Entry(master=updatesc)
    #     source.grid(row=6,column=1)

    #     def updatebutton2():       
    #         if deptime.get()!="":
    #             scheduled[flightnum.get()][0]=deptime.get()
    #         if status.get()!="":
    #             scheduled[flightnum.get()][2]=status.get()
    #         if dest.get()!="":
    #             scheduled[flightnum.get()][1]=dest.get()
    #         if source.get()!="":
    #             scheduled[flightnum.get()][3]=source.get()
    #         updatepopup=tk.Tk()
    #         updatepopup.title("Successfully Updated!")
    #         tk.Label(master=updatepopup,text="Successfully Updated!!").grid(row=0,column=0)
    #         updatesc.destroy()           
    #     tk.Button(master=updatesc,text="Confirm",command=updatebutton2).grid(row=7,column=1)   
    # tk.Button(master=updatesc,text="Confirm",command=updatebutton1).grid(row=2,column=1)
# updatesc.mainloop()


def admain():
    #def switchuserad():
        #admainsc.destroy()
    global admainsc
    admainsc=Tk()
    admainsc.geometry('2000x1000') 
    admainsc.title("Admin Control Panel") 
    img = PhotoImage(file="pic.png")
    label = Label(admainsc,image=img)
    label.place(x=0, y=0)
    # admainsc.configure(bg='pink')  
    c11= tk.Button(admainsc,text="View The Details Of Flights",width=25,command=view,bg="red")
    c11.grid(row=1,column=2)
    #c12=tk.Button(admainsc,text="Switch User",width=25,bg="yellow").grid(row=2,column=1)
    # c13=tk.Button(admainsc,text="Cancel A Flight",width=25,command=cancel,bg="orange")
    # c13.grid(row=3,column=2)
    #c14=tk.Button(admainsc,text="Manage Users",width=25,command=manageuser,bg="green").grid(row=5,column=1)
    c15=tk.Button(admainsc,text="Exit The Program",width=25,command=exit,bg="white")
    c15.grid(row=4,column=2)
    c16=tk.Button(admainsc,text="Add A Flight",width=25,command=update,bg="light blue")
    c16.grid(row=2,column=2)
    tk.Label(admainsc,text="").grid(row=7,column=1) 
    admainsc.mainloop()

    
def supmain():#supervisor control panel
    #def switchusersup():
       # supmainsc.destroy()
    global supmainsc
    supmainsc=Tk()
    rp=tk.Label(master=supmainsc,image=img).grid(row=0,column=0)
    supmainsc.title("Supervisor Control Panel")
    tk.Label(master=supmainsc,text="").grid(row=6,column=0) 
    #Load an image in the script
    img= (Image.open("viewflights.png"))
    #Resize the Image using resize method
    resized_image= img.resize((800,750), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    rp=tk.Label(master=stamainsc,image=new_image).place(x=0,y=0,relwidth=1,relheight=1)   
    tk.Button(master=supmainsc,text="View The Details Of Flights",command=view).grid(row=1,column=1)
    tk.Button(master=supmainsc,text="Switch User").grid(row=2,column=1)
    # tk.Button(master=supmainsc,text="Cancel A Flight",command=cancel).grid(row=4,column=1)
    tk.Button(master=supmainsc,text="Exit The Program",command=exit).grid(row=5,column=1)
    tk.Button(master=supmainsc,text="Add A Flight",command=update).grid(row=3,column=1)

    supmainsc.mainloop()
    
def view():#viewing flights

    w = Tk()
    w.geometry("400x430") 
    w.title('view flight details')
    w.configure(bg='grey')
    connect = pymysql.connect(
    host="localhost",
    user="root", 
    passwd="",
    database="airport_management_system")
    conn = connect.cursor()
    ####### end of connection ####
    conn.execute("SELECT * FROM viewflights")
    e=Label(w,width=10,text='flightnumber',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(w,width=10,text='timing',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=Label(w,width=10,text='destination',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=Label(w,width=10,text='source',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    e=Label(w,width=10,text='status',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=4)

    i=1
    for viewflights in conn: 
        for j in range(len(viewflights)):
            e = Label(w, width=10, text=viewflights[j],bg='pink',borderwidth=2,relief='ridge',anchor="w") 
            e.grid(row=i, column=j) 
            #e.(END, viewflights[j])
        i=i+1
    w.mainloop()
    # c=0
    # r=1
    # view=tk.Tk()
    # view.title("View Details Of Flights")
    # tk.Label(master=view,text="Flight Number--------ETA--------Destination-------Status-------Source",bg="blue",fg="white").grid(row=1,column=0)
    # for i in scheduled:
    #     c+=1
    #     r+=1
    #     tk.Label(master=view,text=(i,"-------",scheduled[i][0],"--------",scheduled[i][1],"--------",scheduled[i][2],"--------",scheduled[i][3])).grid(row=r,column=0)
    # for i in cancelled:
    #     c+=1
    #     r+=1
    #     tk.Label(master=view,text=(i,"-------",cancelled[i][0],"--------",cancelled[i][1],"--------",cancelled[i][2],"--------",scheduled[i])).grid(row=r,column=0)
def ticketbooking():
    def seat():
       num = random.randint(10,200)
       print("The seat number is:",num)
       return num
    global passengername,mobileno,flinumber,sourcee,destinationn,getseat
    root=Tk()
    root.title("Book ticket")
    root.geometry('500x450')
    #set the window color
    root.configure(bg='pink')
    passengername = Label(root, text=" Passenger name").grid(row=1, column=2)
    passengername = StringVar()
    passengername = Entry(root, textvariable=passengername)
    passengername.grid(row=1, column=3)  
    mobileno = Label(root, text=" Mobile number").grid(row=2, column=2)
    mobileno = StringVar()
    mobileno = Entry(root, textvariable=mobileno)
    mobileno.grid(row=2, column=3)  
    # gender = Label(root, text='Gender')
    # male = Radiobutton(root, text='Male')
    # female = Radiobutton(root, text='Female')
    flinumber = Label(root, text="Enter flight number").grid(row=6, column=2)
    flinumber = StringVar()
    flinumber=Entry(root, textvariable=flinumber)
    flinumber.grid(row=6, column=3)
    sourcee = Label(root, text="Source").grid(row=7, column=2)
    sourcee= StringVar()
    sourcee=Entry(root, textvariable=sourcee)
    sourcee.grid(row=7, column=3) 
    destinationn = Label(root, text="Destination").grid(row=8, column=2)
    destinationn= StringVar()
    destinationn=Entry(root, textvariable=destinationn)
    destinationn.grid(row=8, column=3) 
    seatnumber = Label(root, text="Seat number")
    seatnumber.grid(row=9, column=2)
    seatnumber = StringVar()
    getseat = Label(root, text=seat())
    getseat.grid(row=9, column=3)
    button=tk.Button(root,text="book ticket",command=getticket)
    button.grid(row=10,column=3)
    
    root.mainloop() 

def viewticket():
     global seat
     root=Tk()
     root.title("View ticket")
     root.geometry('500x450')
     root.configure(bg='yellow')
     seat = Label(root, text="Enter seat number").grid(row=7, column=2)
     seat= StringVar()
     seat=Entry(root, textvariable=seat)
     seat.grid(row=7, column=3) 
     button1=tk.Button(root,text="view ticket",command=Fetch2)
     button1.grid(row=10,column=3)
     root.mainloop()

def stamain():
    # def switchuserstand():
    # stamainsc.destroy()
    global stamainsc
    stamainsc=Tk()
    stamainsc.geometry('2000x1000')
    stamainsc.title("Standard User Control Panel")
    img = PhotoImage(file="marvelous.png")
    label = Label(stamainsc,image=img)
    label.place(x=0, y=0)
    # stamainsc.configure(bg='green')
    b11=tk.Button(stamainsc,text="View The Details Of Flights",width=20,command=view,bg="red")
    b11.grid(row=15,column=5)
    b12=tk.Button(stamainsc,text="Book Ticket",width=20,command=ticketbooking,bg="pink")
    b12.grid(row=25,column=5)
    b13=tk.Button(stamainsc,text="View your ticket",width=20,command=viewticket,bg="white")
    b13.grid(row=35,column=5)
    b15=tk.Button(stamainsc,text="Exit The Program",width=20,command=exit,bg="orange")
    b15.grid(row=55,column=5)
    tk.Label(stamainsc,text="").grid(row=65,column=5)
    stamainsc.mainloop() 
def registration():
    loginsc.destroy()
    global registrate,firstname,lastname,username,email,password,cmb
    registrate = Tk()
    registrate.geometry("500x450")
    registrate.title("Registration Page")
    registrate.configure(bg='orange')
    # img = PhotoImage(file="registration.png")
    # label = Label(root,image=img)
    # label.place(x=0, y=0)
    firstname=Label(registrate,text="First Name")
    lastname=Label(registrate,text="Last Name")
    username=Label(registrate,text="Username")
    email=Label(registrate,text="Email")
    password=Label(registrate,text="Password")
    role=Label(registrate,text="Select Role")
    roleIn=["Standard User","Admin","Supervisor"]
    firstname.grid(row=2,column=0)
    lastname.grid(row=3,column=0)
    username.grid(row=4,column=0)
    email.grid(row=5,column=0)
    password.grid(row=6,column=0)
    role.grid(row=7,column=1)
    firstname=StringVar()
    lastname=StringVar()
    username=StringVar()
    email=StringVar()
    password=StringVar()
    firstname=Entry(registrate,textvariable=firstname,width=30,bd=3)
    lastname=Entry(registrate,textvariable=lastname,width=30,bd=3)
    username=Entry(registrate,textvariable=username,width=30,bd=3)
    email=Entry(registrate,textvariable=email,width=30,bd=3)
    password=Entry(registrate,textvariable=password, show="*",width=30,bd=3)
    cmb=ttk.Combobox(registrate,value=roleIn)
    cmb.grid(row=8,column=1)
    cmb.current(0)
    firstname.grid(row=2,column=1)
    lastname.grid(row=3,column=1)
    username.grid(row=4,column=1)
    email.grid(row=5,column=1)
    password.grid(row=6,column=1)
    b9= Button(registrate,text = "Register",width="15",command=insertfun,bg='red')
    b9.grid(row=60,column=1)
    # Button(text="Register Now",bg="green",fg="white",command=insertfun,cursor="hand2",pady=0).place(x=161,y=220)
    bw= Button(registrate,text = "Signup",width="15",command=login,bg='green')
    bw.grid(row=67,column=1)
    registrate.mainloop()

def login():             
    
    global loginsc,username,password
    try:
        registrate.destroy()
    except Exception as e:
        print(e)
    loginsc=Tk()
    loginsc.geometry('450x400') 
    loginsc.title("Login")
    loginsc.configure(bg='orange')
    tk.Label(master=loginsc,text="").grid(row=5,column=1)
    img = PhotoImage(file="check.png")
    label = Label(loginsc,image=img)
    label.place(x=0, y=0)
    # resized_image= img.resize((800,750), Image.ANTIALIAS)
    # new_image= ImageTk.PhotoImage(resized_image)
    #Load an image in the script
    # img= (Image.open("login page.png"))
    # #Resize the Image using resize method
    
    #username label and text entry box
    username = Label(loginsc, text="User Name")
    username.grid(row=1, column=2)
    username = StringVar()
    username = Entry(loginsc, textvariable=username)
    username.grid(row=1, column=3)  
    #password label and password entry box
    password = Label(loginsc,text="Password").grid(row=2, column=2)  
    password = StringVar()
    password = Entry(loginsc, textvariable=password, show='*')
    password.grid(row=2, column=3)
    role=Label(loginsc,text="Select Role")
    roleIn=["Standard User","Admin","Supervisor"]
    global cmb
    cmb=ttk.Combobox(loginsc,value=roleIn)
    cmb.grid(row=9,column=3)
    cmb.current(0)
    role.grid(row=8,column=3)
    

    #validateLogin = partial(validateLogin, username, password)
    #login button
    loginButton = Button(loginsc, text="Login", command=Log)
    loginButton.grid(row=10, column=3)   
    b= Button(loginsc,text = "Create account?",width="15",command=registration)
    b.grid(row=50,column=3)
    loginsc.mainloop()
# def open():
#     os.chdir(os.getcwd()) #change this path to your path where your f1.py and f2.py is located
#     print("current dir "+os.getcwd())
#     loginsc.destroy()
#     os.system('python '+'register.py') #runnning the python command on cmd to execute both windows      
login()  
