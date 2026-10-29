def add(x,value=[]):#default argument
    value.append(x)
    return value
print(add(10))
print(add(20))
print(add(30,[])) # second pass argument so it creates a new list and appen only 30 in it
print(add(40))

# in the old list it only append values
# output
# [10]
# [10, 20]
[30]
[10,20,40]