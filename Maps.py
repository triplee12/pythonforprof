__author__ = "Ejie Emmanuel Ebuka"

# Map
# Looping a collection of items without a loop
# Map(func, iterable)

# Basic Usage
animals = ["dog", "cat", "bear", "lion", "tiger"]

# Old way of doing it
counts = []
for x in animals:
    counts.append(len(x))
print(f"Old way: {counts}")

# Modern way
print(f"Modern way: {list(map(len, animals))}") # Simple and short

# More complex
fruites = ("Apple", "Choclate", "Fudge", "Pizza")
reciept = ("Pie", "Cake", "Brownies")

def merge_f_r(f, r):
    return f + " " + r

fr = map(merge_f_r, fruites, reciept)
print(list(fr))

# Multiple functions
# Call multiple functions in one map call

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def subtract(x, y):
    return x - y

def myMath(func, num):
    return func(num[0], num[1])

tuple_func = (add, multiply, divide, subtract)
value = [[20, 2]]
number = list(value) * len(tuple_func)
f_map = map(myMath, tuple_func, number)
print(list(f_map))
