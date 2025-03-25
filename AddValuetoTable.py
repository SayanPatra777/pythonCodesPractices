num:int=int(input("Enter a num: "))
print(f"The multiplication table of {num} is: \n")
tablemultiply=[i*num for i in range (1,11)]
# print(tablemultiply)
with open ("multiplyTable.txt","a") as f:
    f.write (f"The multiplication table of {num} is:\n"+str(tablemultiply)+"\n")