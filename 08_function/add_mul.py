def operation_factory(op):
    def add(a, b):
        return a + b 
    def mul(a, b):
        return a * b 
    if op == "add":
        return add 
    else: 
        return mul
f = operation_factory("mul")
print(f(3, 4))  