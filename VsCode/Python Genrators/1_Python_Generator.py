# Python Generator

def generator_function(num):
    for i in range(num):
        yield i*2            # Yield pauses the function and comes back when next is being called on generator object.

g = generator_function(100)
next(g)
print(next(g))