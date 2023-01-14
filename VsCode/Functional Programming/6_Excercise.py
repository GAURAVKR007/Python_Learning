from functools import reduce
my_pets = ['sisi', 'bibi', 'titi', 'carla']
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
#part 1
def capitalize(item):
    return item.upper()

print(list(map(capitalize, my_pets)))

#part 2
my_numbers.sort()
print(list(zip(my_strings, my_numbers)))

#part 3
scores = [73,20,65,19,76,100,88]
def pass_test(score):
    return score > 50
print(list(filter(pass_test, scores)))

#part 4
def adder(acc, item):
    return acc + item
print(reduce(adder, my_numbers, sum(scores)))