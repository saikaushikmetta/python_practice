class name:
    schoolname="MMPS"
    def __init__(self,name,course):
        self.name=name
        self.course=course
        print(self.name)
        # print("whenever a new object is created i am called automatically")
        # print(self)
student1=name("kaushik","DIPLOMA")#init method will be called
print("student1 name",student1.name)
print("student1 course",student1.course)
student2=name("khushi","DIPLOMA")
print("student2 name",student2.name)
print("student2 course",student2.course)
