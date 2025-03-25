import time as time
listMain=["Chakma","RBTiger","Virat Kholi",69,"KKR","Narendra Modi"]
listQ1=["Chakma","Goro","Tamang","Ghosh"]
listQ2=["RBTiger","Lion","Indian Elephant","kangaroo"]
listQ3=["Virat Kholi","Virndra Sehwag","Rohit Sharma","AB de villiers"]
listQ4=[69,99,31,56]
listQ5=["MI","RCB","KKR","CSK"]
listQ6=["Narendra Modi","Narendra Modi","Narendra Modi","Narendra Modi"]

print("Question:1\nWhat is the title of Terol\n1.Chakma\t2.Goro\n3.Tamang\t4.Ghosh")
n=int(input("Enter The Right Option's Number: "))
if(listQ1[n-1] in listMain):
    print("Yeaah!!, You have given the right ans. Let's move to the next question....")
    time.sleep(2)
    
    print("Question:2\nWhat is the National Animal of India\n1.RBTiger\t2.Lion\n3.Indian Elephant\t4.Kangroo")
    n=int(input("Enter The Right Option's Number: "))
    if(listQ2[n-1] in listMain):
        print("Yeaah!!, You have given the right ans. Let's move to the next question....")
        time.sleep(2)
        
        print("Question:3\nWho is the Greatest Cricketer of this era\n1.VIRAT Kholi\t2.Virndra Sehwag\n3.Rohit Sharma\t4.AB de villiers")
        n=int(input("Enter The Right Option's Number: "))
        if(listQ3[n-1] in listMain):
          print("Yeaah!!, You have given the right ans. Let's move to the next question....")
          time.sleep(2)
          
          print("Question:4\nWhat is 13^13 - 100\n1. 69\t2. 99\n3. 31\t4. 56")
          n=int(input("Enter The Right Option's Number: "))
          if(listQ4[n-1] in listMain):
            print("Yeaah!!, You have given the right ans. Let's move to the next question....")
            time.sleep(2)
            
            print("Question:5\nWhich Team do I support in IPL\n1. MI\t2. RCB\n3. KKR\t4.CSK")
            n=int(input("Enter The Right Option's Number: "))
            if(listQ5[n-1] in listMain):
                print("Yeaah!!, You have given the right ans. Let's move to the next question....")
                time.sleep(2)
                
                print("Question:\6nWhat is the greatest leader in the World \n1. Narendra Modi\t2. Narendra Modi\n3. Narendra Modi\t4. Narendra Modi")
                n=int(input("Enter The Right Option's Number: "))
                if(listQ6[n-1] in listMain):
                    print("Hurray!!, You have given right ans of all questions.Your total earning is being calculated...........")
                    time.sleep(2)
                    print(" You've earned a total ₹ 50000")
                else:
                    print("Sorry! You've made a wrong Choice. Your Total earning is ₹ 20000")
                
            else:
                print("Sorry! You've made a wrong Choice. Your Total earning is ₹ 10000")
          else:
            print("Sorry! You've made a wrong Choice. Your Total earning is ₹ 5000")
        else:
          print("Sorry! You've made a wrong Choice. Your Total earning is ₹ 2000")
    else:
        print("Sorry! You've made a wrong Choice. Your Total earning is ₹ 1000")
else:
    print("Sorry! You've made a wrong Choice. You've earn nothing..")