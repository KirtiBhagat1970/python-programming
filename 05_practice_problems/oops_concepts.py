class user:
    def get(self):
        self.name=input("enter your name:")
        self.email=input("enter your email:")
class student(user):
    def display(self):
        print("student name:",self.name)
        print("student email:",self.email)
class admin(user):
    def displaya(self):
        print("admin name:",self.name)
        print("admin email:",self.email)

obj=student()
obj1=admin()
obj.get()
obj.display()
obj1.get()
obj1.displaya()


                

                
                

                
