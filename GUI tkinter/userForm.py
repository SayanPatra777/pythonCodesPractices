from tkinter import *

root=Tk()
def SubmissionConfirmation():
    print(f"The username is {userval.get()} and the password is {passval.get()}  & The male checkbox value is {maleval.get()} and female checkbox value is {femaleval.get()}\n\nThe record has submitted")

    with open ("listA.txt","a") as f:
        f.write(f"The username is {userval.get()} and the password is {passval.get()}  & The male checkbox value is {maleval.get()} and female checkbox value is {femaleval.get()}\n\nThe record has submitted")


        
Label(root,text="Form of Application",font=(SUNKEN,20)).grid(row=0,column=2,padx=25)
root.title(" form of MYself")


Label(root,text="UserName",font=(SUNKEN,20)).grid(row=1,column=0,pady=8,padx=15)
Label(root,text="Password",font=(SUNKEN,20)).grid(row=2,column=0,pady=8,padx=15)


userval=StringVar()
passval=StringVar()
maleval=IntVar()
femaleval=IntVar()

Entry(root,textvariable=userval,borderwidth=5).grid(row=1,column=1)
Entry(root,textvariable=passval,borderwidth=5).grid(row=2,column=1)



Checkbutton(text="Male",variable=maleval).grid(row=3,column=1,padx=5)
Checkbutton(text="Female",variable=femaleval).grid(row=4,column=1,padx=5)

Button(root,text="SUBMIT",command=SubmissionConfirmation,borderwidth=5).grid(row=3,column=2,padx=5,pady=5)




root.geometry("650x400")

root.mainloop()