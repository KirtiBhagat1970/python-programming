# Nested Function
def outer(): 
    message = "Hello from outer"
    def inner():
        print(message) 
    inner() 
outer()