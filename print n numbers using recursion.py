# print n numbers using recursion 
def print_till_zero(n):
    if (n==0):
        return
    print(n)
    n=n-1
    print_till_zero(n)
a=int(input("Enter the number you want to print till 1: "))    
print_till_zero(a)