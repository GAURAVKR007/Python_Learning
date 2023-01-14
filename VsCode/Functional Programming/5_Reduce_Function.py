from functools import reduce
my_list = list(range(21))

def counting(acc,i):
    print(acc,i)
    return acc + i

print(reduce(counting,my_list,0))