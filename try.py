from tkinter import *
from PIL import ImageTk, Image
root = Tk()
img = Image.open('C:\\Users\\User\\Desktop\\code with vs code\\BillGenerator_Project\\bg1.jpeg')
bgImage=ImageTk.PhotoImage(img)
bgLabel = Label(root, image=bgImage)
bgLabel.pack()
root.mainloop()