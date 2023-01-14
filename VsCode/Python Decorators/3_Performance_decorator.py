from time import time

def performance(func):
    def wrap_func(*args,**kwargs):
        t1 = time()
        result = func(*args,**kwargs)
        t2 = time()
        print(f'\n Time taken => {t2 -t1} sec')
        return result
    return wrap_func



@performance
def long_time():
    my_list = []
    for i in range(10000000):
        my_list.append(int((i**2)/3 + 5 - 10))
    return my_list

long_time()