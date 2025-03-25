import random
import string



def passwordGenerate(length):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation


    final = letters + digits + special_chars

    password =  ''.join(random.choice(final) for _ in range(length))
    return password

length =int(input("Enter Your Password length: "))
print(f"Your {length} digit password is : {passwordGenerate(length)}")
ans=input("Again You want to generate a password (only yes / no):")
for i in range (1,401):
    if ( ans.lower() == "yes"):
        length =int(input("Enter Youe Password length:"))
        print(f"Your {length} digit password is : {passwordGenerate(length)}")
    elif(ans.lower() == "no"):
        break
    else:
        print("You've entered a wrong command !!!!!!!!!!!!!!!")
        break
