#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        


# 1 Instantiate the Cat object with 4 cats

cat1 = Cat("Tom",21)
cat2 = Cat("Oggy",17)
cat3 = Cat("Jack",23)
cat4 = Cat("Stray",14)


# 2 Create a function that finds the oldest cat
old = 0

def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f"The oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age, cat4.age)} years old.")