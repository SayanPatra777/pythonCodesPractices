# sum of first n numbers
n=int(input("Enter the number : "))
s=0
for i in range (1,n+1):
    s+=i
print("The sum of first", n, "numbers is ", s)
print("The average of first", n, "numbers is ", s/n)
 