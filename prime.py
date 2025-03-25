def primeproduct(n):
     x=0
     if(n<2):
         print("False")
     else:
         for i in range (2,n):
             if(n%i==0):
                 x=x+1
     if(x==2):
         print("True")
     else:
         print(("False"))
primeproduct(int(input("Enter the number: ")))
