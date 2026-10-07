import math
class vector():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def get_vector(self):
        print("x:",self.x)
        print("y:",self.y)
    def magnitude(self):
        area=math.sqrt(self.x**2+self.y**2)
        print("area:",area)


v=vector(10,20)
v.get_vector()
v.magnitude()