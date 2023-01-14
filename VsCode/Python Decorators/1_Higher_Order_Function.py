# Higher Order Function : HOC

def greet(func):        # Accept another Function as an Parameter
    func()

def greet2():           # Return a Function 
    def func():
        return 5
    
    return func

