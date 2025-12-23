#create a class Student that takes 3 marks and has a method average()
class student:
    def __init__(self,marks1,marks2,marks3):
        self.marks1=marks=int(input("enter marks"))
        self.marks2=marks2
        self.marks3=marks3
    def average(self):
        avg=(self.marks1+self.marks2+self.marks3)/3
        print("average of 3 subjects: ",avg)
#creating object
s=student(100,200,300)
s.average()          