# using nonlocal 
def myfunc1(): 
    x = "kirti" 
    def myfunc2(): 
        nonlocal x 
        x = "hello" 
    myfunc2() 
    return x 
print(myfunc1())
