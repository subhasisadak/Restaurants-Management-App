import tkinter as tk
# from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pyodbc as odbc
from datetime import *
from tkinter import scrolledtext

codeFont = ("Times_New_Roman", 25)
storeName = ""
itemTable = ""
billTable = ""
successfully_login = 0


# This class responsible for run multiple windows in a single window


class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # we have to store or stitch the every window class
        # So every time we call a specific class it shows top or come front on the window
        self.frames = {}
        for F in (LoginPage, ForgotPasswordPage, CreateAccountPage, MainPage, Update, TakeOrder, CheckOrders):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            # frame.pack()
        # at start, we want to show the login page/StartPage
        self.show_frame(LoginPage)

    # this method is responsible for rise the class on top of the screen/window

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# This is the first page after opening of the app


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # in case of function calling some time image didn't show on window
        # that's why we have to global all the Image variables
        global bg_image
        global close_eye
        global open_eye
        global successfully_login

        # its use to clear the string "Username" on click on it
        def user_enter(event):
            if username_entry.get() == "Username":
                username_entry.delete(0, len("Username"))

        # its use to clear the string "Password" on click on it
        def password_enter(event):
            if password_entry.get() == "Password":
                password_entry.delete(0, len("Password"))

        # Use to show the password on click on the eye button
        def show():
            eye_button.configure(image=open_eye)
            password_entry.configure(show='')
            eye_button.configure(command=hide)

        # Use to hide the password on click on the eye button
        def hide():
            eye_button.configure(image=close_eye)
            password_entry.configure(show='*')
            eye_button.configure(command=show)

        def login():
            global storeName
            global itemTable
            global billTable
            if username_entry.get() == "" or password_entry.get() == "":
                messagebox.showerror("Error", "All Fields Are Required")
            else:
                local_cursor = conc.cursor()
                local_cursor.execute("SELECT * FROM USERS WHERE [USER NAME] = ?", username_entry.get())
                user_row = local_cursor.fetchall()
                if not user_row or user_row[0][2] != password_entry.get() or username_entry.get() != user_row[0][1]:
                    messagebox.showerror("Error", "Invalid Username or Password")
                else:
                    storeName = user_row[0][3]
                    itemTable = user_row[0][4]
                    billTable = user_row[0][5]
                    username_entry.delete(0, len(username_entry.get()))
                    username_entry.insert(0, "Username")
                    password_entry.delete(0, len(password_entry.get()))
                    password_entry.insert(0, "Password")
                    local_cursor.close()
                    controller.show_frame(MainPage)

        def go_to_create_account():
            username_entry.delete(0, len(username_entry.get()))
            username_entry.insert(0, "Username")
            password_entry.delete(0, len(password_entry.get()))
            password_entry.insert(0, "Password")
            controller.show_frame(CreateAccountPage)

        def go_to_forgot_password():
            username_entry.delete(0, len(username_entry.get()))
            username_entry.insert(0, "Username")
            password_entry.delete(0, len(password_entry.get()))
            password_entry.insert(0, "Password")
            controller.show_frame(ForgotPasswordPage)

        # this is for background image
        bg_image = ImageTk.PhotoImage(file='bg1.jpeg')
        bg_label = tk.Label(self, image=bg_image)
        bg_label.pack()
        # login page heading
        heading = tk.Label(self, text="  First Billing  ", font=("Times_New_Roman", 25), bg="plum1", fg="SlateBlue1")
        heading.place(x=195, y=20)
        # Username Entry
        username_entry = tk.Entry(self, width=25, font=("Times_New_Roman", 11), fg='blue')
        username_entry.place(x=190, y=90)
        username_entry.insert(0, "Username")
        username_entry.bind('<FocusIn>', user_enter)
        # password Entry
        password_entry = tk.Entry(self, width=25, font=("Times_New_Roman", 11), fg='blue')
        password_entry.place(x=190, y=130)
        password_entry.insert(0, "Password")
        password_entry.bind('<FocusIn>', password_enter)
        # button to hide or show password
        open_eye = ImageTk.PhotoImage(file='openeye.png')
        close_eye = ImageTk.PhotoImage(file='closeye.png')
        eye_button = tk.Button(self, image=open_eye, bd=0, bg='white', activebackground='white', cursor='hand2',
                               command=hide)
        eye_button.place(x=400, y=128)
        # Button to login
        login_but = tk.Button(self, text="Login", font=("Times_New_Roman", 9), cursor='hand2', bd=4, width=10,
                              fg="blue", activeforeground="blue", command=login)
        login_but.place(x=250, y=170)
        # help to get user id and password in case you forgot the password
        forgot_password_but = tk.Button(self, text='Forgot Password ?', bd=4, cursor='hand2',
                                        font=("Times_New_Roman", 9), fg='blue', activeforeground='blue',
                                        command=go_to_forgot_password)
        forgot_password_but.place(x=235, y=210)
        # A line between login section and create account
        frame_line = tk.Frame(self, width=400, height=2, bg='white')
        frame_line.place(x=100, y=250)
        # button to create a new account
        create_account_but = tk.Button(self, text="Create Account", font=("Times_New_Roman", 9), cursor='hand2', bd=4,
                                       width=20, fg="blue", activeforeground="blue",
                                       command=go_to_create_account)
        create_account_but.place(x=220, y=270)


# This page to retrieve the username and password
class ForgotPasswordPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global bg_image
        # this is for background image
        # bg_image = ImageTk.PhotoImage(file='bg1.jpeg')

        def get():
            global cursor
            cursor = conc.cursor()
            cursor.execute("SELECT * FROM USERS WHERE EMAIL = ?", email_entry.get())
            user_row = cursor.fetchall()
            if not user_row:
                messagebox.showerror("Error", "User not found")
            else:
                show_username.delete(0, tk.END)
                show_password.delete(0, tk.END)
                show_username.insert(0, user_row[0][1])
                show_password.insert(0, user_row[0][2])
            cursor.close()

        def back():
            email_entry.delete(0, tk.END)
            show_username.delete(0, tk.END)
            show_password.delete(0, tk.END)
            controller.show_frame(LoginPage)

        bg_label = tk.Label(self, image=bg_image)
        bg_label.pack()
        heading = tk.Label(self, text=" Retrieve Password ", font=("Times_New_Roman", 25), bg="plum1", fg="SlateBlue1")
        heading.place(x=160, y=20)
        label1 = tk.Label(self, text=" Enter Your Email ", font=("Times_New_Roman", 12), bg="plum1", fg="SlateBlue1")
        label1.place(x=160, y=100)
        email_entry = tk.Entry(self, font=("Times_New_Roman", 10))
        email_entry.place(x=310, y=100)
        get_button = tk.Button(self, text=" Get ", font=("Times_New_Roman", 9), cursor='hand2', bd=4, width=10,
                               fg="blue", activeforeground="blue", command=get)
        get_button.place(x=275, y=150)
        label2 = tk.Label(self, text=" Your Username ", font=("Times_New_Roman", 12), bg="plum1", fg="SlateBlue1")
        label2.place(x=160, y=205)
        show_username = tk.Entry(self, font=("Times_New_Roman", 10))
        show_username.place(x=310, y=205)
        label3 = tk.Label(self, text=" Your Password ", font=("Times_New_Roman", 12), bg="plum1", fg="SlateBlue1")
        label3.place(x=160, y=255)
        show_password = tk.Entry(self, font=("Times_New_Roman", 10))
        show_password.place(x=310, y=255)
        back_button = tk.Button(self, text=" Back ", font=("Times_New_Roman", 9), cursor='hand2', bd=4, width=10,
                                fg="blue", activeforeground="blue", command=back)
        back_button.place(x=275, y=305)


# This is the login page


class CreateAccountPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global open_eye1
        global close_eye1
        global open_eye2
        global close_eye2
        # this is for background image
        bg_label = tk.Label(self, image=bg_image)
        bg_label.pack()
        # create account page heading
        heading = tk.Label(self, text="  Create Account  ", font=("Times_New_Roman", 25), bg="plum1", fg="SlateBlue1")
        heading.place(x=180, y=10)

        # Its use to clear the String "Email" on click
        def email_enter(event):
            if email_entry.get() == "Email":
                email_entry.delete(0, len("Email"))

        # Its use to clear the String "username" on click
        def user_enter(event):
            if username_entry.get() == "Username":
                username_entry.delete(0, len("Username"))

        # its use to clear the string "Store Name on click
        def store_name_enter(event):
            if store_name_entry.get() == "Store Name":
                store_name_entry.delete(0, len("Store Name"))

        # Its use to clear the String "username" on click
        def password_enter(event):
            if password_entry.get() == "Enter Password":
                password_entry.delete(0, len("Enter Password"))

        # its use to clear the string "Password" on click on it
        def confirm_password_enter(event):
            if confirm_password_entry.get() == "Confirm Password":
                confirm_password_entry.delete(0, len("Confirm Password"))

        # Use to show the password on click on the eye button
        def show1():
            eye_button1.configure(image=open_eye1)
            password_entry.configure(show='')
            eye_button1.configure(command=hide1)

        # Use to hide the password on click on the eye button
        def hide1():
            eye_button1.configure(image=close_eye1)
            password_entry.configure(show='*')
            eye_button1.configure(command=show1)

        # Use to show the password on click on the eye button
        def show2():
            eye_button2.configure(image=open_eye2)
            confirm_password_entry.configure(show='')
            eye_button2.configure(command=hide2)

        # Use to hide the password on click on the eye button
        def hide2():
            eye_button2.configure(image=close_eye2)
            confirm_password_entry.configure(show='*')
            eye_button2.configure(command=show2)

        def back_to_login():
            global cursor
            email_entry.delete(0, len(email_entry.get()))
            email_entry.insert(0, "Email")
            username_entry.delete(0, len(username_entry.get()))
            username_entry.insert(0, "Username")
            store_name_entry.delete(0, len("Store Name"))
            store_name_entry.insert(0, "Store Name")
            password_entry.delete(0, len(password_entry.get()))
            password_entry.insert(0, "Enter Password")
            confirm_password_entry.delete(0, len(confirm_password_entry.get()))
            confirm_password_entry.insert(0, "Confirm Password")
            check.set(0)
            controller.show_frame(LoginPage)

        def connect_database():
            global cursor
            if email_entry.get() == "" or username_entry.get() == "" or password_entry.get() == "" or \
                    confirm_password_entry.get() == "" or store_name_entry.get() == "":
                messagebox.showerror("Error", "All Fields Are Required")
            elif password_entry.get() != confirm_password_entry.get():
                messagebox.showerror("Error", "password Mismatch")
            elif check.get() == 0:
                messagebox.showerror("Error", "Please Accept Terms and Conditions")
            else:
                curser = conc.cursor()
                curser.execute("SELECT * FROM USERS WHERE [EMAIL] = ?", email_entry.get())
                email_row = curser.fetchall()
                curser.execute("SELECT * FROM USERS WHERE [USER NAME] = ?", username_entry.get())
                user_row = curser.fetchall()
                if email_row:
                    messagebox.showerror("Error", "Email Already Exists")
                elif user_row:
                    messagebox.showerror("Error", "username Already Exists")
                else:
                    email = email_entry.get()
                    user_name = username_entry.get()
                    store_name = store_name_entry.get()
                    password = password_entry.get()
                    item_database = user_name+"items"
                    bill_database = user_name+"bills"
                    curser.execute("INSERT INTO USERS VALUES (?, ?, ?, ?, ?, ?)", (email, user_name, password,
                                                                                   store_name, item_database,
                                                                                   bill_database))
                    curser.execute("CREATE TABLE {} ([ITEM NAME] VARCHAR(50) PRIMARY KEY, PRICE INT NOT NULL, "
                                   "AVAILABLE INT NOT NULL)".format(item_database))
                    curser.execute("CREATE TABLE {} ([ORDER DATE] VARCHAR(20) NOT NULL, "
                                   "[BILL NUMBER] VARCHAR(20) NOT NULL, STATUS VARCHAR(10) NOT NULL)".
                                   format(bill_database))
                    curser.commit()
                    curser.close()
                    messagebox.showinfo("Success", "Registration is Successful")
                    back_to_login()

        # Email Entry
        email_entry = tk.Entry(self, width=25, font=("Times_New_Roman", 11), fg='blue')
        email_entry.place(x=210, y=70)
        email_entry.insert(0, "Email")
        email_entry.bind('<FocusIn>', email_enter)
        # Username Entry
        username_entry = tk.Entry(self, width=25, font=("Times_New_Roman", 11), fg='blue')
        username_entry.place(x=210, y=110)
        username_entry.insert(0, "Username")
        username_entry.bind('<FocusIn>', user_enter)
        # Store Name Entry
        store_name_entry = tk.Entry(self, width=25, font=("Times_New_Roman", 11), fg='blue')
        store_name_entry.place(x=210, y=150)
        store_name_entry.insert(0, "Store Name")
        store_name_entry.bind('<FocusIn>', store_name_enter)
        # password Entry
        password_entry = tk.Entry(self, width=25, font=("Times_New_Roman", 11), fg='blue')
        password_entry.place(x=210, y=190)
        password_entry.insert(0, "Enter Password")
        password_entry.bind('<FocusIn>', password_enter)
        # button to hide or show password
        open_eye1 = ImageTk.PhotoImage(file='openeye.png')
        close_eye1 = ImageTk.PhotoImage(file='closeye.png')
        eye_button1 = tk.Button(self, image=open_eye1, bd=0, bg='white', activebackground='white', cursor='hand2',
                                command=hide1)
        eye_button1.place(x=420, y=188)
        # Confirm Password Entry
        confirm_password_entry = tk.Entry(self, width=25, font=("Times_New_Roman", 11), fg='blue')
        confirm_password_entry.place(x=210, y=230)
        confirm_password_entry.insert(0, "Confirm Password")
        confirm_password_entry.bind('<FocusIn>', confirm_password_enter)
        # button to hide or show password
        open_eye2 = ImageTk.PhotoImage(file='openeye.png')
        close_eye2 = ImageTk.PhotoImage(file='closeye.png')
        eye_button2 = tk.Button(self, image=open_eye2, bd=0, bg='white', activebackground='white', cursor='hand2',
                                command=hide2)
        eye_button2.place(x=420, y=228)
        # Check terms and condition
        check = tk.IntVar(self)
        terms_and_condition = tk.Checkbutton(self, text="I Agree to the Terms & Conditions",
                                             font=("Times_New_Roman", 9), bg='powder blue',
                                             activebackground='powder blue', activeforeground="blue", fg="blue",
                                             cursor='hand2', variable=check)
        terms_and_condition.place(x=210, y=270)
        # Button to create account
        crate_but = tk.Button(self, text="Create", font=("Times_New_Roman", 9), cursor='hand2', bd=4, width=10,
                              fg="blue", activeforeground="blue", command=connect_database)
        crate_but.place(x=220, y=305)
        back = tk.Button(self, text="Back", font=("Times_New_Roman", 9), cursor='hand2', bd=4, width=10,
                         fg="blue", activeforeground="blue", command=back_to_login)
        back.place(x=330, y=305)

# This page shows after successfully loged-in or Sign In.


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global bg_image

        def back_to_login():
            controller.show_frame(LoginPage)

        def goto_update():
            controller.show_frame(Update)

        def goto_take_order():
            controller.show_frame(TakeOrder)

        def goto_check_order():
            controller.show_frame(CheckOrders)

        bg_label = tk.Label(self, image=bg_image)
        bg_label.pack()
        update_button = tk.Button(self, text=" For Update or Add Items ", bd=5, font=("Times_New_Roman", 13),
                                  bg="plum1", fg="DarkOrchid4", cursor="hand2", activeforeground="DarkOrchid4",
                                  activebackground="plum1", command=goto_update)
        update_button.place(x=180, y=40)
        take_order_button = tk.Button(self, text=" Take Order ", bd=5, font=("Times_New_Roman", 13), bg="plum1",
                                      fg="DarkOrchid4", cursor="hand2", activeforeground="DarkOrchid4",
                                      activebackground="plum1", command=goto_take_order)
        take_order_button.place(x=233, y=120)
        check_order_button = tk.Button(self, text=" Check Orders ", bd=5, font=("Times_New_Roman", 13), bg="plum1",
                                       fg="DarkOrchid4", cursor="hand2", activeforeground="DarkOrchid4",
                                       activebackground="plum1", command=goto_check_order)
        check_order_button.place(x=221, y=200)
        back_button = tk.Button(self, text=" Back ", bd=5, font=("Times_New_Roman", 13), bg="plum1",
                                fg="DarkOrchid4", cursor="hand2", activeforeground="DarkOrchid4",
                                activebackground="plum1", command=back_to_login)
        back_button.place(x=260, y=280)


# For Update database


class Update(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global bg_image
        global itemTable

        def item_enter(event):
            item_name_entry.delete(0, tk.END)

        def price_enter(event):
            price_entry.delete(0, tk.END)

        def availability_enter(event):
            availability_entry.delete(0, tk.END)

        def old_name_enter(event):
            old_name_entry.delete(0, tk.END)

        def new_name_enter(event):
            new_name_entry.delete(0, tk.END)

        def item_name_enter1(event):
            item_name_entry1.delete(0, tk.END)

        def price_enter1(event):
            price_entry1.delete(0, tk.END)

        def item_name_enter2(event):
            item_name_entry2.delete(0, tk.END)

        def quantity_enter(event):
            quantity_entry.delete(0, tk.END)

        def refresh_page():
            old_name_entry.delete(0, tk.END)
            old_name_entry.insert(0, "Enter old Name")
            new_name_entry.delete(0, tk.END)
            new_name_entry.insert(0, "Enter New Name")
            item_name_entry1.delete(0, tk.END)
            item_name_entry1.insert(0, "Enter Item name")
            price_entry1.delete(0, tk.END)
            price_entry1.insert(0, "Enter Price")
            item_name_entry2.delete(0, tk.END)
            item_name_entry2.insert(0, "Enter Item Name")
            quantity_entry.delete(0, tk.END)
            quantity_entry.insert(0, "Enter Available Quantity")
            item_name_entry.delete(0, tk.END)
            item_name_entry.insert(0, "Enter Item Name")
            price_entry.delete(0, tk.END)
            price_entry.insert(0, "Enter Price")
            availability_entry.delete(0, tk.END)
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
                local_cursor = conc.cursor()
                name = item_name_entry.get()
                price = price_entry.get()
                quantity = availability_entry.get()
                local_cursor.execute("SELECT * FROM {} WHERE [ITEM NAME] = ?".format(itemTable), name)
                row = local_cursor.fetchall()
                if row:
                    messagebox.showinfo("Added", "Item already added")
                else:
                    local_cursor.execute("INSERT INTO {} VALUES (?, ?, ?)".format(itemTable), (name, price, quantity))
                    cursor.commit()
                    messagebox.showinfo("Successful", "Item added successfully")
                local_cursor.close()
                refresh_page()

        def update_name():
            if old_name_entry.get() == "" or new_name_entry.get() == "":
                messagebox.showerror("Error", "All field required")
            elif old_name_entry.get() == "Enter Old Name":
                messagebox.showerror("Error", "Enter item's old name")
            elif new_name_entry.get() == "Enter New Name":
                messagebox.showerror("Error", "Enter item's new name")
            else:
                local_cursor = conc.cursor()
                old_name = old_name_entry.get()
                new_name = new_name_entry.get()
                local_cursor.execute("SELECT * FROM {} WHERE [ITEM NAME] = ?".format(itemTable), old_name)
                item_row = local_cursor.fetchall()
                if not item_row:
                    messagebox.showerror("Error", "Item not found")
                else:
                    local_cursor.execute("UPDATE {} SET [ITEM NAME] = ? WHERE [ITEM NAME] = ?".format(itemTable),
                                         (new_name, old_name))
                    local_cursor.commit()
                    local_cursor.close()
                    messagebox.showinfo("Successful", "Quantity update successfully")
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
                local_cursor = conc.cursor()
                name = item_name_entry1.get()
                price = int(price_entry1.get())
                local_cursor.execute("SELECT * FROM {} WHERE [ITEM NAME] = ?".format(itemTable), name)
                item_row = local_cursor.fetchall()
                if not item_row:
                    messagebox.showerror("Error", "Item not found")
                else:
                    local_cursor.execute("UPDATE {} SET PRICE = ? WHERE [ITEM NAME] = ?".format(itemTable),
                                         (price, name))
                    local_cursor.commit()
                    local_cursor.close()
                    messagebox.showinfo("Successful", "Quantity update successfully")
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
                local_cursor = conc.cursor()
                name = item_name_entry2.get()
                quantity = int(quantity_entry.get())
                local_cursor.execute("SELECT * FROM {} WHERE [ITEM NAME] = ?".format(itemTable), name)
                item_row = local_cursor.fetchall()
                if not item_row:
                    messagebox.showerror("Error", "Item not found")
                else:
                    local_cursor.execute("UPDATE {} SET AVAILABLE = ? WHERE [ITEM NAME] = ?".format(itemTable),
                                   (quantity, name))
                    local_cursor.commit()
                    local_cursor.close()
                    messagebox.showinfo("Successful", "Quantity update successfully")
                refresh_page()

        def back():
            refresh_page()
            controller.show_frame(MainPage)

        # bg_image = ImageTk.PhotoImage(file='bg1.jpeg')
        bg_label = tk.Label(self, image=bg_image)
        bg_label.pack()

        old_name_entry = tk.Entry(self, width=20, font=("Times_New_Roman", 10), fg='blue')
        old_name_entry.place(x=95, y=40)
        old_name_entry.insert(0, "Enter Old Name")
        old_name_entry.bind('<FocusIn>', old_name_enter)
        new_name_entry = tk.Entry(self, width=20, font=("Times_New_Roman", 10), fg='blue')
        new_name_entry.place(x=260, y=40)
        new_name_entry.insert(0, "Enter New Name")
        new_name_entry.bind('<FocusIn>', new_name_enter)
        update_name_button = tk.Button(self, text=" Update Name ", font=("Times_New_Roman", 9), cursor='hand2', bd=5,
                                       fg="blue", activeforeground="blue", command=update_name)
        update_name_button.place(x=425, y=35)

        item_name_entry1 = tk.Entry(self, width=20, font=("Times_New_Roman", 10), fg='blue')
        item_name_entry1.place(x=95, y=100)
        item_name_entry1.insert(0, "Enter Item name")
        item_name_entry1.bind('<FocusIn>', item_name_enter1)  # from here we update further
        price_entry1 = tk.Entry(self, width=20, font=("Times_New_Roman", 10), fg='blue')
        price_entry1.place(x=260, y=100)
        price_entry1.insert(0, "Enter Price")
        price_entry1.bind('<FocusIn>', price_enter1)
        update_price_button = tk.Button(self, text=" Update Price ", font=("Times_New_Roman", 9), cursor='hand2', bd=5,
                                        fg="blue", activeforeground="blue", command=update_price)
        update_price_button.place(x=425, y=95)

        item_name_entry2 = tk.Entry(self, width=20, font=("Times_New_Roman", 10), fg='blue')
        item_name_entry2.place(x=95, y=160)
        item_name_entry2.insert(0, "Enter Item Name")
        item_name_entry2.bind('<FocusIn>', item_name_enter2)  # from here we update further
        quantity_entry = tk.Entry(self, width=20, font=("Times_New_Roman", 10), fg='blue')
        quantity_entry.place(x=260, y=160)
        quantity_entry.insert(0, "Enter Available Quantity")
        quantity_entry.bind('<FocusIn>', quantity_enter)
        update_availability_button = tk.Button(self, text=" Update Availability ", font=("Times_New_Roman", 9),
                                               cursor='hand2', bd=5, fg="blue", activeforeground="blue",
                                               command=update_quantity)
        update_availability_button.place(x=425, y=155)

        # A line between login section and create account
        frame_line = tk.Frame(self, width=500, height=2, bg='white')
        frame_line.place(x=45, y=210)
        information_label = tk.Label(self, text="If the item is not available now, enter 0 at Quantity else put the "
                                                "available quantity", bg="plum1", fg="blue",
                                     font=("Times_New_Roman", 9))
        information_label.place(x=80, y=220)
        item_name_entry = tk.Entry(self, width=20, font=("Times_New_Roman", 10), fg='blue')
        item_name_entry.place(x=95, y=255)
        item_name_entry.insert(0, "Enter Item Name")
        item_name_entry.bind('<FocusIn>', item_enter)
        price_entry = tk.Entry(self, width=10, font=("Times_New_Roman", 10), fg='blue')
        price_entry.place(x=255, y=255)
        price_entry.insert(0, "Enter Price")
        price_entry.bind('<FocusIn>', price_enter)
        availability_entry = tk.Entry(self, width=10, font=("Times_New_Roman", 10), fg='blue')
        availability_entry.place(x=345, y=255)
        availability_entry.insert(0, "Quantity")
        availability_entry.bind('<FocusIn>', availability_enter)
        add_button = tk.Button(self, text=" Add  Item ", font=("Times_New_Roman", 9), cursor='hand2', bd=5,
                               fg="blue", activeforeground="blue", command=add)
        add_button.place(x=435, y=248)
        back_button = tk.Button(self, text=" Back ", font=("Times_New_Roman", 9), cursor='hand2', bd=5,
                                fg="blue", activeforeground="blue", command=back)
        back_button.place(x=270, y=295)

# For Taking Orders


class TakeOrder(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global itemTable
        global billTable
        global storeName
        global successfully_login
        global conc
        # global text_area

        # used to clear quantity entry field
        def quantity_enter(event):
            if quantity.get() == "0":
                quantity.delete(0, len("0"))
                # welcome()

        # used to clear item entry field
        def item_enter(event):
            nonlocal flag
            if item_search_entry.get() == "" and flag == 0:
                welcome()
                flag = 1
            else:
                item_search_entry.delete(0, tk.END)

        # it's run at first
        def welcome():
            name = storeName.upper()
            mid = 19
            l_mid = len(name) // 2
            space = " " * int(mid - l_mid)
            text_area.insert(1.0, space + name + "\n")
            border = "=====================================\n"
            text_area.insert(2.0, border)
            text = "    ITEM              QTY   PRICE\n"
            text_area.insert(3.0, text)
            text_area.insert(4.0, border)

        # used to add item
        def add_item():
            nonlocal count_line
            nonlocal total
            global cursor
            if item_search_entry.get() == "":
                messagebox.showerror("Error", "No Item Name")
            elif quantity.get() == "0" or quantity.get() == "":
                messagebox.showerror("Error", "Add Quantity Please")
            else:
                cursor = conc.cursor()
                cursor.execute("SELECT * FROM {} where [ITEM NAME] = ?".format(itemTable), item_search_entry.get())
                item_row = cursor.fetchall()
                if not item_row:
                    messagebox.showerror("Error", "Item didn't found")
                elif item_row[0][2] == 0:
                    messagebox.showerror("Error", "Item not available please update availability")
                elif item_row[0][2] < int(quantity.get()):
                    messagebox.showerror("Error", "Quantity is not available please update availability")
                else:
                    quantity_position = 22
                    price_position = 28
                    remain = ""
                    max_len = 21
                    item_name = item_row[0][0]
                    st = " " + item_name
                    if len(st) > max_len:
                        j = 0
                        for i in range(max_len):
                            if st[i] == " ":
                                j = i
                        remain = " " + st[j+1:] + "\n"
                        st = st[:j]
                    has_available = item_row[0][2]
                    q = int(quantity.get())
                    cursor.execute("UPDATE {} SET AVAILABLE = ? WHERE [ITEM NAME] = ?".format(itemTable),
                                   ((has_available - q), item_name))
                    space = " "*(quantity_position - len(st))
                    st += space + str(q)
                    price = float(q*int(item_row[0][1]))
                    space = " "*(price_position - len(st))
                    st += space + str(price) + "\n"
                    text_area.insert(5.0 + count_line, st)
                    total += price
                    count_line += 1.0
                    if remain:
                        text_area.insert(5.0 + count_line, remain)
                        count_line += 1.0
                    
        # help to generate bill
        def generate_bill():
            nonlocal total
            if count_line == 0:
                messagebox.showerror("Error", "Add Items First")
            else:
                price_position = 28
                border = "=====================================\n"
                temp = text_area.get(5.0, 5.0 + count_line)
                text_area.delete(0.0, tk.END)
                welcome()
                st = " Total Amount"
                space = " "*(price_position - len(st))
                st += space + str(total) + "\n"
                text_area.insert(tk.END, temp)
                text_area.insert(tk.END, border)
                text_area.insert(tk.END, st)
                text_area.insert(tk.END, border)
                save_bill()

        # help to save the bill
        def save_bill():
            global cursor
            cursor1 = conc.cursor()
            today_date = str(date.today())
            date_time = str(datetime.now())
            bill_no = ""
            for i in range(11, len(date_time)):
                if date_time[i] == '-' or date_time[i] == ':' or date_time[i] == '.':
                    continue
                bill_no += date_time[i]
            choice = messagebox.askyesno("Save Bill", "Do you want to save the bill ?")
            if choice > 0:
                bill = text_area.get(0.0, tk.END)
                f1 = open("bills/" + bill_no + ".txt", "w")
                f1.write(bill)
                f1.close()
                cursor1.execute("INSERT INTO {} VALUES (?, ?, ?)".format(billTable), (today_date, bill_no, "NO"))
                cursor1.commit()
                cursor.commit()
                messagebox.showinfo("Saved", "Saved successfully")
                clear()
                cursor1.close()
            else:
                return

        # used to check item is available or not
        def check():
            cursor1 = conc.cursor()
            show_availability.delete(0, tk.END)
            cursor1.execute("SELECT * FROM {} where [ITEM NAME] = ?".format(itemTable), item_search_entry.get())
            item_row = cursor1.fetchall()
            if not item_row:
                messagebox.showerror("Error", "Item didn't found")
            else:
                show_availability.insert(0, item_row[0][2])
            cursor1.close()

        # used to clear all fields
        def clear():
            nonlocal count_line
            nonlocal total
            global cursor
            item_search_entry.delete(0, len(item_search_entry.get()))
            item_search_entry.insert(0, "")
            quantity.delete(0, len(quantity.get()))
            quantity.insert(0, "0")
            text_area.delete(0.0, tk.END)
            show_availability.delete(0, tk.END)
            if count_line > 0:
                cursor.rollback()
                cursor.close()
            count_line = float(0)
            total = float(0)
            welcome()

        # used to back in Main Page
        def back():
            clear()
            controller.show_frame(MainPage)

        # This is the head part of take order frame
        # this is the heading frame
        heading_label_frame = tk.LabelFrame(self, bg="tomato", width=600, height=42)
        heading_label_frame.place(x=0, y=0)
        # this is for heading
        heading_label = tk.Label(heading_label_frame, text="Take Order", font=("Times_New_Roman", 17, "bold"),
                                 bg="tomato", fg="khaki1")
        heading_label.place(x=240, y=5)

        # This is the section/frame to add item or generate bill
        # this is the frame for add item and generate bill
        take_order_frame = tk.LabelFrame(self, height=305, width=270, background="SlateGray1")
        take_order_frame.place(x=1, y=43)
        # for heading in take_order_frame
        head_label1 = tk.Label(take_order_frame, text="Product Details", font=("Times_New_Roman", 12, "bold"),
                               bg="SlateGray1", fg="black")
        head_label1.place(x=70, y=5)
        # Item name label
        search_label = tk.Label(take_order_frame, text="Item Name", font=("Times_New_Roman", 10))
        search_label.place(x=6, y=40)
        # it is the dash between Item name and search bar
        dash_label = tk.Label(take_order_frame, text="-", font=("Times_New_Roman", 15), bg="SlateGray1", fg="black")
        dash_label.place(x=77, y=35)
        # search bar for item
        item_search_entry = tk.Entry(take_order_frame, width=23, font=("Times_New_Roman", 10))
        item_search_entry.place(x=93, y=40)
        item_search_entry.bind('<FocusIn>', item_enter)  # while click on search bar it become empty
        # this button is for check the availability of the item
        check_button = tk.Button(take_order_frame, text="Check Availability", bd=4, background="pale green", fg="black",
                                 activeforeground="black", activebackground="pale green", command=check)
        check_button.place(x=120, y=75)
        # label for available
        availability_label = tk.Label(take_order_frame, text="  Available ", font=("Times_New_Roman", 10))
        availability_label.place(x=6, y=115)
        # dash between available label and show availability entry
        dash_label1 = tk.Label(take_order_frame, text="-", font=("Times_New_Roman", 15), bg="SlateGray1", fg="black")
        dash_label1.place(x=77, y=110)
        # its show the item is available or not
        show_availability = tk.Entry(take_order_frame, width=23, font=("Times_New_Roman", 10))
        show_availability.place(x=93, y=115)
        # label for quantity
        quantity_label = tk.Label(take_order_frame, text="  Quantity  ", font=("Times_New_Roman", 10))
        quantity_label.place(x=6, y=160)
        # dash between quantity label and quantity entry
        dash_label2 = tk.Label(take_order_frame, text="-", font=("Times_New_Roman", 15), bg="SlateGray1", fg="black")
        dash_label2.place(x=80, y=155)
        # entry to add quantity
        quantity = tk.Entry(take_order_frame, width=12, font=("Times_New_Roman", 10))
        quantity.place(x=97, y=160)
        quantity.insert(0, "0")
        quantity.bind('<FocusIn>', quantity_enter)  # onclick it become empty
        # this button is used to add item
        add_item_button = tk.Button(take_order_frame, text="Add Item", bd=4, background="pale green", fg="black",
                                    activebackground="pale green", activeforeground="black", command=add_item)
        add_item_button.place(x=197, y=157)
        # this button is used to generate bill
        generate_bill_button = tk.Button(take_order_frame, text="   Generate  Bill  ", bd=4, background="pale green",
                                         fg="black", activebackground="pale green", activeforeground="black",
                                         command=generate_bill)
        generate_bill_button.place(x=90, y=205)
        # this button clears the billing area as well as cancel the bill
        clear_button = tk.Button(take_order_frame, text="Clear Bill", bd=4, background="pale green", fg="black",
                                 activeforeground="black", activebackground="pale green", command=clear)
        clear_button.place(x=85, y=250)
        # button to back Main page
        back_button = tk.Button(take_order_frame, text="Back", bd=4, background="pale green", fg="black",
                                activeforeground="black", activebackground="pale green", command=back)
        back_button.place(x=155, y=250)

        # this section for billing area
        # frame for billing area
        billing_frame = tk.LabelFrame(self, height=305, width=328, background="white")
        billing_frame.place(x=271, y=43)
        # heading in billing area
        head_label2 = tk.Label(billing_frame, text="  Billing  Area  ", font=("Times_New_Roman", 12, "bold"),
                               bg="white")
        head_label2.pack(fill=tk.X)
        # this is the scroll bar in text area
        scrollbar = tk.Scrollbar(billing_frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # it places the scroll bar at right side
        # this is the text area where bill shows
        text_area = tk.Text(billing_frame, height=17, width=37, yscrollcommand=scrollbar.set, bg="pink")
        text_area.pack()
        scrollbar.configure(command=text_area.yview)
        # count the lines
        count_line = float(0)
        # count the total bill
        total = float(0)
        # it used at starting to start writing in text area after start it become 1
        flag = 0


# For Kitchen


class CheckOrders(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global billTable

        def check_bill():
            nonlocal bill
            text_area.delete(0.0, tk.END)
            check = bill_no_entry.get()
            if check not in order_list:
                messagebox.showerror("Error", "Bill number is not found")
            else:
                bill = check
                file_name = "bills/" + bill + ".txt"
                with open(file_name) as order:
                    text_area.insert(0.0, order.read())

        def check_orders():
            show_bills_area.delete(0.0, tk.END)
            order_list.clear()
            local_cursor = conc.cursor()
            today = str(date.today())
            local_cursor.execute("SELECT * FROM {} WHERE [ORDER DATE] = ? AND STATUS = ?".format(billTable),
                                 (today, "NO"))
            rows = local_cursor.fetchall()
            if not rows:
                show_bills_area.insert(0.0, "No Order placed Yet")
            else:
                for row in rows:
                    order_list.add(row[1])
                    show_bills_area.insert(tk.END, row[1]+"\n")
            local_cursor.close()

        def back():
            text_area.delete(0.0, tk.END)
            show_bills_area.delete(0.0, tk.END)
            bill_no_entry.delete(0, tk.END)
            bill_no_entry.insert(0, " Enter Bill Number Here")
            controller.show_frame(MainPage)

        def ready():
            nonlocal bill
            if bill == "":
                messagebox.showerror("Error", "Check bill first")
            else:
                local_cursor = conc.cursor()
                local_cursor.execute("UPDATE {} SET STATUS = ? WHERE [BILL NUMBER] = ?".format(billTable),
                                     ("YES", bill))
                local_cursor.commit()
                local_cursor.close()
                text_area.delete(0.0, tk.END)
                bill = ""

        def bill_no_enter(event):
            bill_no_entry.delete(0, tk.END)

        heading_frame = tk.Frame(self, bd=5, relief=tk.GROOVE, width=600, height=40, bg="gold")
        heading_frame.place(x=0, y=0)
        heading_label = tk.Label(heading_frame, text="Check   Orders", font=("Times_New_Roman", 13, "bold"),
                                 bg="gold", fg="black")
        heading_label.place(x=230, y=3)

        check_order_frame = tk.Frame(self, bd=5, relief=tk.GROOVE, width=270, height=307, bg="gold")
        check_order_frame.place(x=1, y=41)
        heading_label1 = tk.Label(check_order_frame, text="Search  Order  Here", font=("Times_New_Roman", 11, "bold"),
                                  bg="gold", fg="black")
        heading_label1.place(x=50, y=1)
        show_bills_area = tk.scrolledtext.ScrolledText(check_order_frame, width=16, height=10, bg="pale turquoise",
                                                       fg="red4")
        show_bills_area.place(x=1, y=30)
        check_orders_button = tk.Button(check_order_frame, text="Check \n Placed Orders", bd=4, background="khaki1",
                                        fg="red2", activeforeground="red2", activebackground="khaki1",
                                        command=check_orders)
        check_orders_button.place(x=162, y=150)
        bill_no_entry = tk.Entry(check_order_frame, width=21, font=("Times_New_Roman", 9), background="pale turquoise",
                                 fg="red4")
        bill_no_entry.place(x=3, y=220)
        bill_no_entry.insert(0, " Enter Bill Number Here")
        bill_no_entry.bind('<FocusIn>', bill_no_enter)
        check_bill_button = tk.Button(check_order_frame, text=" Check Bill ", bd=4, background="khaki1", fg="red2",
                                      activebackground="khaki1", activeforeground="red2", command=check_bill)
        check_bill_button.place(x=170, y=216)
        back_button = tk.Button(check_order_frame, text=" Back ", bd=4, background="khaki1", fg="red2",
                                activebackground="khaki1", activeforeground="red2", command=back)
        back_button.place(x=110, y=256)

        show_bill_frame = tk.Frame(self, bd=5, relief=tk.GROOVE, width=329, height=307, bg="gold")
        show_bill_frame.place(x=272, y=41)
        head_label2 = tk.Label(show_bill_frame, text="  Billing  Area  ", font=("Times_New_Roman", 12, "bold"),
                               bg="gold")
        head_label2.pack(fill=tk.X)
        scrollbar = tk.Scrollbar(show_bill_frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_area = tk.Text(show_bill_frame, height=12, width=37, yscrollcommand=scrollbar.set, bg="pale turquoise",
                            fg="red4")
        text_area.pack()
        scrollbar.configure(command=text_area.yview)
        blank_label1 = tk.Label(show_bill_frame, text=" ", font=("Times_New_Roman", 1), background="gold")
        blank_label1.pack()
        info_label = tk.Label(show_bill_frame, text=" If Order is Ready Press Ready Button ", bg="pink",
                              font=("Times_New_Roman", 8), background="gold")
        info_label.pack()
        blank_label2 = tk.Label(show_bill_frame, text=" ", font=("Times_New_Roman", 1), background="gold")
        blank_label2.pack()
        ready_button = tk.Button(show_bill_frame, text=" Ready ", font=("Times_New_Roman", 9), bd=4,
                                 background="khaki1", fg="red2", activebackground="khaki1", activeforeground="red2",
                                 command=ready)
        ready_button.pack()
        blank_label3 = tk.Label(show_bill_frame, text=" ", font=("Times_New_Roman", 2), background="gold")
        blank_label3.pack()
        order_list = set()
        bill = ""

# This part responsible for the sixe and the position(mid) of screen


app = Main()
width = 600
height = 350
screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()
x = (screenWidth/2) - (width/2)
y = (screenHeight/2) - (height/2)
app.geometry('%dx%d+%d+%d' % (width, height, x, y))
app.resizable(False, False)
app.title("Restaurant Management App")
DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'LAPTOP-AC68O3VM'
DATABASE_NAME = 'RMA'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""
try:
    conc = odbc.connect(connection_string)
    cursor = conc.cursor()
except ConnectionError:
    messagebox.showerror("Error", "Database Connectivity Issue, Please Try Again")
    app.destroy()

app.mainloop()
