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


# this is for background image
bg_image = ImageTk.PhotoImage(file='bg1.jpeg')
bg_label = Label(root, image=bg_image)
bg_label.pack()
# create account page heading
heading = Label(root, text="  Create Account  ", font=("Times_New_Roman", 25), bg="plum1", fg="SlateBlue1")
heading.place(x=180, y=10)

# Its use to clear the String "Email" on click


def email_enter(event):
    if email_entry.get() == "Email":
        email_entry.delete(0, len("Email"))

# Its use to clear the String "username" on click


def user_enter(event):
    if username_entry.get() == "Username":
        username_entry.delete(0, len("Username"))

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


def goto_login_page():
    root.destroy()
    import login_page

# Email Entry


email_entry = Entry(root, width=25, font=("Times_New_Roman", 11), fg='blue')
email_entry.place(x=210, y=70)
email_entry.insert(0, "Email")
email_entry.bind('<FocusIn>', email_enter)
# Username Entry
username_entry = Entry(root, width=25, font=("Times_New_Roman", 11), fg='blue')
username_entry.place(x=210, y=110)
username_entry.insert(0, "Username")
username_entry.bind('<FocusIn>', user_enter)
# password Entry
password_entry = Entry(root, width=25, font=("Times_New_Roman", 11), fg='blue')
password_entry.place(x=210, y=150)
password_entry.insert(0, "Enter Password")
password_entry.bind('<FocusIn>', password_enter)
# button to hide or show password
open_eye1 = ImageTk.PhotoImage(file='openeye.png')
close_eye1 = ImageTk.PhotoImage(file='closeye.png')
eye_button1 = Button(root, image=open_eye1, bd=0, bg='white', activebackground='white', cursor='hand2',
                     command=hide1)
eye_button1.place(x=420, y=148)
# Confirm Password Entry
confirm_password_entry = Entry(root, width=25, font=("Times_New_Roman", 11), fg='blue')
confirm_password_entry.place(x=210, y=190)
confirm_password_entry.insert(0, "Confirm Password")
confirm_password_entry.bind('<FocusIn>', confirm_password_enter)
# button to hide or show password
open_eye2 = ImageTk.PhotoImage(file='openeye.png')
close_eye2 = ImageTk.PhotoImage(file='closeye.png')
eye_button2 = Button(root, image=open_eye2, bd=0, bg='white', activebackground='white', cursor='hand2',
                     command=hide2)
eye_button2.place(x=420, y=188)
# Check terms and condition
terms_and_condition = Checkbutton(root, text="I Agree to the Terms & Conditions", font=("Times_New_Roman", 9),
                                  bg='powder blue', activebackground='powder blue',
                                  activeforeground="blue", fg="blue", cursor='hand2')
terms_and_condition.place(x=210, y=230)
# Button to create account
crate_but = Button(root, text="Create", font=("Times_New_Roman", 9), cursor='hand2', bd=0, width=10,
                   fg="blue")
crate_but.place(x=220, y=265)
back = Button(root, text="Back", font=("Times_New_Roman", 9), cursor='hand2', bd=0, width=10,
              fg="blue", command=goto_login_page)
back.place(x=330, y=265)

root.mainloop()
