from tkinter import *
root =Tk()
root.geometry("700x500")


#function
def joy():
    print("SAYAN")

f1=Frame(root)
f1.pack(anchor=SW)

b1=Button(f1,fg="red",text="presss",command=joy)
b1.pack()

b2=Button(f1,fg="red",text="presss",command=joy)
b2.pack()

b3=Button(f1,fg="red",text="presss",command=joy)
b3.pack()

b4=Button(f1,fg="red",text="presss",command=joy)
b4.pack()


root.mainloop()