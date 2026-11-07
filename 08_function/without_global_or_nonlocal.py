#without global or nonlocal
x = "global"
def outer():
    x = "enclosing"
    def inner(): 
        x = "local"
        print("Inner:", x)
    inner() 
    print("Outer:", x) 
outer() 
print("Global:", x)