from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from PIL import ImageTk,Image

root = Tk()
root.title('Crazy store')
#icon for window
photo = PhotoImage(file ='Images//logo.png')
root.iconphoto(True, photo) #window icon
root.geometry("1000x550")
root.resizable(False,False)


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
	rowheight=25,
	fieldbackground="Light blue")

# Change Selected Color
style.map('Treeview',
	background=[('selected', "red")])
#===================image for treeview================
my_pic1=Image.open("Images//front.png")
resized=my_pic1.resize((948,40),Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(resized)
# Create a Treeview Frame
tree_frame = Frame(root,bg="light blue")
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
data_frame = LabelFrame(root, text="Record of employee working in crazy Store",bg="light blue")
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
phone_label.grid(row=1, column=0, padx=10, pady=10)
phone_entry = Entry(data_frame)
phone_entry.grid(row=1, column=1, padx=10, pady=10)

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
Search_buttom.place(x=830,y=7)
search_entry = Entry(data_frame,)
search_entry.place(x=680,y=10)



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
		root.destroy()
		import adminhomepage
	else:
		pass

# Add Buttons
button_frame = LabelFrame(root, text="CRUD Operation",bg="light blue")
button_frame.pack(fill="x", expand="yes", padx=20)


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

root.mainloop()