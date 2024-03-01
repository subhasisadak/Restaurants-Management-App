import tkinter as tk
from tkinter import *
from tkinter.font import Font
from tkinter import scrolledtext
from tkinter import messagebox
# from PIL import ImageTk
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


def bill_no_enter(event):
    bill_no_entry.delete(0, END)


heading_frame = Frame(root, bd=5, relief=GROOVE, width=600, height=40, bg="gold")
heading_frame.place(x=0, y=0)
heading_label = Label(heading_frame, text="Check   Orders", font=("Times_New_Roman", 13, "bold"),
                      bg="gold", fg="black")
heading_label.place(x=230, y=3)

check_order_frame = Frame(root, bd=5, relief=GROOVE, width=270, height=307, bg="gold")
check_order_frame.place(x=1, y=41)
heading_label1 = Label(check_order_frame, text="Search  Order  Here", font=("Times_New_Roman", 11, "bold"),
                       bg="gold", fg="black")
heading_label1.place(x=50, y=1)
show_bills_area = scrolledtext.ScrolledText(check_order_frame, width=16, height=10, bg="pale turquoise", fg="red4")
show_bills_area.place(x=1, y=30)
check_orders_button = Button(check_order_frame, text="Check \n Placed Orders", bd=4, background="khaki1", fg="red2",
                             activeforeground="red2", activebackground="khaki1")
check_orders_button.place(x=162, y=150)
bill_no_entry = Entry(check_order_frame, width=21, font=("Times_New_Roman", 9), background="pale turquoise", fg="red4")
bill_no_entry.place(x=3, y=220)
bill_no_entry.insert(0, " Enter Bill Number Here")
bill_no_entry.bind('<FocusIn>', bill_no_enter)
check_bill_button = Button(check_order_frame, text=" Check Bill ", bd=4, background="khaki1", fg="red2",
                           activebackground="khaki1", activeforeground="red2")
check_bill_button.place(x=170, y=216)
back_button = Button(check_order_frame, text=" Back ", bd=4, background="khaki1", fg="red2",
                     activebackground="khaki1", activeforeground="red2")
back_button.place(x=110, y=256)


show_bill_frame = Frame(root, bd=5, relief=GROOVE, width=329, height=307, bg="gold")
show_bill_frame.place(x=272, y=41)
head_label2 = Label(show_bill_frame, text="  Billing  Area  ", font=("Times_New_Roman", 12, "bold"), bg="gold")
head_label2.pack(fill=tk.X)
scrollbar = tk.Scrollbar(show_bill_frame, orient=VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_area = tk.Text(show_bill_frame, height=12, width=37, yscrollcommand=scrollbar.set, bg="pale turquoise", fg="red4")
text_area.pack()
scrollbar.configure(command=text_area.yview)
blank_label1 = Label(show_bill_frame, text=" ", font=("Times_New_Roman", 1), background="gold")
blank_label1.pack()
info_label = Label(show_bill_frame, text=" If Order is Ready Press Ready Button ", bg="pink",
                   font=("Times_New_Roman", 8), background="gold")
info_label.pack()
blank_label2 = Label(show_bill_frame, text=" ", font=("Times_New_Roman", 1), background="gold")
blank_label2.pack()
ready_button = Button(show_bill_frame, text=" Ready ", font=("Times_New_Roman", 9), bd=4, background="khaki1",
                      fg="red2", activebackground="khaki1", activeforeground="red2")
ready_button.pack()
blank_label3 = Label(show_bill_frame, text=" ", font=("Times_New_Roman", 2), background="gold")
blank_label3.pack()
root.mainloop()
