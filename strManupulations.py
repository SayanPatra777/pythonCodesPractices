# def strRev(a):
#     a=a[::-1]
#     return a

# a=input("Enter the string:")
# l=strRev(a)
# if(a==l):
#     print(l,"is a  ")
# else:
#     print("Fuck you")
t=("Cat","dogs","Human")
temp=list(t)
temp.append("Cow")
temp.pop(2)
temp[2]=2
t=tuple(temp)
print(t)
