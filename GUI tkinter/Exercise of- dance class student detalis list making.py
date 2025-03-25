from tkinter import *
root=Tk()


root.geometry("700x500")
root.title("........................Exercise of Dance Class student list making.......................")

def Joy():
    print("\nThe details of the student is: ")
    print(f"Name of the Student is: {nameval.get()} ; \nFather's name is: {fatherval.get()}; \nage is: {ageval.get()}; \n gender -> {genderval.get()}")

Label(root,text="      Name of the Student: ").grid()    #namme
Label(root,text="   Age of the Student: ").grid(row=1)   #agee
Label(root,text="Gender : ").grid(row=2)                #genderr
Label(root,text="Father's Name : ").grid(row=3)         #fatherr


nameval=StringVar()
fatherval=StringVar()
genderval=StringVar()
ageval=IntVar()

namentry=Entry(root,textvariable=nameval)
fatherentry=Entry(root,textvariable=fatherval)
genderentry=Entry(root,textvariable=genderval)
agentery=Entry(root,textvariable=ageval)

namentry.grid(row=0,column=1)
fatherentry.grid(row=1,column=1)
genderentry.grid(row=2,column=1)
agentery.grid(row=3,column=1) 

Button(root,text="Submit",command=Joy).grid(row=4,column=1)

root.mainloop()