def factorial(n):
    if n==1:
        return 1
    return n+factorial(n-1)
print(factorial(4))

# n=4 4!=1 4+factorial(3)  calls factorial (stack cantain 4)
# n=3 3!=1 3+factorial(2)  calls factorial (stack cantain 4 3)
# n=2 2!=1 2+factorial(1)  calls factorial (stack cantain 4 3 2)
# n=1 1==1 4+factorial(3)  calls factorial (stack cantain 4 3 2 1)
# return 1+2+3+4=10 from stack
