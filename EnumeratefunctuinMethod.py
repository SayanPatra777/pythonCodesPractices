multiplyList = [1,2,3,4,5,6,7,8,9,10]
num:int =int(input("Enter the number: "))
print(f"The multiplication table of {num} is:\n")
for i , item in enumerate(multiplyList):
    print(f"{num} x {i+1} = {num*(i+1)}")
