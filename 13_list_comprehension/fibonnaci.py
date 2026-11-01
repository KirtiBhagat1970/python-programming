#Fibonacci series using generator- yeild and next()
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
# Get first 20 Fibonacci numbers
gen = fibonacci()
for _ in range(20):
    print(next(gen))