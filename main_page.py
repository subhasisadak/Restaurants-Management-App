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
bg_image = ImageTk.PhotoImage(file='bg1.jpeg')
bg_label = Label(root, image=bg_image)
bg_label.pack()
update_button = Button(root, text=" For Update or Add Items ", bd=5, font=("Times_New_Roman", 13), bg="plum1",
                       fg="DarkOrchid4", cursor="hand2", activeforeground="DarkOrchid4", activebackground="plum1")
update_button.place(x=180, y=40)
take_order_button = Button(root, text=" For Take Order ", bd=5, font=("Times_New_Roman", 13), bg="plum1",
                           fg="DarkOrchid4", cursor="hand2", activeforeground="DarkOrchid4", activebackground="plum1")
take_order_button.place(x=218, y=120)
check_order_button = Button(root, text=" Check Orders ", bd=5, font=("Times_New_Roman", 13), bg="plum1",
                            fg="DarkOrchid4", cursor="hand2", activeforeground="DarkOrchid4", activebackground="plum1")
check_order_button.place(x=221, y=200)
back_button = Button(root, text=" Back ", bd=5, font=("Times_New_Roman", 13), bg="plum1",
                     fg="DarkOrchid4", cursor="hand2", activeforeground="DarkOrchid4", activebackground="plum1")
back_button.place(x=260, y=280)
root.mainloop()
