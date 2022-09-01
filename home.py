
from tkinter import *
from tkinter import messagebox
import time
from PIL import ImageTk,Image


Aces=Tk()
Aces.title("Home Page")


#GUI of window
Aces.geometry("600x300")
Aces.resizable(width=False,height=False)

#icon for window
photo = PhotoImage(file ='logo.png')
Aces.iconphoto(True, photo) #window icon

my_pic=Image.open("back1.png")
resized=my_pic.resize((600,300),Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(resized)
background = Label(Aces, image = photo3).place(x=0, y=0) #since tkinter doesn't support background image, we place it as a label



#background image for window
photo2=PhotoImage(file='logo.png')
background = Label(Aces, image = photo2).place(x=330, y=40) #since tkinter doesn't support background image, we place it as a label

#-------------menu bar------------------

my_menu=Menu(Aces)
Aces.config(menu=my_menu)


#------command--------
def our_command():
    top=Toplevel()
    top.geometry('270x310')
    top.title('About system')
    top.resizable(width=False,height=False)

    title=Label(top, text="Version:1.0.1 \n This is a store management system \n which is developed by Aces group as \n a group project for sem 1. This \n system allows store owner to store, \n update, read and delete record of \nmerchandise in store and also for employees\n data. This system makes store easy to \nmanage and also more  efficient. Data \nstored in this  system can be retrived\n anytime and can be modified. This system \nis very secure as username and password is \nrequired to fetch data. Only admin can \nadd, remove, update and  delete  data\n but merchandises' data can be seen and\n updated by employee also to make \nthe data uptodate. Password of employee \naccount can be changed by individual. ")
    title.place(x=10,y=10)



def developed():
    top=Toplevel()
    top.geometry('270x300')
    top.title('Developing team')
    top.resizable(width=False,height=False)


    #----------frame-----------
    Frame(top,bg='light blue',height=300,width=300).place(x=0,y=0)
    title=Label(top,text="Group project by Aces",  bg="light blue", fg='black', font=('impact',15,))
    title.place(x=30, y=20)
    title=Label(top,text="Abishek Bimali (C), Coventry ID : 12332649",  bg="light blue", fg='red', )
    title.place(x=20, y=60)
    title=Label(top,text="Shrijan Pokharel, Coventry ID: 12333510",  bg="light blue", fg='red', )
    title.place(x=20, y=80)
    title=Label(top,text="Bikesh Chaudary, Coventry ID : 12332823 ",  bg="Light blue", fg='red', )
    title.place(x=20, y=100)
    title=Label(top,text="Shekh MD Atiur Rahaman, Coventry ID:12333473",  bg="light blue", fg='red', )
    title.place(x=5, y=120)

    def back():
        top.destroy()
    button_top=Button(top,text="exit",command=back,bg="red",fg="white")
    button_top.place(x=80,y=200)

def exit():
    status=messagebox.askyesno(title="Exit",message="Do you really want to exit?")
    if status==True:
        Aces.destroy()
        # messagebox.showinfo(message="System closed!")

    else:
        pass

#-------------photo for icon ------
my_pic=Image.open("exit.png")
resized=my_pic.resize((80,20),Image.ANTIALIAS)
photo4 = ImageTk.PhotoImage(resized)
#----menu items-------
file_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=file_menu)
file_menu.add_cascade(label="About System",command=our_command)
file_menu.add_separator()
file_menu.add_cascade(label="Exit",image=photo4,command=exit)
file_menu.add_separator()
file_menu.add_cascade(label="Developed By",command=developed)

#=======second menu-----------------
setting_menu=Menu(my_menu)
my_menu.add_cascade(label="new",menu=setting_menu)



#frame 
Frame_Aces=Frame(Aces,bg="light blue")
Frame_Aces.place(x=10,y=60,height=130,width=280)

# creating text
text=Label(Aces,text="Welcome to Homepage of Crazy Store",fg="red",bg="light blue")
text.place(x=45,y=70)

l1=Label(Aces,text="We provide all goods such as groceries  including ",fg="red",bg="light blue")
l1.place(x=15,y=90)


l2=Label(Aces,text="electronic. ",fg="red",bg="light blue")
l2.place(x=80,y=110)



#----------import-------------

def employee():
    Aces.destroy()
    import employelogin

def admin():
    Aces.destroy()
    import Adminlogin




#----images for buttons---------

my_pic1=Image.open("admin.png")
resized=my_pic1.resize((60,20),Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(resized)
my_pic2=Image.open("employee.png")
resized=my_pic2.resize((80,20),Image.ANTIALIAS)
photo6 = ImageTk.PhotoImage(resized)
#creating buttons

B=Button(Aces,image=photo6,command=employee,cursor="hand2",bd=1)
B.place(x=25,y=150)

C=Button(Aces,image=photo5,cursor="hand2",command=admin,bd=1)
C.place(x=205,y=150)
 

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
my_label.place(x=450,y=220)


my_label2=Label(Aces,text="",bg="red",fg="white",font=(30))
my_label2.place(x=450,y=250)


clock()
Aces.mainloop()
