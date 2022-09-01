from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from PIL import ImageTk,Image



root = Tk()
root.title('Items data')
# # icon for window
photo = PhotoImage(file ='logo.png')
root.iconphoto(True, photo) #window icon
root.geometry("800x550")
root.resizable(False,False)


my_menu=Menu(root)
root.config(menu=my_menu)
file_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=file_menu)
file_menu.add_cascade(label="Setting",command=lambda:change())


def change():
    top=Toplevel()
    top.geometry('300x330')
    top.title('Change Password')
    top.resizable(width=False,height=False)

	#===frame =====
    frame_top=Frame(top,bg="light blue")
    frame_top.place(x=10,y=5,height=290,width=300)

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

    text=Label(frame_top,text="Change Password",font=("impact",14),bg="red",fg="white").place(x=35,y=10)


    text=Label(frame_top,text="Username",fg="red",bg="light blue")
    old=Entry(frame_top)
    old.place(x=45,y=70,width=150)
    text.place(x=50,y=45)
    A=Label(frame_top,text="Current Password",fg="red",bg="lightblue")
    A.place(x=50,y=95)
    new=Entry(frame_top,)
    new.place(x=45,y=120,width=150)
    showw1=IntVar(value=1)
    Checkbutton(top,text='Show',offvalue=0,variable=showw1,bg='lightblue',command=show3).place(x=210,y=122)
    
	
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

        
    B=Button(top, text=" Update password",bg="red",fg="white",command=change_check,cursor="hand2",bd=1)
    B.place(x=70,y=280)
   

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
my_pic1=Image.open("items.png")
resized=my_pic1.resize((753,40),Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(resized)

# Create a Treeview Frame
tree_frame = Frame(root,height=5,bg="Light blue")
tree_frame.pack(pady=10)

text=Label(tree_frame,image=photo5,bg='light blue')
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
data_frame = LabelFrame(root, text="Record of merchandise",bg="Light blue")
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
		root.destroy()
		import employelogin
	else:
		pass
# Add Buttons
button_frame = LabelFrame(root, text="CRUD Operation",bg="Light blue")
button_frame.pack(fill="x", expand="yes", padx=10)

update_button = Button(button_frame, text="Update Record",command=check_ecord,bg="red",fg="white")
update_button.grid(row=0, column=1, padx=10, pady=10)

logout_button = Button(button_frame, text="Logout", command=logout,bg="red",fg="white")
logout_button.grid(row=0, column=3, padx=10, pady=10)
logout_button1 = Button(button_frame, text="Select record", command=select_record,bg="red",fg="white")
logout_button1.grid(row=0, column=2, padx=10, pady=10)

query_database()

root.mainloop()