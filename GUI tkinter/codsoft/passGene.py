import random
import string
from tkinter import *
root=Tk()
root.title("Strong Password Generator")
root.geometry("700x450")

# Get user input 
UserEntry=IntVar()
UserEntry.set("")
Entry(root,textvariable=UserEntry).grid(row=1,column=1)

Label(root,text="Enter passsword length",fg="blue").grid(padx=5,pady=5,row=1)

def passMaking():
    Plength=int(UserEntry.get())
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    final = letters + digits + special_chars
    password =  ''.join(random.choice(final) for _ in range(Plength))
    text_entry.insert('end', f"{password}\n\n")
    
    
# Create the Text widget and then place it
Label(root,text="Your Strong Password is: ").grid(row=15,column=1,padx=3,pady=3)
text_entry = Text(root, width=40, height=10)
text_entry.place(x=100, y=90)


Button(root,text="Generate pass",command=passMaking).grid(padx=5,pady=5,row=12,column=1)
    
root.mainloop()