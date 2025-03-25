import random
choice = input("Enter your choice (Stone or Paper or Scissor): ")
choicesss= ("stone" , "paper" , "scissor")
comChoice = random.choice(choicesss)
print("The computer has chosen: ",comChoice)
if(choice.lower()==comChoice):
    print("Tie")
elif(choice.lower =="stone" and comChoice=="paper"):
    print("Computer wins")
elif(choice.lower =="scissor" and comChoice=="stone"):
    print("Computer Wins")
elif(choice.lower == "paper" and comChoice=="scissor"):
    print("Computer Wins")
else:
    print("You win")