import time as time
a="WELCOME To Sayan Bank OF Anywhere"
print(a.center(75))
CardNo=25569
PIN=722152
Bal=112042
b=int(input("Please Enter The Card Number: "))
if(b==25569):
    c = int(input("Please Enter The PIN Number: "))
    if(c==PIN):
        print("Please wait while Your Request is Processing......")
        time.sleep(4)
        print("PLease Enter The Corresponding Number to Process The Requests\n1.Cash Withdraw    \t2.Mini Statement\n3.Balance Inquiry   \t4.Cash Deposite\n5.PIN Change ")
        d = int(input())
        print("Please wait while Your Request is Processing......")
        time.sleep(4)
        match d:
            case 1:
                print("Please Enter the Amount of Money You Want to Withdraw")
                e = int(input())
                print("Please wait while Your Request is Processing......")
                time.sleep(4)
                if(e<=Bal):
                    print("Amount Withdrawn Successfully , Your Current Balance is: ",(Bal-e))
                else:
                    print("Insufficient Balance !! PLease Enter A valid Amount ")
            case 2:
                print("20106 Credited on 20/11/2022\n114 debited on 04/01/2023\n47112 debited on 16/03/2023")
            case 3:
                print("Your Balance is: ",Bal)
            case 4:
                print("Enter the Depositing Amount ")
                f=int(input())
                print("Please insert the Cash")
                print("Please wait while Your Request is Processing......")
                time.sleep(4)
                print("Your Amount of",f,"is successfully deposited in your account \n Current Balance is: ",(Bal+f))
            case 5:
                print("Enter your New PIN")
                g=int(input())
                print("A otp is sent to Your Mobile number ends with xxxxxxx740\nEnter the OTP: ")
                h=int(input())
                print("Please wait while Your Request is Processing......")
                time.sleep(4)
                print("Your PIN is successfully changed")
            case _:
                print(("You Entered Wrong Command"))
    else:
        print("You Entered Wrong PIN")
else:
    print("You Entered Wrong User Detail!!!")