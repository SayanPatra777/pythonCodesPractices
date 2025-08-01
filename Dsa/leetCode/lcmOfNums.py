# num1=int(input("Enter Num1: "))
# num2=int(input("Enter Num2: "))

# for i in range (max(num1,num2),num1*num2+1):
#     if (i%num1==0) and (i%num2==0):
#         break
# print (i)

nums = list(map(int, input("Enter the Numbers in the array separated with space :\n").split()))
sumOfElements=0
sumOfList=0
for number in nums:
    sumOfElements^=number
# print(sumOfElements)

for i in range (1,len(nums)+1):
    sumOfList^=i
# print(sumOfList)
print(sumOfElements^sumOfList)
