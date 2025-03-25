from tkinter import *
root=Tk()
root.title("Simple Calculator")
root.geometry("600x400")

def a():
    pass


Button(root,text="1",command=a).grid(row=0,column=1)
Button(root,text="2",command=a).grid(row=0,column=2)
Button(root,text="3",command=a).grid(row=0,column=3)
Button(root,text="4",command=a).grid(row=1,column=1)
Button(root,text="5",command=a).grid(row=1,column=2)
Button(root,text="6",command=a).grid(row=1,column=3)
Button(root,text="7",command=a).grid(row=2,column=1)
Button(root,text="8",command=a).grid(row=2,column=2)
Button(root,text="9",command=a).grid(row=2,column=3)
Button(root,text="+",command=a).grid(row=3,column=1)
Button(root,text="0",command=a).grid(row=3,column=2)
Button(root,text="-",command=a).grid(row=3,column=3)
Button(root,text="x",command=a).grid(row=4,column=1)
Button(root,text="/",command=a).grid(row=4,column=2)
Button(root,text="All Clear",command=a).grid(row=4,column=3)
Button(root,text="Clear",command=a).grid(row=5,column=1)
Button(root,text="=",command=a).grid(row=5,column=2)
Button(root,text=".",command=a).grid(row=5,column=3)




root.mainloop()