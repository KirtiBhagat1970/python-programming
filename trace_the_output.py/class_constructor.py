class Student:
    def __init__(self,marks):
        self.marks=marks # self.marks is a object variable
    def update(self,marks):
        marks=marks+10 # this marks variable is local 
        self.marks=self.marks+5
s=Student(50)
s.update(60)
print(s.marks) # so it print 55 object variable
