class Test:
    count=0
    def __init__(self):
        Test.count+=1
a=Test()
b=Test()
c=Test()
print(a.count,b.count,c.count)

# count is a class variable
# when the object is created every time the init function is called and count increase
# the output is 3 3 3
# not 1 2 3 because it is aclass variable not specific object