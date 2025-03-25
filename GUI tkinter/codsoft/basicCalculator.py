#Noemal Calculator
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
# Sayan
OperInput=int(input("Enter Your Choice:->\nEnter 1 for Addition\nEnter 2 for Substraction\nEnter 3 for multiplication \nEnter 4 for Division\n"))
match OperInput:
    case 1:
        print("Result of Addition :",num1+num2)
    case 2:
        print("Result of Substraction :",num1-num2)
    case 3 :
        print("Result of Multiplication :",num1*num2)
    case 4 :
        print("Result of Division :",num1/num2)
