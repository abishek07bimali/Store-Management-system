from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from PIL import ImageTk,Image




root = Tk()
root.title('Admin table')
# # icon for window
photo = PhotoImage(file ='logo.png')
root.iconphoto(True, photo) #window icon
root.geometry("500x550")
root.resizable(False,False)


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
my_pic1=Image.open("record.png")
resized=my_pic1.resize((480,35),Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(resized)


# Create a Treeview Frame
tree_frame = Frame(root,height=5,bg="light blue")
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
data_frame = LabelFrame(root, text="Record of Admin",bg="light blue")
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
		root.destroy()
		import adminhomepage
	else:
		pass



  

# Add Buttons
button_frame = LabelFrame(root, text="CRUD Operation",bg="light blue")
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

root.mainloop()