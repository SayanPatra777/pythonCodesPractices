num:int=int(input("Enter a num: "))
print(f"The multiplication table of {num} is: \n")
tablemultiply=[i*num for i in range (1,11)]
print(tablemultiply)