#tkinter window
from tkinter import *
import time
import sqlite3
from tkinter import messagebox
from PIL import ImageTk,Image

Aces=Tk()
#--------Displaying title--------------
Aces.title("Employee log in Page")
Aces.geometry("600x300")
Aces.resizable(width=False,height=False)

#----------icon for window------------
photo = PhotoImage(file = 'logo.png')
Aces.iconphoto(True, photo) #window icon

#-------------background image-------------
my_pic=Image.open("back1.png")
resized=my_pic.resize((600,300),Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(resized)
background = Label(Aces, image = photo3).place(x=0, y=0) #since tkinter doesn't support background image, we place it as a label

# photo2=PhotoImage(file='logo1.png')
# background = Label(Aces, image = photo2).place(x=280, y=20) #since tkinter doesn't support background image, we place it as a label


#-----frame---- 
Frame_Aces=Frame(Aces,bg="light blue")
Frame_Aces.place(x=10,y=30,height=250,width=260)


text=Label(Aces,text="Employee Log in here",bg="red",fg="white",bd=2,font=("impact",15," "))
text.place(x=55,y=32)



#----------------databse connect-------------------------------

#text1=username
# text2=password 

def check():
        a=text1.get()
        b=text2.get()

        conn=sqlite3.connect('admin.db')
        c=conn.cursor()

        c.execute("SELECT * from employee")
        records=c.fetchall()
        i=len(records)-1
        while i>=0:
            if records[i][3]!=a or records[i][4]!=b:
                i=i-1
                if i==-1:
                    messagebox.showerror("Login","Invalid Credentials")
                  
                    break
            else:
                messagebox.showinfo("Login","Logged in Successfully")
                Aces.destroy()
                import viewitem
            
                break             
        conn.commit()
        conn.close()
        


text=Label(Aces,text="User name",fg="brown",bg="light blue")
text1=Entry(Aces)
text1.place(x=45,y=95,width=150)
text.place(x=50,y=70)




def show():
    if (showw.get()==1):
        text2.config(show='')
    else:
        text2.config(show='*')



A=Label(Aces,text="Password",fg="brown",bg="light blue")
A.place(x=50,y=120)

text2=Entry(Aces,)
text2.place(x=45,y=145,width=150)
showw=IntVar(value=1)
Checkbutton(text='show',offvalue=0,variable=showw,bg='lightblue',command=show).place(x=210,y=145)


#------Cancel Function----

def cancel():
    status=messagebox.askyesno(title="Close",message="DO you really want to close? ")
    if status==True:
        Aces.destroy()
        import home
    else:
        pass



def change():
    top=Toplevel()
    top.geometry('300x320')
    top.title('Forget password')
    top.resizable(width=False,height=False)

    
	#===frame =====
    frame_top=Frame(top,bg="light blue")
    frame_top.place(x=10,y=5,height=290,width=280)
    text=Label(frame_top,text="Forget Password",font=("impact",14),bg="red",fg="white").place(x=35,y=10)
    #===show password==
    def show():
        if (showw.get()==1):
            re.config(show='')
        else:
            re.config(show='*')
    def show2():
        if (showww.get()==1):
            re1.config(show='')
        else:
            re1.config(show='*')
    


    text=Label(frame_top,text="Username",fg="red",bg="light blue")
    old=Entry(frame_top)
    old.place(x=45,y=70,width=150)
    text.place(x=50,y=45)
    A=Label(frame_top,text="Fullname ",fg="red",bg="lightblue")
    A.place(x=50,y=95)
    new=Entry(frame_top,)
    new.place(x=45,y=120,width=150)
    A=Label(frame_top,text="New Password",fg="red",bg="light blue")
    A.place(x=50,y=145)
    re=Entry(frame_top,)
    re.place(x=45,y=170,width=150)
    showw=IntVar(value=1)
    Checkbutton(top,text='Show',offvalue=0,variable=showw,bg='lightblue',command=show).place(x=210,y=172)
    A=Label(frame_top,text="Re_type Password",fg="red",bg="light blue")
    A.place(x=50,y=195)
    re1=Entry(frame_top,)
    re1.place(x=45,y=220,width=150)
    showww=IntVar(value=1)
    Checkbutton(top,text='Show',offvalue=0,variable=showww,bg='lightblue',command=show2).place(x=210,y=222) 

    

     #===clear entry=
    def clear_entries():
        old.delete(0, END)
        new.delete(0, END)
        re.delete(0, END)
        re1.delete(0, END)

    def change_password():
        a=old.get()
        b=new.get()
        c=re.get()
        d=re1.get()

        conn = sqlite3.connect('admin.db')
        c = conn.cursor()
        c.execute("SELECT * from employee")
        records=c.fetchall()
        i=len(records)-1
        while i>=0:
            if records[i][3]!=a or records[i][0]!=b:
                i=i-1
                if i==-1:
                    messagebox.showerror("Invalid","Username or Fullname not matched")
                    break
            else:
                c.execute("""  UPDATE  employee SET 
					
						Password = :Pass

					WHERE Username = :a""",
					{
					'Pass': re.get(),
						
						'a': a
					})
                messagebox.showinfo("Changed Password","Password reset successfully!")
                break
        conn.commit()
        conn.close()
        clear_entries()

    def change_check():
        a=old.get()
        b=new.get()
        c=re.get()
        d=re1.get()
        if(a=="" or b=="" or c=="" or d==""):
            messagebox.showerror("Invalid","One or More Fields Empty.")
        elif b==c or c==a:
            messagebox.showerror("error password","Password should not be username or fullname!!")
        elif c!=d:
            messagebox.showerror("Error password","Password didn't match!!")
        elif len(d)<6:
            messagebox.showerror("invalid","Password should ba atleast 6 characters!")
        else:
            change_password()


    B=Button(top, text="Change password",bg="red",fg="white",command=change_check,cursor="hand2",bd=1)
    B.place(x=90,y=280)


B=Button(Aces,text="Login",fg="white",bg="red",bd=0,cursor="hand2",command=check)
B.place(x=65,y=180)

C=Button(Aces,text="Cancel" ,command=cancel,bd=0,fg="white",bg="red",cursor="hand2",)
C.place(x=170,y=180)

d=Button(Aces,text="Forget Password?" ,command=change,bd=0,fg="blue",bg="light blue",cursor="hand2",)
d.place(x=110,y=255)
 
 
#-----------time for window-----------------
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