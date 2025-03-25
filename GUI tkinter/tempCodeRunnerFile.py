def comCompare1():
    text_entry.clear()
    choice="stone"
    choicesss= ("stone" , "paper" , "scissor")
    comChoice = random.choice(choicesss)
    text_entry.insert('end', f"The computer has chosen: {comChoice}\n")
    if(choice==comChoice):
        text_entry.insert('end',"The Game is a tie\n\n")
    elif(choice =="stone" and comChoice=="paper"):
        text_entry.insert('end',"Sorry, Computer is the winner\n\n")
    elif(choice =="scissor" and comChoice=="stone"):
        text_entry.insert('end',"Sorry, Computer is the winner\n\n")
    elif(choice == "paper" and comChoice=="scissor"):
        text_entry.insert('end',"Sorry, Computer is the winner\n\n")
    else:
        text_entry.insert('end',"Hurray!!  You Win\n\n")