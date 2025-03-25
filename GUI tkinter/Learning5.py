from tkinter import *
from PIL import Image , ImageTk
root=Tk()

root.geometry("1000x650")
root.title("NEWS PAPER")


Label1=Label(text="SAYAN NEWS PAPER",bg="white",font=("GROOVE",80,"bold"))
Label1.pack()


f1=Frame(root,background="red",relief=SUNKEN,borderwidth=20)
f1.pack(anchor=SW,fill=BOTH,side=TOP)
Label2=Label(text='''Narendra Damodardas Modi  born 17 September 1950 \nis an Indian politician who has served as the 14th prime minister of India \nsince May 2014. Modi was the Chief Minister of Gujarat from \n2001 to 2014 and is the Member of Parliament (MP) for Varanasi. He is a\n member of the Bharatiya Janata Party (BJP) and of the Rashtriya Swayamsevak Sangh (RSS),\n a right-wing Hindu nationalist paramilitary volunteer organisation. He is the longest-serving \nprime minister from outside the Indian National Congress.''')
image1 = Image.open("C:/Users/Sayan Patra/Desktop/paper photographs/OIP.jpg")
photo = ImageTk.PhotoImage(image1)
Label3 = Label(f1,image=photo)
Label3.pack(anchor=SW)
Label2.pack(anchor=SE)
# Label1=Label(text="")

root.mainloop()