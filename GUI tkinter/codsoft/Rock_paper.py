from tkinter import *
import random
root=Tk()
root.title("Rock Paper scissor")
root.geometry("800x600")


def comCompare1():
    #text_entry.delete('1.0', 'end')
    choice="stone"
    choicesss= ("stone" , "paper" , "scissor")
    comChoice = random.choice(choicesss)
    text_entry.insert('end', f"You have choosen: {choice}\n&  The computer has chosen: {comChoice}\n\n")
    if(choice==comChoice):
        text_entry.insert('end',"The Game is a tie\n\n\n")
    elif(choice =="stone" and comChoice=="paper"):
        text_entry.insert('end',"Sorry, Computer is the winner\n\n\n")
    elif(choice =="scissor" and comChoice=="stone"):
        text_entry.insert('end',"Sorry, Computer is the winner\n\n\n")
    elif(choice == "paper" and comChoice=="scissor"):
        text_entry.insert('end',"Sorry, Computer is the winner\n\n\n")
    else:
        text_entry.insert('end',"Hurray!!  You Win\n\n\n")

def comCompare2():
    #text_entry.delete('1.0', 'end')
    choice="paper"
    choicesss= ("stone" , "paper" , "scissor")
    comChoice = random.choice(choicesss)
    text_entry.insert('end', f"You have choosen: {choice}\n&  The computer has chosen: {comChoice}\n\n")
    if(choice==comChoice):
        text_entry.insert('end',"The Game is a tie\n\n\n")
    elif(choice =="stone" and comChoice=="paper"):
        text_entry.insert('end',"Sorry, Computer is the winner\n\n\n")
    elif(choice =="scissor" and comChoice=="stone"):
        text_entry.insert('end',"Sorry, Computer is the winner\n\n\n")
    elif(choice == "paper" and comChoice=="scissor"):
        text_entry.insert('end',"Sorry, Computer is the winner\n\n\n")
    else:
        text_entry.insert('end',"Hurray!!  You Win\n\n\n")
        
def comCompare3():
    # text_entry.delete('1.0', 'end')
    choice="scissor"
    choicesss= ("stone" , "paper" , "scissor")
    comChoice = random.choice(choicesss)
    text_entry.insert('end', f"You have choosen: {choice}\n&  The computer has chosen: {comChoice}\n\n")
    if(choice==comChoice):
        text_entry.insert('end',"The Game is a tie\n\n\n")
    elif(choice =="stone" and comChoice=="paper"):
        text_entry.insert('end',"Sorry, Computer is the winner\n\n\n")
    elif(choice =="scissor" and comChoice=="stone"):
        text_entry.insert('end',"Sorry, Computer is the winner\n\n\n")
    elif(choice == "paper" and comChoice=="scissor"):
        text_entry.insert('end',"Sorry, Computer is the winner\n\n\n")
    else:
        text_entry.insert('end',"Hurray!!  You Win\n\n\n")

def clrScreen():
    text_entry.delete('1.0', 'end')

text_entry = Text(root, width=40, height=10)
text_entry.place(x=100, y=150)
Label(root,text="   Click on Your choice : ",font=" 23 ").grid(column=2,pady=20)
Button(root,text="Stone",command=comCompare1).grid(row=2,column=3,pady=3,padx=15)
Button(root,text="Paper",command=comCompare2).grid(row=2,column=4,pady=3,padx=15)
Button(root,text="Scissor",command=comCompare3).grid(row=2,column=5,pady=3,padx=15)
Button(root,text="Clear Screen",command=clrScreen).grid(row=3,column=4,pady=6,padx=15)
    
    
    
root.mainloop()