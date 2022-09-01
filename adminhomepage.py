#Admin_Home_Page
from tkinter import *
import time
from tkinter import messagebox
from PIL import ImageTk,Image



Aces=Tk()


#Displaying title
Aces.title("Admin log in Page")


#sets geometry according to provided data
Aces.geometry("600x300")
Aces.resizable(width=False,height=False)

photo = PhotoImage(file = 'logo.png')
Aces.iconphoto(True, photo) #window icon


my_pic=Image.open("back1.png")
resized=my_pic.resize((600,300),Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(resized)
background = Label(Aces, image = photo3)
background.place(x=0, y=0) #since tkinter doesn't support background image, we place it as a label



# my_pic1=Image.open("crazy.png")
# resized=my_pic1.resize((250,250),Image.ANTIALIAS)
# photo4 = ImageTk.PhotoImage(resized)
# background = Label(Aces, image = photo4)
# background.place(x=320, y=20) #since tkinter doesn't support background image, we place it as a label



#-------frame---------
Frame_Aces=LabelFrame(Aces,text="Data Query",bg="white")
Frame_Aces.place(x=30,y=180,height=80,width=362)

def homeadmin():
    Aces.destroy()
    import addemployee

def Addhome():
    Aces.destroy()
    import Additem

#=========image in button===========

my_pic1=Image.open("employeedata.png")
resized=my_pic1.resize((80,30),Image.ANTIALIAS)
photo4 = ImageTk.PhotoImage(resized)
 #button 
C=Button(Aces,image=photo4,cursor="hand2",command= homeadmin)
C.place(x=30,y=200)

my_pic2=Image.open("itemsdata.png")
resized=my_pic2.resize((80,30),Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(resized)

D=Button(Aces,image=photo5,cursor="hand2",command=Addhome)
D.place(x=120,y=200)


def cancel():
    status=messagebox.askyesno(title="Close",message="DO you really want to logout? ")
    if status==True:
        Aces.destroy()
        import Adminlogin
    else:
       pass
def admindata():
    Aces.destroy()
    import admintable


my_pic3=Image.open("logout.png")
resized=my_pic3.resize((80,30),Image.ANTIALIAS)
photo6 = ImageTk.PhotoImage(resized)
E=Button(Aces,image=photo6,cursor="hand2",command=cancel)
E.place(x=300,y=200)


my_pic4=Image.open("admindata.png")
resized=my_pic4.resize((80,30),Image.ANTIALIAS)
photo7 = ImageTk.PhotoImage(resized)
E=Button(Aces,image=photo7,cursor="hand2",command=admindata)
E.place(x=210,y=200)


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


my_label2=Label(Aces,text="",fg="white",bg="red",font=(30))
my_label2.place(x=450,y=230)


clock()
Aces.mainloop()