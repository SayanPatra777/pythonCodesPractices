import random
num=random.randint(1,100)
print(" ## Welcome To The Guess Game ## \n\n")
count=0
for i in range (100):
    guessUser=int(input("Enter a number :"))
    if guessUser==num :
        count=count+1
        print("You've made a successful guess..!!!!!!!!!\nYou took total",count,"guesses")
        break
    elif guessUser>num:
        print("You've guess a larger number..")
        count=count+1
    else:
        print("You've guess a smaller number..")
        count=count+1