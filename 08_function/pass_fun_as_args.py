# pass function as argument 
def add(x, y):
    return x + y 
def mul(x,y): return "Mulipliaction is ", x*y 
def calculate(func, x, y): 
    return func(x, y)
result = calculate(add, 8, 20) 
res = calculate(mul,4,5)
print("Addition is ",result) 
print(res)