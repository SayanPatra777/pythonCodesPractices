from tkinter import *
root=Tk()
root.geometry("700x500")

def Joy():
    print(uservalue.get())
    print(passvalue.get())

user=Label(root,text="User Name")
passWard =Label(root,text="Passward")
user.grid(row=0,column=0)
passWard.grid(row=1,column=0)

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(root,text="Submit",command=Joy).grid(row=3,column=2)

root.mainloop()