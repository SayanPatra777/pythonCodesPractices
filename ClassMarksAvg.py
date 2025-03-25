# marks=[12,45,23,65,33]
# print()
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg_marks(self):
        return sum(self.marks)/len(self.marks)
    

marks=[]
nam=input("Enter your name: ")
keys=int(input("Enter the number of your subjects: "))
print("Enter your numbers one by one: ")
for i in range (keys):
    marks.append(int(input()))
s=Student(nam,marks)
print(f"{s.name} your average number is: {s.avg_marks()}")
# print(Student("Sayan Patra",[100,90,90]).avg_marks())
