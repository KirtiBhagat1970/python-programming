# Using Non local
def outer():
    x = "enclosing"
    #y = 3
    def inner(): 
        nonlocal x
        x = "modified by nonlocal"
    inner() 
    print("Outer:", x)
outer()