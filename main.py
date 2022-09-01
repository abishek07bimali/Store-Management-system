
from tkinter import *
from tkinter import messagebox
import time
from PIL import ImageTk,Image
import sqlite3
from tkinter import ttk



Aces=Tk()
Aces.title("Crazy Store")


#GUI of window
Aces.geometry("1270x670")
Aces.resizable(width=False,height=False)

#icon for window
photo = PhotoImage(file ='Images//logo.png')
Aces.iconphoto(True, photo) #window icon

my_pic=Image.open("Images//back1.png")
resized=my_pic.resize((1270,670),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized)
background = Label(Aces, image = photo).place(x=0, y=0) #since tkinter doesn't support background image, we place it as a label



#background image for window
my_pic1=Image.open("Images//logo.png")
resized=my_pic1.resize((450,480),Image.ANTIALIAS)
photologo = ImageTk.PhotoImage(resized)
background = Label(Aces, image = photologo).place(x=800, y=50) #since tkinter doesn't support background image, we place it as a label

#-------------menu bar------------------

my_menu=Menu(Aces)
Aces.config(menu=my_menu)


#------command--------
def our_command():
    frame_menu1=Frame(Aces,bg="light blue")
    frame_menu1.place(x=10,y=0,height=350,width=270)

    title=Label(frame_menu1,bg="light blue", text="Version:1.0.1 \n This is a store management system \n which is developed by Aces group as \n a group project for sem 1. This \n system allows store owner to store, \n update, read and delete record of \nmerchandise in store and also for employees\n data. This system makes store easy to \nmanage and also more  efficient. Data \nstored in this  system can be retrived\n anytime and can be modified. This system \nis very secure as username and password is \nrequired to fetch data. Only admin can \nadd, remove, update and  delete  data\n but merchandises' data can be seen and\n updated by employee also to make \nthe data uptodate. Password of employee \naccount can be changed by individual. ")
    title.place(x=10,y=10)
    def exit_frame_menu1():
        frame_menu1.destroy()
    button_top=Button(frame_menu1,text="Cancel",command=exit_frame_menu1,bg="red",fg="white",width=20)
    button_top.place(x=60,y=300)



def developed():
        #----------frame-----------
    frame_menu=Frame(Aces,bg="lightblue")
    frame_menu.place(x=10,y=0,height=300,width=300)

    title=Label(frame_menu,text="Group project by Aces",  bg="light blue", fg='black', font=('impact',15,))
    title.place(x=30, y=20)
    title=Label(frame_menu,text="Abishek Bimali (Leader), Coventry ID : 12332649",  bg="light blue", fg='red', )
    title.place(x=20, y=60)
    title=Label(frame_menu,text="Shrijan Pokharel, Coventry ID: 12333510",  bg="light blue", fg='red', )
    title.place(x=20, y=80)
    title=Label(frame_menu,text="Bikesh Chaudary, Coventry ID : 12332823",  bg="Light blue", fg='red', )
    title.place(x=20, y=100)
    title=Label(frame_menu,text="Shekh MD Atiur Rahaman, Coventry ID-12333473",  bg="light blue", fg='red', )
    title.place(x=5, y=120)

    def back():
        frame_menu.destroy()
    button_top=Button(frame_menu,text="Cancel",command=back,bg="red",fg="white",width=20)
    button_top.place(x=60,y=200)

def exit():
    status=messagebox.askyesno(title="Exit",message="Do you really want to exit?")
    if status==True:
        Aces.destroy()
        # messagebox.showinfo(message="System closed!")

    else:
        pass

#-------------photo for icon ------
my_pic=Image.open("Images//exit.png")
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
Frame_Aces=Frame(Aces,bg="#728FCE")
Frame_Aces.place(x=280,y=200,height=200,width=350)

# creating text
text=Label(Frame_Aces,text="Welcome to Homepage of Crazy Store",fg="red",bg="#728FCE")
text.place(x=45,y=10)

l1=Label(Frame_Aces,text="We provide all goods such as groceries  including ",fg="red",bg="#728FCE")
l1.place(x=40,y=40)


l2=Label(Frame_Aces,text="electronic. ",fg="red",bg="#728FCE")
l2.place(x=130,y=70)

#----images for buttons---------

my_pic1=Image.open("Images//admin.png")
resized=my_pic1.resize((60,20),Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(resized)
my_pic2=Image.open("Images//employee.png")
resized=my_pic2.resize((80,20),Image.ANTIALIAS)
photo6 = ImageTk.PhotoImage(resized)

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
my_label.place(x=900,y=550)


my_label2=Label(Aces,text="",bg="red",fg="white",font=(30))
my_label2.place(x=900,y=580)


clock()



#----------import-------------

def employee():
    
    frame_import=Frame(Aces,bg="light blue")
    frame_import.place(x=0,y=0,height=670,width=700)
        
    global photo1
    my_pic=Image.open("Images//back1.png")
    resized=my_pic.resize((1270,670),Image.ANTIALIAS)
    photo1 = ImageTk.PhotoImage(resized)
    background = Label(frame_import, image = photo1).place(x=0, y=0) #since tkinter doesn't support background image, we place it as a label

    # photo2=PhotoImage(file='logo1.png')
    # background = Label(frame_import, image = photo2).place(x=280, y=20) #since tkinter doesn't support background image, we place it as a label


    #-----frame---- 
    Frame_frame_import=Frame(frame_import,bg="light blue")
    Frame_frame_import.place(x=280,y=200,height=250,width=280)


    text=Label(Frame_frame_import,text="Employee Log in here",bg="red",fg="white",bd=2,font=("impact",15," "))
    text.place(x=55,y=32)
    text=Label(Frame_frame_import,text="User name",fg="brown",bg="light blue")
    text1=Entry(Frame_frame_import)
    text1.place(x=45,y=95,width=150)
    text.place(x=50,y=70)




    def show():
        if (showw.get()==1):
            text2.config(show='')
        else:
            text2.config(show='*')



    A=Label(Frame_frame_import,text="Password",fg="brown",bg="light blue")
    A.place(x=50,y=120)

    text2=Entry(Frame_frame_import,)
    text2.place(x=45,y=145,width=150)
    showw=IntVar(value=1)
    Checkbutton(Frame_frame_import,text='show',offvalue=0,variable=showw,bg='lightblue',command=show).place(x=210,y=145)




    #----------------databse connect-------------------------------

    #text1=username
    # text2=password 
    def import_viewitems():
        frame_viewitems=Frame(Aces)
        frame_viewitems.place(x=0,y=0,height=670,width=800)     

        def change():
            #===frame =====
            frame_top=Frame(frame_viewitems,bg="#728FCE")
            frame_top.place(x=200,y=100,height=310,width=300)

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
            def show3():
                if (showw1.get()==1):
                    new.config(show='')
                else:
                    new.config(show='*')

            text=Label(frame_top,text="Change Password",font=("impact",14),bg="red",fg="white").place(x=45,y=10)


            text=Label(frame_top,text="Username",fg="red",bg="#728FCE")
            old=Entry(frame_top)
            old.place(x=45,y=70,width=150)
            text.place(x=50,y=45)
            A=Label(frame_top,text="Current Password",fg="red",bg="#728FCE")
            A.place(x=50,y=95)
            new=Entry(frame_top,)
            new.place(x=45,y=120,width=150)
            showw1=IntVar(value=1)
            Checkbutton(frame_top,text='Show',offvalue=0,variable=showw1,bg='#728FCE',command=show3).place(x=210,y=122)
            
            
            A=Label(frame_top,text="New Password",fg="red",bg="#728FCE")
            A.place(x=50,y=145)
            re=Entry(frame_top,)
            re.place(x=45,y=170,width=150)
            showw=IntVar(value=1)
            Checkbutton(frame_top,text='Show',offvalue=0,variable=showw,bg='#728FCE',command=show).place(x=210,y=172)


            A=Label(frame_top,text="Re_type Password",fg="red",bg="#728FCE")
            A.place(x=50,y=195)
            re1=Entry(frame_top,)
            re1.place(x=45,y=220,width=150)
            showww=IntVar(value=1)
            Checkbutton(frame_top,text='Show',offvalue=0,variable=showww,bg='#728FCE',command=show2).place(x=210,y=222) 
            
            
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
                    if records[i][3]!=a or records[i][4]!=b:
                        i=i-1
                        if i==-1:
                            messagebox.showerror("Invalid","Username or Password not matched")
                            break
                    else:
                        c.execute("""  UPDATE  employee SET 
                            
                                Password = :Pass

                            WHERE Username = :a""",
                            {
                            'Pass': re.get(),
                                
                                'a': a
                            })
                        messagebox.showinfo("Changed Password","Password changed successfully!")
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
                    messagebox.showerror("Invalid","One or More Fields Empty!")
                elif b==c:
                    messagebox.showerror("error password","new password should not be same as old!!")
                elif c==a:
                    messagebox.showerror("error password","Password should not be username!")
                elif c!=d:
                    messagebox.showerror("Error password","Password didn't match!!")
                elif len(d)<6:
                    messagebox.showerror("invalid","Password should ba atleast 6 characters!")
                else:
                    change_password()
            def exit_frame():
                frame_top.destroy()

                
            B=Button(frame_top, text=" Update password",bg="red",fg="white",command=change_check,cursor="hand2",bd=1)
            B.place(x=120,y=280) 
            cancel_button=Button(frame_top, text="Cancel",bg="red",fg="white",command=exit_frame,cursor="hand2",bd=1)
            cancel_button.place(x=30,y=280)   

        def query_database():
            # Create a database or connect to one that exists
            conn = sqlite3.connect('admin.db')
            c = conn.cursor()
            c.execute("SELECT rowid, * FROM items")
            records = c.fetchall()
            
            # Add our data to the screen
            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3],record[4]), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3],record[4]), tags=('oddrow',))
                # increment counter
                count += 1


            conn.commit()
            conn.close()


        def search_records():
            lookup_record = search_entry.get()

            # Clear the Treeview
            for record in my_tree.get_children():
                my_tree.delete(record)
            conn = sqlite3.connect('admin.db')
            c = conn.cursor()

            c.execute("SELECT rowid, * FROM items WHERE Itemname like ?", (lookup_record,))
            records = c.fetchall()
            
            # Add our data to the screen
            global count
            count = 0
            
            for record in records:
                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3],record[4]), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3],record[4]), tags=('oddrow',))
                # increment counter
                count += 1


            conn.commit()
            conn.close()

        #====search function======
        def checksearch():
            if search_entry.get()=="":
                messagebox.showerror("Invalid","Search Fields Empty.")
            else:
                search_records()
            


        # Add Some Style
        style = ttk.Style()

        # Pick A Theme
        style.theme_use('default')

        # Configure the Treeview Colors
        style.configure("Treeview",
            background="#D3D3D3",
            foreground="black",
            rowheight=25,
            fieldbackground="light blue")

        # Change Selected Color
        style.map('Treeview',
            background=[('selected', "red")])

        #========image for frame=====
        global photo5_view
        my_pic1=Image.open("Images//items.png")
        resized=my_pic1.resize((753,40),Image.ANTIALIAS)
        photo5_view= ImageTk.PhotoImage(resized)

        # Create a Treeview Frame
        tree_frame = Frame(frame_viewitems,height=5,bg="Light blue")
        tree_frame.pack(pady=10)

        text=Label(tree_frame,image=photo5_view,bg='light blue')
        text.pack(side=TOP)

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        # Create The Treeview
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
        my_tree.pack()

        # Configure the Scrollbar
        tree_scroll.config(command=my_tree.yview)


        # Define Our Columns
        my_tree['columns'] = ("ID", "Itemname", "Rate", "Quantity", "Avaibality")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("ID", anchor=W, width=50)
        my_tree.column("Itemname", anchor=W, width=200)
        my_tree.column("Rate", anchor=CENTER, width=150)
        my_tree.column("Quantity", anchor=CENTER, width=150)
        my_tree.column("Avaibality", anchor=CENTER, width=180)


        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("ID", text="ID", anchor=W)
        my_tree.heading("Itemname", text="Itemname", anchor=W)
        my_tree.heading("Rate", text="Rate", anchor=CENTER)
        my_tree.heading("Quantity", text="Quantity", anchor=CENTER)
        my_tree.heading("Avaibality", text="Avaibality", anchor=CENTER)

        # Create Striped Row Tags
        my_tree.tag_configure('oddrow', background="green")
        my_tree.tag_configure('evenrow', background="lightgreen")

        # Add Record Entry Boxes
        data_frame = LabelFrame(frame_viewitems, text="Record of merchandise",bg="Light blue")
        data_frame.pack(fill="x", expand="yes", padx=10)

        id = Label(data_frame, text="ID",bg="Light blue")
        id.grid(row=0, column=0, padx=10, pady=10)
        id = Entry(data_frame)
        id.grid(row=0, column=1, padx=10, pady=10)

        fn_label = Label(data_frame, text="Itemname",bg="Light blue")
        fn_label.grid(row=0, column=2, padx=10, pady=10)
        fn_entry = Entry(data_frame)
        fn_entry.grid(row=0, column=3, padx=10, pady=10)

        rate_label = Label(data_frame, text="Rate",bg="Light blue")
        rate_label.grid(row=0, column=4, padx=10, pady=10)
        rate_entry = Entry(data_frame)
        rate_entry.grid(row=0, column=5, padx=10, pady=10)

        quanatity_label = Label(data_frame, text="Quantity",bg="Light blue")
        quanatity_label.grid(row=1, column=0, padx=10, pady=10)
        quanatity_entry = Entry(data_frame)
        quanatity_entry.grid(row=1, column=1, padx=10, pady=10)

        avaibality_label = Label(data_frame, text="Avaibality",bg="Light blue")
        avaibality_label.grid(row=1, column=2, padx=10, pady=10)
        avaibality_entry = Entry(data_frame)
        avaibality_entry.grid(row=1, column=3, padx=10, pady=10)


        Search_buttom=Button(data_frame,text="Search",command=checksearch,bg="red",fg="white")
        Search_buttom.place(x=650,y=47)
        search_entry = Entry(data_frame,)
        search_entry.place(x=500,y=50)

        # Update record
        def update_record():
            # Grab the record number
            selected = my_tree.focus()
            # # Update record
            my_tree.item(selected, text="", values=(id.get(), fn_entry.get(), rate_entry.get(), quanatity_entry.get(), avaibality_entry.get(),))
            
            # # Update the database
            conn = sqlite3.connect('admin.db')
            c = conn.cursor()
            c.execute("""  UPDATE  items SET 
                Itemname = :name,
                Rate = :Add,
                Quantity = :Pone,
                Avaibality = :User
                
                WHERE oid = :oid""",
                {
                    'name': fn_entry.get(),
                    'Add': rate_entry.get(),
                    'Pone': quanatity_entry.get(),
                    'User': avaibality_entry.get(),
                    'oid': id.get(),
                })
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Items updated Successfully") 


            # Clear entry boxes
            id.delete(0, END)
            fn_entry.delete(0, END)
            rate_entry.delete(0, END)
            quanatity_entry.delete(0, END)
            avaibality_entry.delete(0, END)
        #-----validation for update -------

        def check_ecord():
            a=fn_entry.get()
            b=rate_entry.get()
            c=quanatity_entry.get()
            d=avaibality_entry.get()

            if(a=="" or b=="" or c=="" or d==""):
                messagebox.showerror("Invalid","One or More Fields Empty.")
            else:
                update_record()



        def clear_entries():
            # Clear entry boxes
            id.delete(0, END)
            fn_entry.delete(0, END)
            rate_entry.delete(0, END)
            quanatity_entry.delete(0, END)
            avaibality_entry.delete(0, END)

        #=selection of record
        def select_record():

            clear_entries()
            selected = my_tree.focus()
            values = my_tree.item(selected, 'values')
            if not my_tree.selection():
                messagebox.showwarning("Warning","Data not Selected")
            else:
            # outpus to entry boxes
                id.insert(0, values[0])
                fn_entry.insert(0, values[1])
                rate_entry.insert(0, values[2])
                quanatity_entry.insert(0, values[3])
                avaibality_entry.insert(0, values[4])

                
        def logout():
            status=messagebox.askyesno(title="Warning",message="Do you  want to logout??")
            if status==True:
                frame_viewitems.destroy()
            else:
                pass
        # Add Buttons
        button_frame = LabelFrame(frame_viewitems, text="CRUD Operation",bg="Light blue")
        button_frame.pack(fill="x", expand="yes", padx=10)

        update_button = Button(button_frame, text="Update Record",command=check_ecord,bg="red",fg="white")
        update_button.grid(row=0, column=1, padx=10, pady=10)

        logout_button = Button(button_frame, text="Logout", command=logout,bg="red",fg="white")
        logout_button.grid(row=0, column=3, padx=10, pady=10)
        logout_button1 = Button(button_frame, text="Select record", command=select_record,bg="red",fg="white")
        logout_button1.grid(row=0, column=2, padx=10, pady=10)
        Button_change = Button(button_frame, text="Change Password", command=lambda:change(),bg="red",fg="white")
        Button_change.grid(row=0, column=4, padx=10, pady=10)

        query_database()

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
                    import_viewitems()
                
                    break             
            conn.commit()
            conn.close()
            


 

    #------Cancel Function----

    def cancel():
        status=messagebox.askyesno(title="Close",message="DO you really want to close? ")
        if status==True:
            frame_import.destroy()
            # import home
        else:
            pass



    def change():
      

        
        #===frame =====
        frame_forgetpassword=Frame(frame_import,bg="light blue")
        frame_forgetpassword.place(x=280,y=200,height=310,width=280)
        text=Label(frame_forgetpassword,text="Forget Password",font=("impact",14),bg="red",fg="white")
        text.place(x=45,y=10)
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
        


        text=Label(frame_forgetpassword,text="Username",fg="red",bg="light blue")
        old=Entry(frame_forgetpassword)
        old.place(x=45,y=70,width=150)
        text.place(x=50,y=45)
        A=Label(frame_forgetpassword,text="Fullname ",fg="red",bg="lightblue")
        A.place(x=50,y=95)
        new=Entry(frame_forgetpassword,)
        new.place(x=45,y=120,width=150)
        A=Label(frame_forgetpassword,text="New Password",fg="red",bg="light blue")
        A.place(x=50,y=145)
        re=Entry(frame_forgetpassword,)
        re.place(x=45,y=170,width=150)
        showw=IntVar(value=1)
        Checkbutton(frame_forgetpassword,text='Show',offvalue=0,variable=showw,bg='lightblue',command=show).place(x=210,y=172)
        A=Label(frame_forgetpassword,text="Re_type Password",fg="red",bg="light blue")
        A.place(x=50,y=195)
        re1=Entry(frame_forgetpassword,)
        re1.place(x=45,y=220,width=150)
        showww=IntVar(value=1)
        Checkbutton(frame_forgetpassword,text='Show',offvalue=0,variable=showww,bg='lightblue',command=show2).place(x=210,y=222) 

        

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
        
        def cancel_forget():
            frame_forgetpassword.destroy()


        B=Button(frame_forgetpassword, text="Change password",bg="red",fg="white",command=change_check,cursor="hand2",bd=1)
        B.place(x=160,y=280)
        cancel_Forget=Button(frame_forgetpassword, text="Cancel",bg="red",fg="white",command=cancel_forget,cursor="hand2",bd=1)
        cancel_Forget.place(x=10,y=280)


    B=Button(Frame_frame_import,text="Login",fg="white",bg="red",bd=0,cursor="hand2",command=check)
    B.place(x=65,y=180)

    C=Button(Frame_frame_import,text="Cancel" ,command=cancel,bd=0,fg="white",bg="red",cursor="hand2",)
    C.place(x=170,y=180)

    d=Button(Frame_frame_import,text="Forget Password?" ,command=change,bd=0,fg="blue",bg="light blue",cursor="hand2",)
    d.place(x=100,y=220)

def admin():
    frame_import_admin=Frame(Aces)
    frame_import_admin.place(x=0,y=0,height=600,width=700)

    global photo_admin
    my_pic=Image.open("Images//back1.png")
    resized=my_pic.resize((1270,670),Image.ANTIALIAS)
    photo_admin = ImageTk.PhotoImage(resized)
    background = Label(frame_import_admin, image = photo_admin).place(x=0, y=0) #since tkinter doesn't support background image, we place it as a label

    # photo2=PhotoImage(file='Images//crazy.png')
    # background = Label(frame_import_admin, image = photo2).place(x=320, y=20) #since tkinter doesn't support background image, we place it as a label


    #frame 
    Frame_frame_import_admin=Frame(frame_import_admin,bg="light blue")
    Frame_frame_import_admin.place(x=300,y=200,height=250,width=270)


    text=Label(Frame_frame_import_admin,text="Admin Log in here",bg="red",fg="white",bd=2,font=("impact",15," "))
    text.place(x=65,y=32)


    #--------------show---------

    def show():
        if (showw.get()==1):
            text2.config(show='')
        else:
            text2.config(show='*')


    text=Label(Frame_frame_import_admin,text="User name",fg="brown",bg="light blue")
    text1=Entry(Frame_frame_import_admin)
    text1.place(x=45,y=95,width=150)
    text.place(x=85,y=70)

    A=Label(Frame_frame_import_admin,text="Password",fg="brown",bg="light blue")
    text2=Entry(Frame_frame_import_admin,)
    text2.place(x=45,y=145,width=150)
    A.place(x=85,y=120)
    showw=IntVar(value=1)
    Checkbutton(Frame_frame_import_admin,text='show',offvalue=0,variable=showw,bg="light blue",bd=0,command=show).place(x=205,y=145)




    #------Cancel function----



    def cancel():
        status=messagebox.askyesno(title="Close",message="DO you really want to cancel? ")
        if status==True:
            frame_import_admin.destroy()
        else:
            pass

    #--------signup for Admin--------------------

    def adminsign():
      

        frame_adminsign=Frame(frame_import_admin,bg='lightblue',height=300,width=300)
        frame_adminsign.place(x=300,y=200)
        title=Label(frame_adminsign, text='Admin signup', bg="red", fg='white', font=('Arial',20,'bold'))
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
        

        
        A=Label(frame_adminsign, text='Username', bg="lightblue", fg='red')
        A.place(x=100, y=75)
        user_name=Entry(frame_adminsign)
        user_name.place(x=60, y=100,)

        B=Label(frame_adminsign, text='Password', bg="lightblue", fg='red')
        B.place(x=100, y=125)
        user_password=Entry(frame_adminsign)
        user_password.place(x=60, y=150,)
        showw=IntVar(value=1)
        Checkbutton(frame_adminsign,text='Show',offvalue=0,variable=showw,bg='lightblue',command=show).place(x=190,y=150)


    
        c=Label(frame_adminsign, text='Default Password', bg="lightblue", fg='red')
        c.place(x=70, y=175)
        user_default=Entry(frame_adminsign)
        user_default.place(x=60, y=200,)
        showww=IntVar(value=1)
        Checkbutton(frame_adminsign,text='Show',offvalue=0,variable=showww,bg='lightblue',command=show2).place(x=190,y=200) 
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
                    frame_adminsign.destroy()
                
                except:
                    pass
        def cancelsignup():
            frame_adminsign.destroy()




        
        BUttn_add=Button(frame_adminsign,text="Add",fg="white",bg="red",bd=2,cursor="hand2",command=Addadmin)
        BUttn_add.place(x=150,y=230)
        BUttn_cancel=Button(frame_adminsign,text="Cancel",fg="white",bg="red",bd=2,cursor="hand2",command=cancelsignup)
        BUttn_cancel.place(x=40,y=230)
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
                    adminhonepage()
                                    
                    break             
            conn.commit()
            conn.close()
    def adminhonepage():
        frame_import_adminhomepage=Frame(Aces)
        frame_import_adminhomepage.place(x=0,y=0,height=1270,width=700)
        
        global photoAdminhomepage
        my_pic=Image.open("Images//back1.png")
        resized=my_pic.resize((1270,670),Image.ANTIALIAS)
        photoAdminhomepage = ImageTk.PhotoImage(resized)
        background = Label(frame_import_adminhomepage, image = photoAdminhomepage)
        background.place(x=0, y=0) #since tkinter doesn't support background image, we place it as a label




        #-------frame---------
        Frame_frame_import_adminhomepage=LabelFrame(frame_import_adminhomepage,text="Data Query",bg="white")
        Frame_frame_import_adminhomepage.place(x=200,y=200,height=80,width=370)

        def homeadmin():

            frame_import_employeedata=Frame(Aces,bg="light green")
            frame_import_employeedata.place(x=0,y=0,height=670,width=1270)    
            # Create a database or connect to one that exists
            conn = sqlite3.connect('admin.db')
            c = conn.cursor()
            # Create Table
            try:
                c.execute("""CREATE TABLE if not exists employee 
                (Fullname text,
                Address text,
                Phone text,
                Username text,
                Password text,
                Salary text)
                """)
            except:
                pass


            conn.commit()
            conn.close()

            def query_database():
                # Create a database or connect to one that exists
                conn = sqlite3.connect('admin.db')
                c = conn.cursor()

                c.execute("SELECT rowid, * FROM employee")
                records = c.fetchall()
                
                # Add our data to the screen
                global count
                count = 0

                for record in records:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow',))
                    else:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('oddrow',))
                    # increment counter
                    count += 1


                conn.commit()
                conn.close()
            #===clear search====
            def search_clear():
                    search_entry.delete(0, END)


            def search_records():
                lookup_record = search_entry.get()

                # Clear the Treeview
                for record in my_tree.get_children():
                    my_tree.delete(record)
                conn = sqlite3.connect('admin.db')
                c = conn.cursor()

                c.execute("SELECT rowid, * FROM employee WHERE Fullname like ?", (lookup_record,))
                records = c.fetchall()
                
                # Add our data to the screen
                global count
                count = 0
                for record in records:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow',))
                    else:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('oddrow',))
                    # increment counter
                    count += 1
                
                conn.commit()
                conn.close()
                search_clear()




            def checksearch():
                if search_entry.get()=="":
                    messagebox.showerror("Invalid","Search Fields Empty.")
                else:
                    search_records()             


            # Add Some Style in tree
            style = ttk.Style()

            # Pick A Theme
            style.theme_use('default')

            # Configure the Treeview Colors
            style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=30,
                fieldbackground="Light blue")

            # Change Selected Color
            style.map('Treeview',
                background=[('selected', "red")])
            #===================image for treeview================
            global photo5_employeephoto
            my_pic1=Image.open("Images//front.png")
            resized=my_pic1.resize((948,40),Image.ANTIALIAS)
            photo5_employeephoto= ImageTk.PhotoImage(resized)
            # Create a Treeview Frame
            tree_frame = Frame(frame_import_employeedata,bg="light blue")
            tree_frame.pack(pady=10)
            text=Label(tree_frame,image=photo5_employeephoto,bg='light blue')
            text.pack(side=TOP)

            # Create a Treeview Scrollbar
            tree_scroll = Scrollbar(tree_frame)
            tree_scroll.pack(side=RIGHT, fill=Y)

            # Create The Treeview
            my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
            my_tree.pack()

            # Configure the Scrollbar
            tree_scroll.config(command=my_tree.yview)

            # Define Our Columns
            my_tree['columns'] = ("ID", "Fullname", "Address", "Phone", "Username", "Password", "Salary")

            # Format Our Columns
            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("ID", anchor=W, width=60)
            my_tree.column("Fullname", anchor=W, width=180)
            my_tree.column("Address", anchor=CENTER, width=120)
            my_tree.column("Phone", anchor=CENTER, width=140)
            my_tree.column("Username", anchor=CENTER, width=140)
            my_tree.column("Password", anchor=CENTER, width=140)
            my_tree.column("Salary", anchor=CENTER, width=140)


            # Create Headings
            my_tree.heading("#0", text="", anchor=W)
            my_tree.heading("ID", text="ID", anchor=W)
            my_tree.heading("Fullname", text="Fullname", anchor=W)
            my_tree.heading("Address", text="Address", anchor=CENTER)
            my_tree.heading("Phone", text="Phone", anchor=CENTER)
            my_tree.heading("Username", text="Username", anchor=CENTER)
            my_tree.heading("Password", text="Password", anchor=CENTER)
            my_tree.heading("Salary", text="Salary", anchor=CENTER)


            # Create Striped Row Tags
            my_tree.tag_configure('oddrow', background="green")
            my_tree.tag_configure('evenrow', background="lightgreen")



            # Add Record Entry Boxes
            data_frame = LabelFrame(frame_import_employeedata, text="Record of employee working in crazy Store",bg="light blue")
            data_frame.pack(fill="x", expand="yes", padx=20)

            id = Label(data_frame, text="ID",bg="light blue")
            id.grid(row=0, column=0, padx=10, pady=10)
            id = Entry(data_frame)
            id.grid(row=0, column=1, padx=10, pady=10)

            fn_label = Label(data_frame, text="Fullname",bg="light blue")
            fn_label.grid(row=0, column=2, padx=10, pady=10)
            fn_entry = Entry(data_frame)
            fn_entry.grid(row=0, column=3, padx=10, pady=10)

            Address_label = Label(data_frame, text="Address",bg="light blue")
            Address_label.grid(row=0, column=4, padx=10, pady=10)
            Address_entry = Entry(data_frame)
            Address_entry.grid(row=0, column=5, padx=10, pady=10)

            phone_label = Label(data_frame, text="Phone",bg="light blue")
            phone_label.grid(row=0, column=6, padx=10, pady=10)
            phone_entry = Entry(data_frame)
            phone_entry.grid(row=0, column=7, padx=10, pady=10)

            Username_label = Label(data_frame, text="Username",bg="light blue")
            Username_label.grid(row=1, column=2, padx=10, pady=10)
            Username_entry = Entry(data_frame)
            Username_entry.grid(row=1, column=3, padx=10, pady=10)

            Password_label = Label(data_frame, text="Password",bg="light blue")
            Password_label.grid(row=1, column=4, padx=10, pady=10)
            Password_entry = Entry(data_frame)
            Password_entry.grid(row=1, column=5, padx=10, pady=10)

            Salary_label = Label(data_frame, text="Salary",bg="light blue")
            Salary_label.grid(row=1, column=6, padx=10, pady=10)
            Salary_entry = Entry(data_frame)
            Salary_entry.grid(row=1, column=7, padx=10, pady=10)

            Search_buttom=Button(data_frame,text="Search",command=checksearch,bg="red",fg="white")
            Search_buttom.place(x=1030,y=7)
            search_entry = Entry(data_frame,)
            search_entry.place(x=880,y=10)



            def clear_entries():
                # Clear entry boxes
                id.delete(0, END)
                fn_entry.delete(0, END)
                Address_entry.delete(0, END)
                phone_entry.delete(0, END)
                Username_entry.delete(0, END)
                Password_entry.delete(0, END)
                Salary_entry.delete(0, END)


            # Select Record
            def select_record():

                clear_entries()
                selected = my_tree.focus()
                values = my_tree.item(selected, 'values')
                if not my_tree.selection():
                    messagebox.showwarning("Warning","Data not Selected")
                else:
                # output to entry boxes
                    id.insert(0, values[0])
                    fn_entry.insert(0, values[1])
                    Address_entry.insert(0, values[2])
                    phone_entry.insert(0, values[3])
                    Username_entry.insert(0, values[4])
                    Password_entry.insert(0, values[5])
                    Salary_entry.insert(0, values[6])

            # Update record
            def update_record():
                # Grab the record number
                selected = my_tree.focus()
                my_tree.item(selected, text="", values=( id.get(), fn_entry.get(), Address_entry.get(), phone_entry.get(), Username_entry.get(), Password_entry.get(), Salary_entry.get(),))
                
                conn = sqlite3.connect('admin.db')

                c = conn.cursor()

                c.execute("""  UPDATE  employee SET 
                    Fullname = :name,
                    Address = :Add,
                    Phone = :Pone,
                    Username = :User,
                    Password = :Pass,
                    Salary = :fee
                    WHERE oid = :oid""",
                    {
                        'name': fn_entry.get(),
                        'Add': Address_entry.get(),
                        'Pone': phone_entry.get(),
                        'User': Username_entry.get(),
                        'Pass': Password_entry.get(),
                        'fee': Salary_entry.get(),
                        'oid': id.get(),
                    })
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Employee updated Successfully") 


                # Clear entry boxes
                id.delete(0, END)
                fn_entry.delete(0, END)
                Address_entry.delete(0, END)
                phone_entry.delete(0, END)
                Username_entry.delete(0, END)
                Password_entry.delete(0, END)
                Salary_entry.delete(0, END)



            #=========validation for updates==========
            def check_updates():
                g=id.get()
                a=fn_entry.get()
                b=Address_entry.get()
                c=phone_entry.get()
                d=Username_entry.get()
                e=Password_entry.get()
                f=Salary_entry.get()
                H=d.find("@")

                if(a=="" or b=="" or c=="" or d=="" or e=="" or f=="" or g==""):
                    messagebox.showerror("Invalid","One or More Fields Empty.")
                elif H!=0:
                    messagebox.showerror("Invalid","Username should start with @")                     

                elif len(c)!=10:
                    messagebox.showerror("Invalid","Invalid phone number.")
                elif len(e)<6:
                    messagebox.showerror("invalid","Password should ba atleast 6 characters!")
                elif d==e or e==a:
                    messagebox.showerror("error password","Password should not be username or fullname!!")
                else:
                    try:
                        int(c)
                        update_record()            
                    except:
                        messagebox.showerror("Invalid","Invalid Phone Number")
                

            # Remove one record
            def remove_one():
                conn = sqlite3.connect('admin.db')
                c = conn.cursor()

                if not my_tree.selection():
                    messagebox.showwarning("Warning","Select data to delete")
                else:
                    result = messagebox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                                    icon="warning")
                    if result == 'yes':
                            curItem = my_tree.focus()
                            contents = (my_tree.item(curItem))
                            selecteditem = contents['values']
                            my_tree.delete(curItem)
                            cursor=conn.execute("DELETE FROM employee WHERE oid = %d" % selecteditem[0])
                            conn.commit()
                            cursor.close()
                            conn.close()
                            messagebox.showinfo("Success","Data deleted successfully!")


            def adduser():
                conn=sqlite3.connect('admin.db')
                c=conn.cursor()
                c.execute("INSERT INTO employee VALUES ( :Fullname, :Address, :Phone, :Username, :Password, :Salary)",
                {
                "Fullname":fn_entry.get() ,
                "Address":Address_entry.get(),
                "Phone":phone_entry.get() ,
                "Username":Username_entry.get() ,
                "Password":Password_entry.get() ,
                "Salary":Salary_entry.get() 
                })
                conn.commit()
                conn.close()

                messagebox.showinfo("Success","Employee added Successfully") 
                clear_entries()

                #=====autoupdate treeview===
                my_tree.delete(*my_tree.get_children())
                query_database()


            def check():
                a=fn_entry.get()
                b=Address_entry.get()
                c=phone_entry.get()
                d=Username_entry.get()
                e=Password_entry.get()
                f=Salary_entry.get()
                H=d.find("@")

                if(a=="" or b=="" or c=="" or d=="" or e=="" or f==""):
                    messagebox.showerror("Invalid","One or More Fields Empty.")
                elif H!=0:
                    messagebox.showerror("Invalid","Username should start with @")                   
                elif len(c)!=10:
                    messagebox.showerror("Invalid","Invalid phone number.")
                elif len(e)<6:
                    messagebox.showerror("invalid","Password should ba atleast 6 characters!")
                elif d==e or e==a:
                    messagebox.showerror("error password","Password should not be username or fullname!!")
                else:
                    try:
                        int(c)
                        adduser()            
                    except:
                        messagebox.showerror("Invalid","Invalid Phone Number")
                

            def logout():
                status=messagebox.askyesno(title="Warning",message="Do you really want to go back??")
                if status==True:
                    frame_import_employeedata.destroy()
                else:
                    pass

            # Add Buttons
            button_frame = LabelFrame(frame_import_employeedata, text="CRUD Operation",bg="light blue")
            button_frame.pack(fill="x", expand="yes", padx=10)



            update_button = Button(button_frame, text="Update Record", command=check_updates,bg="red",fg="white")
            update_button.grid(row=0, column=0, padx=10, pady=10)

            add_button = Button(button_frame, text="Add Record", command=check,bg="red",fg="white")
            add_button.grid(row=0, column=1, padx=10, pady=10)


            remove_button = Button(button_frame, text="Delete", command=remove_one,bg="red",fg="white")
            remove_button.grid(row=0, column=2, padx=10, pady=10)
            logout_button = Button(button_frame, text="Back", command=logout,bg="red",fg="white")
            logout_button.grid(row=0, column=4, padx=10, pady=10)


            logout_button1 = Button(button_frame, text="Select Record", command=select_record,bg="red",fg="white")
            logout_button1.grid(row=0, column=3, padx=10, pady=10)


            query_database()
            
        #######################################################################
        #==================================================
        ##
        #
        #items data

        def Addhome():
            frame_import_itemsdata=Frame(Aces)
            frame_import_itemsdata.place(x=0,y=0,height=650,width=800)
            conn = sqlite3.connect('admin.db')
            c = conn.cursor()

            try:
                c.execute("""CREATE TABLE if not exists items (
                Itemname text,
                Rate text,
                Quantity text,
                Avaibality text)
                """)
            except:
                pass

            conn.commit()
            conn.close()



            def query_database():
                # Create a database or connect to one that exists
                conn = sqlite3.connect('admin.db')

                # Create a cursor instance
                c = conn.cursor()

                c.execute("SELECT rowid, * FROM items")
                records = c.fetchall()
                
                # Add our data to the screen
                global count
                count = 0

                for record in records:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4]), tags=('evenrow',))
                    else:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4]), tags=('oddrow',))
                    # increment counter
                    count += 1

                # Commit changes
                conn.commit()

                # Close our connection
                conn.close()




            # Add Some Style
            style = ttk.Style()

            # Pick A Theme
            style.theme_use('default')

            # Configure the Treeview Colors
            style.configure("Treeview",
                background="#D3D3D3",
                foreground="Black",
                rowheight=25,
                fieldbackground="light blue")

            # Change Selected Color
            style.map('Treeview',
                background=[('selected', "red")])

            #========image for frame=====
            global photo_itemsdata
            my_pic1=Image.open("Images//items.png")
            resized=my_pic1.resize((753,40),Image.ANTIALIAS)
            photo_itemsdata = ImageTk.PhotoImage(resized)


            # Create a Treeview Frame
            tree_frame = Frame(frame_import_itemsdata,height=5,bg="light blue")
            tree_frame.pack(pady=10)

            text=Label(tree_frame,image=photo_itemsdata,bg='light blue')
            text.pack(side=TOP)

            # Create a Treeview Scrollbar
            tree_scroll = Scrollbar(tree_frame)
            tree_scroll.pack(side=RIGHT, fill=Y)

            # Create The Treeview
            my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
            my_tree.pack()

            # Configure the Scrollbar
            tree_scroll.config(command=my_tree.yview)



            #=====search iteam====

            def search_records():
                lookup_record = search_entry.get()

                # Clear the Treeview
                for record in my_tree.get_children():
                    my_tree.delete(record)
                conn = sqlite3.connect('admin.db')
                c = conn.cursor()

                c.execute("SELECT rowid, * FROM items WHERE Itemname like ?", (lookup_record,))
                records = c.fetchall()
                
                # Add our data to the screen
                global count
                count = 0
                
                for record in records:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3],record[4]), tags=('evenrow',))
                    else:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3],record[4]), tags=('oddrow',))
                    # increment counter
                    count += 1


                conn.commit()
                conn.close()
            def checksearch():
                if search_entry.get()=="":
                    messagebox.showerror("Invalid","Search Fields Empty.")
                else:
                    search_records()



            # Define Our Columns
            my_tree['columns'] = ("ID", "Itemname", "Rate", "Quantity", "Avaibality")

            # Format Our Columns
            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("ID", anchor=W, width=50)
            my_tree.column("Itemname", anchor=W, width=200)
            my_tree.column("Rate", anchor=CENTER, width=150)
            my_tree.column("Quantity", anchor=CENTER, width=150)
            my_tree.column("Avaibality", anchor=CENTER, width=170)


            # Create Headings
            my_tree.heading("#0", text="", anchor=W)
            my_tree.heading("ID", text="ID", anchor=W,)
            my_tree.heading("Itemname", text="Items name", anchor=W)
            my_tree.heading("Rate", text="Rate", anchor=CENTER)
            my_tree.heading("Quantity", text="Quantity", anchor=CENTER)
            my_tree.heading("Avaibality", text="Avaibality", anchor=CENTER)

            # Create Striped Row Tags
            my_tree.tag_configure('oddrow', background="green")
            my_tree.tag_configure('evenrow', background="lightgreen")

            # Add Record Entry Boxes
            data_frame = LabelFrame(frame_import_itemsdata, text="Record of merchandise",bg="light blue")
            data_frame.pack(fill="x", expand="yes", padx=10)

            id = Label(data_frame, text="ID",bg="Light blue")
            id.grid(row=0, column=0, padx=10, pady=10)
            id = Entry(data_frame)
            id.grid(row=0, column=1, padx=10, pady=10)

            fn_label = Label(data_frame, text="Itemname",bg="light blue")
            fn_label.grid(row=0, column=2, padx=10, pady=10)
            fn_entry = Entry(data_frame)
            fn_entry.grid(row=0, column=3, padx=10, pady=10)

            rate_label = Label(data_frame, text="Rate",bg="light blue")
            rate_label.grid(row=0, column=4, padx=10, pady=10)
            rate_entry = Entry(data_frame)
            rate_entry.grid(row=0, column=5, padx=10, pady=10)

            quanatity_label = Label(data_frame, text="Quantity",bg="light blue")
            quanatity_label.grid(row=1, column=0, padx=10, pady=10)
            quanatity_entry = Entry(data_frame)
            quanatity_entry.grid(row=1, column=1, padx=10, pady=10)

            avaibality_label = Label(data_frame, text="Avaibality",bg="light blue")
            avaibality_label.grid(row=1, column=2, padx=10, pady=10)
            avaibality_entry = Entry(data_frame)
            avaibality_entry.grid(row=1, column=3, padx=10, pady=10)

            Search_buttom=Button(data_frame,text="Search",command=checksearch,bg="red",fg="white")
            Search_buttom.place(x=650,y=47)
            search_entry = Entry(data_frame,)
            search_entry.place(x=500,y=50)



            def clear_entries():
                # Clear entry boxes
                id.delete(0, END)
                fn_entry.delete(0, END)
                rate_entry.delete(0, END)
                quanatity_entry.delete(0, END)
                avaibality_entry.delete(0,END)

                
            def select_record():

                clear_entries()

                selected = my_tree.focus()	
                values = my_tree.item(selected, 'values')
                if not my_tree.selection():
                    messagebox.showwarning("Warning","Data not Selected")
                else:
                # output to entry boxes
                    id.insert(0, values[0])
                    fn_entry.insert(0, values[1])
                    rate_entry.insert(0, values[2])
                    quanatity_entry.insert(0, values[3])
                    avaibality_entry.insert(0, values[4])

                
            # Update record
            def update_record():
                # Grab the record number
                selected = my_tree.focus()
                # # Update record
                my_tree.item(selected, text="", values=( id.get(), fn_entry.get(), rate_entry.get(), quanatity_entry.get(), avaibality_entry.get(),))
                
                # # Update the database
                conn = sqlite3.connect('admin.db')
                c = conn.cursor()
                c.execute("""  UPDATE  items SET 
                    Itemname = :name,
                    Rate = :Add,
                    Quantity = :Pone,
                    Avaibality = :User

                    WHERE oid = :oid""",

                    {
                        'name': fn_entry.get(),
                        'Add': rate_entry.get(),
                        'Pone': quanatity_entry.get(),
                        'User': avaibality_entry.get(),
                        'oid': id.get(),
                    })
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Items Updated Successfully") 


                # Clear entry boxes
                id.delete(0, END)
                fn_entry.delete(0, END)
                rate_entry.delete(0, END)
                quanatity_entry.delete(0, END)
                avaibality_entry.delete(0, END)


            def check_ecord():
                a=fn_entry.get()
                b=rate_entry.get()
                c=quanatity_entry.get()
                d=avaibality_entry.get()

                if(a=="" or b=="" or c=="" or d==""):
                    messagebox.showerror("Invalid","One or More Fields Empty.")
                else:
                    update_record()


            def remove_one():
                conn = sqlite3.connect('admin.db')
                c = conn.cursor()

                if not my_tree.selection():
                    messagebox.showwarning("Warning","Select data to delete")
                else:
                    result = messagebox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                                    icon="warning")
                    if result == 'yes':
                            curItem = my_tree.focus()
                            contents = (my_tree.item(curItem))
                            selecteditem = contents['values']
                            my_tree.delete(curItem)
                            cursor=conn.execute("DELETE FROM items WHERE oid = %d" % selecteditem[0])
                            conn.commit()
                            cursor.close()
                            conn.close()
                            messagebox.showinfo("Success","Data deleted successfully!")
            
            def logout():
                status=messagebox.askyesno(title="Warning",message="Do you  want to go back??")
                if status==True:
                    frame_import_itemsdata.destroy()
                else:
                    pass



            def additems():
                conn=sqlite3.connect('admin.db')
                c=conn.cursor()
                c.execute("INSERT INTO items VALUES ( :Itemname, :Rate, :Quantity, :Avaibality)",
                {
                "Itemname":fn_entry.get() ,
                "Rate":rate_entry.get(),
                "Quantity":quanatity_entry.get() ,
                "Avaibality":avaibality_entry.get() ,
                    })
                conn.commit()
                conn.close() 
                
                messagebox.showinfo("Success","Items added Successfully") 
                clear_entries()
                #=====autoupdate treeview===
                my_tree.delete(*my_tree.get_children())
                query_database()

            def check():
                a=fn_entry.get()
                b=rate_entry.get()
                c=quanatity_entry.get()
                d=avaibality_entry.get()
                e=id.get()

                if(a=="" or b=="" or c=="" or d=="" or e==""):
                    messagebox.showerror("Invalid","One or More Fields Empty.")
                else:
                    additems()
            

            # Add Buttons
            button_frame = LabelFrame(frame_import_itemsdata, text="CRUD Operation",bg="light blue")
            button_frame.pack(fill="x", expand="yes", padx=10)


            update_button = Button(button_frame, text="Update Record",bg="red",fg="white",command=check_ecord)
            update_button.grid(row=0, column=1, padx=10, pady=10)

            update_button = Button(button_frame, text="Add Record",command=check,bg="red",fg="white" )
            update_button.grid(row=0, column=2, padx=10, pady=10)

            update_button = Button(button_frame, text="Delete Record",command=remove_one,bg="red",fg="white" )
            update_button.grid(row=0, column=3, padx=10, pady=10)


            update_button = Button(button_frame, text="Back", command=logout,bg="red",fg="white")
            update_button.grid(row=0, column=5, padx=10, pady=10)

            logout_button1 = Button(button_frame, text="Select record", command=select_record,bg="red",fg="white")
            logout_button1.grid(row=0, column=4, padx=10, pady=10)

            query_database()

        #=========image in button===========
        global photo_employee
        global photo_items
        global photo_admindata
        global photo_logout

        my_pic1=Image.open("Images//employeedata.png")
        resized=my_pic1.resize((80,30),Image.ANTIALIAS)
        photo_employee = ImageTk.PhotoImage(resized)
        #button 
        C=Button(Frame_frame_import_adminhomepage,image=photo_employee,cursor="hand2",command= homeadmin)
        C.place(x=3,y=10)


        my_pic2=Image.open("Images//itemsdata.png")
        resized=my_pic2.resize((80,30),Image.ANTIALIAS)
        photo_items = ImageTk.PhotoImage(resized)
        D=Button(Frame_frame_import_adminhomepage,image=photo_items,cursor="hand2",command=Addhome)
        D.place(x=94,y=10)


        def cancel():
            status=messagebox.askyesno(title="Close",message="DO you really want to logout? ")
            if status==True:
                frame_import_adminhomepage.destroy()                
            else:
                pass
        def admindata():
            frame_import_admintable=Frame(Aces)
            frame_import_admintable.place(x=0,y=0,height=670,width=600)
            conn = sqlite3.connect('admin.db')
            c = conn.cursor()

            try:
                c.execute("""CREATE TABLE if not exists admin (
                Itemname text,
                Rate text,
                Quantity text,
                Avaibality text)
                """)
            except:
                pass

            conn.commit()
            conn.close()



            def query_database():
                # Create a database or connect to one that exists
                conn = sqlite3.connect('admin.db')

                # Create a cursor instance
                c = conn.cursor()

                c.execute("SELECT rowid, * FROM admin")
                records = c.fetchall()
                
                # Add our data to the screen
                global count
                count = 0

                for record in records:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
                    else:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('oddrow',))
                    # increment counter
                    count += 1

                # Commit changes
                conn.commit()

                # Close our connection
                conn.close()




            # Add Some Style
            style = ttk.Style()

            # Pick A Theme
            style.theme_use('default')

            # Configure the Treeview Colors
            style.configure("Treeview",
                background="#D3D3D3",
                foreground="Black",
                rowheight=25,
                fieldbackground="light blue")

            # Change Selected Color
            style.map('Treeview',
                background=[('selected', "red")])

            #========image for frame=====
            global photo5_Admins_photo
            my_pic1=Image.open("Images//record.png")
            resized=my_pic1.resize((480,35),Image.ANTIALIAS)
            photo5_Admins_photo= ImageTk.PhotoImage(resized)


            # Create a Treeview Frame
            tree_frame = Frame(frame_import_admintable,height=5,bg="light blue")
            tree_frame.pack(pady=10)

            text=Label(tree_frame,image=photo5_Admins_photo,bg='light blue')
            text.pack(side=TOP)

            # Create a Treeview Scrollbar
            tree_scroll = Scrollbar(tree_frame)
            tree_scroll.pack(side=RIGHT, fill=Y)

            # Create The Treeview
            my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
            my_tree.pack()

            # Configure the Scrollbar
            tree_scroll.config(command=my_tree.yview)



            # Define Our Columns
            my_tree['columns'] = ("ID", "Admin_username", "Admin_password")

            # Format Our Columns
            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("ID", anchor=W, width=50)
            my_tree.column("Admin_username", anchor=W, width=200)
            my_tree.column("Admin_password", anchor=CENTER, width=150)



            # Create Headings
            my_tree.heading("#0", text="", anchor=W)
            my_tree.heading("ID", text="ID", anchor=W,)
            my_tree.heading("Admin_username", text="Admin_username", anchor=W)
            my_tree.heading("Admin_password", text="Admin_password", anchor=CENTER)

            # Create Striped Row Tags
            my_tree.tag_configure('oddrow', background="green")
            my_tree.tag_configure('evenrow', background="lightgreen")

            # Add Record Entry Boxes
            data_frame = LabelFrame(frame_import_admintable, text="Record of Admin",bg="light blue")
            data_frame.pack(fill="x", expand="yes", padx=10)

            id = Label(data_frame, text="ID",bg="Light blue")
            id.grid(row=0, column=0, padx=10, pady=10)
            id = Entry(data_frame)
            id.grid(row=0, column=1, padx=10, pady=10)

            fn_label = Label(data_frame, text="Username",bg="light blue")
            fn_label.grid(row=0, column=2, padx=10, pady=10)
            fn_entry = Entry(data_frame)
            fn_entry.grid(row=0, column=3, padx=10, pady=10)

            password_label = Label(data_frame, text="Password",bg="light blue")
            password_label.grid(row=1, column=0, padx=10, pady=10)
            password_entry = Entry(data_frame)
            password_entry.grid(row=1, column=1, padx=10, pady=10)





            def clear_entries():
                # Clear entry boxes
                id.delete(0, END)
                fn_entry.delete(0, END)
                password_entry.delete(0, END)


                
            def select_record():

                clear_entries()

                selected = my_tree.focus()	
                values = my_tree.item(selected, 'values')
                if not my_tree.selection():
                    messagebox.showwarning("Warning","Data not Selected")
                else:
                # output to entry boxes
                    id.insert(0, values[0])
                    fn_entry.insert(0, values[1])
                    password_entry.insert(0, values[2])
                    

                
            # Update record
            def update_record():
                # Grab the record number
                selected = my_tree.focus()
                # # Update record
                my_tree.item(selected, text="", values=( id.get(), fn_entry.get(), password_entry.get()))
                
                # # Update the database
                conn = sqlite3.connect('admin.db')
                c = conn.cursor()
                c.execute("""  UPDATE  admin SET 
                    Admin_username = :name,
                    Admin_password = :Add		

                    WHERE oid = :oid""",

                    {
                        'name': fn_entry.get(),
                        'Add': password_entry.get(),
                        
                        'oid': id.get(),
                    })
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Data Updated Successfully") 


                # Clear entry boxes
                id.delete(0, END)
                fn_entry.delete(0, END)
                password_entry.delete(0, END)
                

            def check_ecord():
                a=fn_entry.get()
                b=password_entry.get()
                

                if(a=="" or b==""):
                    messagebox.showerror("Invalid","One or More Fields Empty.")
                else:
                    update_record()


            def remove_one():
                conn = sqlite3.connect('admin.db')
                c = conn.cursor()

                if not my_tree.selection():
                    messagebox.showwarning("Warning","Select data to delete")
                else:
                    result = messagebox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                                    icon="warning")
                    if result == 'yes':
                            curItem = my_tree.focus()
                            contents = (my_tree.item(curItem))
                            selecteditem = contents['values']
                            my_tree.delete(curItem)
                            cursor=conn.execute("DELETE FROM admin WHERE oid = %d" % selecteditem[0])
                            conn.commit()
                            cursor.close()
                            conn.close()
                            messagebox.showinfo("Success","Data deleted successfully!")
            
            def logout():
                status=messagebox.askyesno(title="Warning",message="Do you  want to go back??")
                if status==True:
                    frame_import_admintable.destroy()
                else:
                    pass



            

            # Add Buttons
            button_frame = LabelFrame(frame_import_admintable, text="CRUD Operation",bg="light blue")
            button_frame.pack(fill="x", expand="yes", padx=10)

            update_button = Button(button_frame, text="Update Record",bg="red",fg="white",command=check_ecord)
            update_button.grid(row=0, column=1, padx=10, pady=10)


            update_button = Button(button_frame, text="Delete Record",command=remove_one,bg="red",fg="white" )
            update_button.grid(row=0, column=3, padx=10, pady=10)


            update_button = Button(button_frame, text="Back", command=logout,bg="red",fg="white")
            update_button.grid(row=0, column=5, padx=10, pady=10)

            logout_button1 = Button(button_frame, text="Select record", command=select_record,bg="red",fg="white")
            logout_button1.grid(row=0, column=4, padx=10, pady=10)






            query_database()


        my_pic3=Image.open("Images//logout.png")
        resized=my_pic3.resize((80,30),Image.ANTIALIAS)
        photo_logout= ImageTk.PhotoImage(resized)
        E=Button(Frame_frame_import_adminhomepage,image=photo_logout,cursor="hand2",command=cancel)
        E.place(x=277,y=10)


        my_pic4=Image.open("Images//admindata.png")
        resized=my_pic4.resize((80,30),Image.ANTIALIAS)
        photo_admindata = ImageTk.PhotoImage(resized)
        E=Button(Frame_frame_import_adminhomepage,image=photo_admindata,cursor="hand2",command=admindata)
        E.place(x=186,y=10)

    B=Button(Frame_frame_import_admin,text="Login",fg="white",bg="red",bd=0,cursor="hand2",command=check)
    B.place(x=65,y=180)

    BUttn_b=Button(Frame_frame_import_admin,text="Cancel",fg="white",bg="red",bd=0,cursor="hand2",command=cancel)
    BUttn_b.place(x=180,y=180)

    BUttn_sign=Button(Frame_frame_import_admin,text="Register here!",bg="lightblue",fg="blue",bd=0,cursor="hand2",command=adminsign)
    BUttn_sign.place(x=110,y=230)

#================
#=============
#----------------
#Buttons for homepage
#creating buttons

B=Button(Frame_Aces,image=photo6,command=employee,cursor="hand2",bd=1)
B.place(x=35,y=150)

C=Button(Frame_Aces,image=photo5,cursor="hand2",command=admin,bd=1)
C.place(x=220,y=150)
 


Aces.mainloop()
