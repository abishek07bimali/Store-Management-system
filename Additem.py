
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from PIL import ImageTk,Image




root = Tk()
root.title('Items data')
# # icon for window
photo = PhotoImage(file ='Images//logo.png')
root.iconphoto(True, photo) #window icon
root.geometry("800x550")
root.resizable(False,False)




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
my_pic1=Image.open("Images//items.png")
resized=my_pic1.resize((753,40),Image.ANTIALIAS)
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
data_frame = LabelFrame(root, text="Record of merchandise",bg="light blue")
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
		root.destroy()
		import adminhomepage
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
button_frame = LabelFrame(root, text="CRUD Operation",bg="light blue")
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

root.mainloop()