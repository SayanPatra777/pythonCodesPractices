from tkinter import *
from PIL import Image , ImageTk
root=Tk()


root.geometry("1200x900")

# photo=PhotoImage("D:\python vs\GUI tkinter\MY IMAGE.jpg")

image1 = Image.open("D:\sayan passpor.jpg")
photo1 = ImageTk.PhotoImage(image1)
Label = Label(image = photo1)
Label.pack()


root.mainloop()