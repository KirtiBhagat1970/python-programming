numbers=[15,10,30,9,45,20,60]
divisible=list(filter(lambda x: x%3==0 and x%5==0, numbers))
print(divisible)
