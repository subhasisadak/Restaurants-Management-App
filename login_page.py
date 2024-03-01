import tkinter as tk
from tkinter import *
from PIL import ImageTk
codeFont = ("Times_New_Roman", 25)
root = tk.Tk()
width = 600
height = 300
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
x = (screenWidth/2) - (width/2)
y = (screenHeight/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(False, False)
root.title("Bill Generator")

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


def goto_crate_account():
    root.destroy()
    import creat_account_page

# this is for background image


bg_image = ImageTk.PhotoImage(file='bg1.jpeg')
bg_label = Label(root, image=bg_image)
bg_label.pack()
# login page heading
heading = Label(root, text="  First Billing  ", font=("Times_New_Roman", 25), bg="plum1", fg="SlateBlue1")
heading.place(x=200, y=10)
# Username Entry
username_entry = Entry(root, width=25, font=("Times_New_Roman", 11), fg='blue')
username_entry.place(x=190, y=80)
username_entry.insert(0, "Username")
username_entry.bind('<FocusIn>', user_enter)
# password Entry
password_entry = Entry(root, width=25, font=("Times_New_Roman", 11), fg='blue')
password_entry.place(x=190, y=120)
password_entry.insert(0, "Password")
password_entry.bind('<FocusIn>', password_enter)
# button to hide or show password
open_eye = ImageTk.PhotoImage(file='openeye.png')
close_eye = ImageTk.PhotoImage(file='closeye.png')
eye_button = Button(root, image=open_eye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
eye_button.place(x=400, y=118)
# Button to login
login_but = Button(root, text="Login", font=("Times_New_Roman", 9), cursor='hand2', bd=0, width=10, fg="blue",
                   activeforeground="blue")
login_but.place(x=250, y=160)
# help to get user id and password in case you forgot the password
forgot_password_but = Button(root, text='Forgot Password ?', bd=0, bg='white', activebackground='white',
                             cursor='hand2', font=("Times_New_Roman", 9), fg='blue', activeforeground='blue')
forgot_password_but.place(x=235, y=200)
# A line between login section and create account
frame_line = Frame(root, width=400, height=2, bg='white')
frame_line.place(x=100, y=235)
# button to create a new account
create_account_but = Button(root, text="Create Account", font=("Times_New_Roman", 9), cursor='hand2', bd=0,
                            width=20, fg="blue", activeforeground="blue", command=goto_crate_account)
create_account_but.place(x=220, y=250)

root.mainloop()
