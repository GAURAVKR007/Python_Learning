# Generator for Fibonacci Series

def fibonacci(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b



fib = fibonacci(21)
for i in fib:
    print(i)
    