from tkinter import *
from tkinter import messagebox
import time
import sqlite3
from  PIL import ImageTk,Image


Aces=Tk()
Aces.title("Admin log in Page")
Aces.geometry("600x300")
Aces.resizable(width=False,height=False)
photo = PhotoImage(file = 'logo.png')
Aces.iconphoto(True, photo) #window icon




my_pic=Image.open("back1.png")
resized=my_pic.resize((600,300),Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(resized)
background = Label(Aces, image = photo3).place(x=0, y=0) #since tkinter doesn't support background image, we place it as a label

# photo2=PhotoImage(file='crazy.png')
# background = Label(Aces, image = photo2).place(x=320, y=20) #since tkinter doesn't support background image, we place it as a label


#frame 
Frame_Aces=Frame(Aces,bg="light blue")
Frame_Aces.place(x=10,y=30,height=250,width=260)


text=Label(Aces,text="Admin Log in here",bg="red",fg="white",bd=2,font=("impact",15," "))
text.place(x=65,y=32)


#--------------show---------

def show():
    if (showw.get()==1):
        text2.config(show='')
    else:
        text2.config(show='*')


text=Label(Aces,text="User name",fg="brown",bg="light blue")
text1=Entry(Aces)
text1.place(x=45,y=95,width=150)
text.place(x=85,y=70)

A=Label(Aces,text="Password",fg="brown",bg="light blue")
text2=Entry(Aces,)
text2.place(x=45,y=145,width=150)
A.place(x=85,y=120)
showw=IntVar(value=1)
Checkbutton(text='show',offvalue=0,variable=showw,bg="light blue",bd=0,command=show).place(x=205,y=145)




#------Cancel function----



def cancel():
    status=messagebox.askyesno(title="Close",message="DO you really want to cancel? ")
    if status==True:
        Aces.destroy()
        import home
    else:
       pass

#--------signup for Admin--------------------

def adminsign():
    top=Toplevel()
    top.geometry('250x300')
    top.title('Admin signup here')
    top.resizable(width=False,height=False)


    Frame(top,bg='lightblue',height=300,width=300).place(x=0,y=0)
    title=Label(top, text='Admin signup', bg="red", fg='white', font=('Arial',20,'bold'))
    title.place(x=40, y=20)


    #-----hide password--------
    def show():
        if (showw.get()==1):
            user_password.config(show='')
        else:
            user_password.config(show='*')

    def show2():
        if (showww.get()==1):
            user_default.config(show='')
        else:
            user_default.config(show='*')
    

    
    A=Label(top, text='Username', bg="lightblue", fg='red')
    A.place(x=100, y=75)
    user_name=Entry(top)
    user_name.place(x=60, y=100,)

    B=Label(top, text='Password', bg="lightblue", fg='red')
    B.place(x=100, y=125)
    user_password=Entry(top)
    user_password.place(x=60, y=150,)
    showw=IntVar(value=1)
    Checkbutton(top,text='Show',offvalue=0,variable=showw,bg='lightblue',command=show).place(x=190,y=150)


  
    c=Label(top, text='Default Password', bg="lightblue", fg='red')
    c.place(x=70, y=175)
    user_default=Entry(top)
    user_default.place(x=60, y=200,)
    showww=IntVar(value=1)
    Checkbutton(top,text='Show',offvalue=0,variable=showww,bg='lightblue',command=show2).place(x=190,y=200) 
    #-------------table for data base-----------

    def get():
       user_name.delete(0,END)
       user_password.delete(0,END)
       user_default.delete(0,END)


    try:
        conn=sqlite3.connect("admin.db")
        c=conn.cursor()
        c.execute("""CREATE TABLE admin(
       
       Admin_username text,
       Admin_password text
        )""")
        conn.commit()
        conn.close()      
    except:
        pass
 
       
    def adduser():
        conn=sqlite3.connect('admin.db')
        c=conn.cursor()
        c.execute("INSERT INTO admin VALUES (:Admin_username, :Admin_password)",
     {
        "Admin_username":user_name.get(),
        "Admin_password":user_password.get(),
              })
        conn.commit()
        conn.close()
        get()

    def Addadmin():
        A=user_name.get()
        H=A.find("@")


        if user_password.get()=="" or user_name.get()=="":
            messagebox.showerror(title="Empty entry ",message="One or more entries are empty!")
        elif H!=0:
                messagebox.showerror("Invalid","Username should start with @!")
        elif len(user_password.get())<6:
            messagebox.showerror("Invalid","Pssword must be more then 6 Character!")
        elif user_default.get()!="Admin":
                      messagebox.showerror(title="Error ",message="Invalid Default Password!")      
        else:
            try:
               adduser()
               messagebox.showinfo(title="Success",message="Admin added!")
               top.destroy()
              
            except:
                pass



    
    BUttn_add=Button(top,text="Add",fg="white",bg="red",bd=2,cursor="hand2",command=Addadmin)
    BUttn_add.place(x=150,y=230)
#----------------connecting database for login---------------------    

def check():
        a=text1.get()
        b=text2.get()

        conn=sqlite3.connect('admin.db')
        c=conn.cursor()

        c.execute("SELECT * from admin")
        records=c.fetchall()
        i=len(records)-1
        while i>=0:
            if records[i][0]!=a or records[i][1]!=b:
                i=i-1
                if i==-1:
                    messagebox.showerror("Login","Invalid")
                  
                    break
            else:
                messagebox.showinfo("Login","Logged in Successfully")
                Aces.destroy()
                import adminhomepage
            
                break             
        conn.commit()
        conn.close()



#--------image for buttons----------


B=Button(Aces,text="Login",fg="white",bg="red",bd=0,cursor="hand2",command=check)
B.place(x=65,y=180)


BUttn_b=Button(Aces,text="Cancel",fg="white",bg="red",bd=0,cursor="hand2",command=cancel)
BUttn_b.place(x=180,y=180)



BUttn_sign=Button(Aces,text="Register here!",bg="lightblue",fg="blue",bd=0,cursor="hand2",command=adminsign)
BUttn_sign.place(x=110,y=250)




#time for window
def clock():
    hours=time.strftime("%I")
    minutes=time.strftime("%M")
    second=time.strftime("%S")
    day=time.strftime("%A")
    am_pm=time.strftime("%p")


    my_label.config(text= hours + ":" + minutes + ":" + second + " " + am_pm)
    my_label.after(1000,clock)

    my_label2.config(text=day )
    



my_label=Label(Aces,text= " ",fg="white",bg="red",font=(48))
my_label.place(x=450,y=200)


my_label2=Label(Aces,text="",fg="White",bg="red",font=(30))
my_label2.place(x=450,y=230)


clock()




Aces.mainloop()