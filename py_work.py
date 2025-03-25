n=int(input("Enter the number of rows: "))
if(n%2==0):
    l=int((n/2)+2)
else:
    l = int((n+1)/2)+1
for i in range (1,l):
    for j in range (1,i+1) :
        print(j,end =" ")
    print(" ")


for i in range(l,0,-1):
    for j in range (1,i-1):
        print(j,end=" ")
    print(" ")