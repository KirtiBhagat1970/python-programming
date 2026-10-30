def sum_even(*args):
    sum=0
    for i in args:
        if i % 2==0:
            sum=sum+i
    return sum
numbers=[1,2,3,4,5,6]           
print(sum_even(*numbers))