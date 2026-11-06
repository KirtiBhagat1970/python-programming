#Nested Function 
def outer(x): 
    def inner(y): 
        return x + y
    return inner
add_five = outer(5) 
result = add_five(6) 
print(add_five) 
print("Final Result is :",result)  