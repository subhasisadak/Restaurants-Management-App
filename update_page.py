import tkinter as tk
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from PIL import ImageTk
codeFont = ("Times_New_Roman", 25)
root = tk.Tk()
width = 600
height = 350
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
x = (screenWidth/2) - (width/2)
y = (screenHeight/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(False, False)
root.title("Bill Generator")


def item_enter(event):
    item_name_entry.delete(0, END)


def price_enter(event):
    price_entry.delete(0, END)


def availability_enter(event):
    availability_entry.delete(0, END)


def old_name_enter(event):
    old_name_entry.delete(0, END)


def new_name_enter(event):
    new_name_entry.delete(0, END)


def item_name_enter1(event):
    item_name_entry1.delete(0, END)


def price_enter1(event):
    price_entry1.delete(0, END)


def item_name_enter2(event):
    item_name_entry2.delete(0, END)


def quantity_enter(event):
    quantity_entry.delete(0, END)


def refresh_page():
    old_name_entry.delete(0, END)
    old_name_entry.insert(0, "Enter old Name")
    new_name_entry.delete(0, END)
    new_name_entry.insert(0, "Enter New Name")
    item_name_entry1.delete(0, END)
    item_name_entry1.insert(0, "Enter Item name")
    price_entry1.delete(0, END)
    price_entry1.insert(0, "Enter Price")
    item_name_entry2.delete(0, END)
    item_name_entry2.insert(0, "Enter Item Name")
    quantity_entry.delete(0, END)
    quantity_entry.insert(0, "Enter Available Quantity")
    item_name_entry.delete(0, END)
    item_name_entry.insert(0, "Enter Item Name")
    price_entry.delete(0, END)
    price_entry.insert(0, "Enter Price")
    availability_entry.delete(0, END)
    availability_entry.insert(0, "Quantity")


def is_integer(s):
    for c in s:
        if ord(c) < 48 or ord(c) > 57:
            return False
    return True


def add():
    if item_name_entry.get() == "" or price_entry.get() == "" or availability_entry.get() == "":
        messagebox.showerror("Error", "All Fields Required")
    elif item_name_entry.get() == "Enter Item Name":
        messagebox.showerror("Error", "Enter Item Name")
    elif price_entry.get() == "Enter Price":
        messagebox.showerror("Error", "Enter Price")
    elif availability_entry.get() == "Quantity":
        messagebox.showerror("Error", "Enter Quantity")
    elif not is_integer(price_entry.get()):
        messagebox.showerror("Error", "Enter valid price")
    elif not is_integer(availability_entry.get()):
        messagebox.showerror("Error", "Enter valid quantity")
    else:
        messagebox.showinfo("Successful", "Item added successfully")
        refresh_page()


def update_name():
    if old_name_entry.get() == "" or new_name_entry.get() == "":
        messagebox.showerror("Error", "All field required")
    elif old_name_entry.get() == "Enter Old Name":
        messagebox.showerror("Error", "Enter item's old name")
    elif new_name_entry.get() == "Enter New Name":
        messagebox.showerror("Error", "Enter item's new name")
    else:
        refresh_page()


def update_price():
    if item_name_entry1.get() == "" or price_entry1.get() == "":
        messagebox.showerror("Error", "All field required")
    elif item_name_entry1.get() == "Enter Item Name":
        messagebox.showerror("Error", "Enter item name")
    elif price_entry1.get() == "Enter Price":
        messagebox.showerror("Error", "Enter price")
    elif not is_integer(price_entry1.get()):
        messagebox.showerror("Error", "Enter valid price")
    else:
        refresh_page()


def update_quantity():
    if item_name_entry2.get() == "" or quantity_entry.get() == "":
        messagebox.showerror("Error", "All field required")
    elif item_name_entry2.get() == "Enter Item Name":
        messagebox.showerror("Error", "Enter item name")
    elif quantity_entry.get() == "Enter Available Quantity":
        messagebox.showerror("Error", "Enter quantity")
    elif not is_integer(quantity_entry.get()):
        messagebox.showerror("Error", "Enter valid quantity")
    else:
        refresh_page()


def back():
    refresh_page()


bg_image = ImageTk.PhotoImage(file='bg1.jpeg')
bg_label = Label(root, image=bg_image)
bg_label.pack()

old_name_entry = Entry(root, width=20, font=("Times_New_Roman", 10), fg='blue')
old_name_entry.place(x=95, y=40)
old_name_entry.insert(0, "Enter Old Name")
old_name_entry.bind('<FocusIn>', old_name_enter)
new_name_entry = Entry(root, width=20, font=("Times_New_Roman", 10), fg='blue')
new_name_entry.place(x=260, y=40)
new_name_entry.insert(0, "Enter New Name")
new_name_entry.bind('<FocusIn>', new_name_enter)
update_name_button = Button(root, text=" Update Name ", font=("Times_New_Roman", 9), cursor='hand2', bd=5,
                            fg="blue", activeforeground="blue", command=update_name)
update_name_button.place(x=425, y=35)

item_name_entry1 = Entry(root, width=20, font=("Times_New_Roman", 10), fg='blue')
item_name_entry1.place(x=95, y=100)
item_name_entry1.insert(0, "Enter Item name")
item_name_entry1.bind('<FocusIn>', item_name_enter1)  # from here we update further
price_entry1 = Entry(root, width=20, font=("Times_New_Roman", 10), fg='blue')
price_entry1.place(x=260, y=100)
price_entry1.insert(0, "Enter Price")
price_entry1.bind('<FocusIn>', price_enter1)
update_price_button = Button(root, text=" Update Price ", font=("Times_New_Roman", 9), cursor='hand2', bd=5,
                             fg="blue", activeforeground="blue", command=update_price)
update_price_button.place(x=425, y=95)

item_name_entry2 = Entry(root, width=20, font=("Times_New_Roman", 10), fg='blue')
item_name_entry2.place(x=95, y=160)
item_name_entry2.insert(0, "Enter Item Name")
item_name_entry2.bind('<FocusIn>', item_name_enter2)  # from here we update further
quantity_entry = Entry(root, width=20, font=("Times_New_Roman", 10), fg='blue')
quantity_entry.place(x=260, y=160)
quantity_entry.insert(0, "Enter Available Quantity")
quantity_entry.bind('<FocusIn>', quantity_enter)
update_availability_button = Button(root, text=" Update Availability ", font=("Times_New_Roman", 9), cursor='hand2', bd=5,
                                    fg="blue", activeforeground="blue", command=update_quantity)
update_availability_button.place(x=425, y=155)

# A line between login section and create account
frame_line = Frame(root, width=500, height=2, bg='white')
frame_line.place(x=45, y=210)
information_label = Label(root,
                          text=" If the item is not available now, enter 0 at Quantity else put the available quantity",
                          bg="plum1", fg="blue", font=("Times_New_Roman", 9))
information_label.place(x=80, y=220)
item_name_entry = Entry(root, width=20, font=("Times_New_Roman", 10), fg='blue')
item_name_entry.place(x=95, y=255)
item_name_entry.insert(0, "Enter Item Name")
item_name_entry.bind('<FocusIn>', item_enter)
price_entry = Entry(root, width=10, font=("Times_New_Roman", 10), fg='blue')
price_entry.place(x=255, y=255)
price_entry.insert(0, "Enter Price")
price_entry.bind('<FocusIn>', price_enter)
availability_entry = Entry(root, width=10, font=("Times_New_Roman", 10), fg='blue')
availability_entry.place(x=345, y=255)
availability_entry.insert(0, "Quantity")
availability_entry.bind('<FocusIn>', availability_enter)
add_button = Button(root, text=" Add  Item ", font=("Times_New_Roman", 9), cursor='hand2', bd=5,
                    fg="blue", activeforeground="blue", command=add)
add_button.place(x=435, y=248)
back_button = Button(root, text=" Back ", font=("Times_New_Roman", 9), cursor='hand2', bd=5,
                     fg="blue", activeforeground="blue", command=back)
back_button.place(x=270, y=295)
root.mainloop()
