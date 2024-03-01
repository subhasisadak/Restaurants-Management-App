import tkinter as tk
from tkinter import *
from tkinter.font import Font
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


def quantity_enter(event):
    if quantity.get() == "0":
        quantity.delete(0, len("0"))


def welcome():
    fl = 9 / 5
    name = "chittodar bhater hotel"
    mid = 19
    l_mid = len(name)//2
    space = " "*int(mid-l_mid)
    text_area.insert(1.0, space+name+"\n")
    h1 = "=====================================\n"
    text_area.insert(2.0, h1)
    text = "      ITEM             QTY    PRICE\n"
    text_area.insert(3.0, text)
    h2 = "                                    p\n"
    text_area.insert(4.0, h1)
    print(len(h1), len(h2))
    remain = ""
    item = "CHICKEN TIKKA BUTTER MASALA".lower()
    item = " " + item
    print(len(" Mppppppppppppppppppp"))
    max_len = len(" ppppppppppppppppppppp")
    print(max_len, "hi")
    if len(item) > max_len:
        j = 0
        for i in range(max_len):
            if item[i] == " ":
                j = i
        remain = item[j+1:]
        item = item[:j]
    print(len(item))
    start_quantity = 23
    start_price = 30
    space = " "*(start_quantity - len(item))
    item += space + "1000"
    print(len(item))
    space = " "*(start_price - len(item))
    item += space + "1000000\n"
    text_area.insert(END, item)
    if remain:
        text_area.insert(END, " "+remain+"\n")


def add_item():
    item_name = "Pan Fried Chicken Momo"
    q = "10"
    price = "1000"
    st = " " + item_name + "\t\t\t  " + q + "\t   " + price + "\n"
    text_area.insert(END, st)
    item_name = "Radha Ballabi"
    q = "500"
    price = "6000"
    st = " " + item_name + "\t\t\t  " + q + "\t   " + price + "\n"
    text_area.insert(END, st)
    item_name = "Roll"
    q = "1"
    price = "50"
    st = " " + item_name + "\t\t\t  " + q + "\t   " + price + "\n"
    text_area.insert(END, st)


def generate_bill():
    if count_item == 0:
        messagebox.showerror("Error", "Add Items First")
    else:
        temp = text_area.get(5.0, 5.0 + count_item)
        print(temp)
        text_area.delete(0.0, END)
        welcome()
        text_area.insert(END, temp)
        text_area.insert(END, "====================================\n")
        text_area.insert(END, " Total Amount                 10\n")
        text_area.insert(END, "====================================\n")


def save_bill():
    bill_no = 000
    choice = messagebox.askyesno("Save Bill", "Do you want to save the bill ?")
    if choice > 0:
        bill = text_area.get(0.0, END)
        f1 = open("bills/"+str(bill_no)+".txt", "w")
        f1.write(bill)
        f1.close()
        messagebox.showinfo("Saved", "Saved successfully")
    else:
        return


def clear():
    item_search_entry.delete(0, len(item_search_entry.get()))
    item_search_entry.insert(0, "")
    quantity.delete(0, len(quantity.get()))
    quantity.insert(0, "0")
    text_area.delete(0.0, END)
    welcome()


my_front = Font(family="JetBrains Mono", size=10)
heading_label_frame = LabelFrame(root, bg="tomato", width=600, height=42)
heading_label_frame.place(x=0, y=0)
heading_label = tk.Label(heading_label_frame, text="Take Order", font=("Times_New_Roman", 17, "bold"),
                         bg="tomato", fg="khaki1")
heading_label.place(x=240, y=5)

take_order_frame = LabelFrame(root, height=305, width=270, background="SlateGray1")
take_order_frame.place(x=1, y=43)

head_label1 = Label(take_order_frame, text="Product Details", font=("Times_New_Roman", 12, "bold"), bg="SlateGray1",
                    fg="black")
head_label1.place(x=70, y=5)
search_label = Label(take_order_frame, text="Item Name", font=("Times_New_Roman", 10), background="SlateGray1")
search_label.place(x=6, y=40)
dash_label = Label(take_order_frame, text="-", font=("Times_New_Roman", 15), bg="SlateGray1", fg="black")
dash_label.place(x=77, y=35)
item_search_entry = Entry(take_order_frame, width=23, font=("Times_New_Roman", 10))
item_search_entry.place(x=93, y=40)
check = Button(take_order_frame, text="Check Availability", bd=4, background="pale green", fg="black",
               activeforeground="black", activebackground="pale green")
check.place(x=120, y=75)

availability_label = Label(take_order_frame, text="  Available ", font=("Times_New_Roman", 10), background="SlateGray1")
availability_label.place(x=6, y=115)
dash_label1 = Label(take_order_frame, text="-", font=("Times_New_Roman", 15), bg="SlateGray1", fg="black")
dash_label1.place(x=77, y=110)
show_availability = Entry(take_order_frame, width=23, font=("Times_New_Roman", 10))
show_availability.place(x=93, y=115)

quantity_label = Label(take_order_frame, text="  Quantity  ", font=("Times_New_Roman", 10), background="SlateGray1")
quantity_label.place(x=6, y=160)
dash_label2 = Label(take_order_frame, text="-", font=("Times_New_Roman", 15), bg="SlateGray1", fg="black")
dash_label2.place(x=80, y=155)
quantity = Entry(take_order_frame, width=12, font=("Times_New_Roman", 10))
quantity.place(x=97, y=160)
quantity.insert(0, "0")
quantity.bind('<FocusIn>', quantity_enter)
add_item_button = Button(take_order_frame, text="Add Item", bd=4, background="pale green", fg="black",
                         activebackground="pale green", activeforeground="black", command=add_item)
add_item_button.place(x=197, y=157)

generate_bill_button = Button(take_order_frame, text="   Generate  Bill  ", bd=4, background="pale green", fg="black",
                              activeforeground="black", activebackground="pale green", command=generate_bill)
generate_bill_button.place(x=90, y=205)
clear_button = Button(take_order_frame, text="Clear Bill", bd=4, background="pale green", fg="black",
                      activebackground="pale green", activeforeground="black", command=clear)
clear_button.place(x=110, y=250)

billing_frame = LabelFrame(root, background="white", relief=tk.GROOVE, bd=8)
billing_frame.place(x=271, y=43)

head_label2 = Label(billing_frame, text="  Billing  Area  ", font=("Times_New_Roman", 12, "bold"), bg="white")
head_label2.pack(fill=tk.X)
scrollbar = tk.Scrollbar(billing_frame, orient=VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_area = tk.Text(billing_frame, height=17, width=37, yscrollcommand=scrollbar.set, bg="SlateGray1")
text_area.pack()
scrollbar.configure(command=text_area.yview)
# text_area = scrolledtext.ScrolledText(billing_frame, width=42, height=16, font=my_front, bg="pink")
# text_area.place(x=5, y=35)
count_item = float(3)
welcome()
root.mainloop()
