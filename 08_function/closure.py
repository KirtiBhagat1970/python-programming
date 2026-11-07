# Closure example
def multiplier(factor):
    def inner(number):
        return number * factor
    return inner 
double = multiplier(2)
triple = multiplier(3) 
print(double(5))  
print(triple(5))  