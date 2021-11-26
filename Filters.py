import random

__author__ = "Ejie Emmanuel Ebuka"

# Filter
# filter(func, iterables)
# returns True if it matches the filter

# Sub range

v = []
for x in range(10):
    v.append(random.randrange(100))
print(v)

def lowerthan50(value):
    if value < 50:
        return True
    else:
        return False

f = filter(lowerthan50, v)
print(f"Less than 50: {list(f)}")

# Filter types

class People:
    name = ''
    def __init__(self, name):
        self.name = name

class Male(People):
    def __init__(self, name):
        super().__init__(name)


class Female(People):
    def __init__(self, name):
        super().__init__(name)

people = []
for x in range(10):
    name = 'People ' + str(x)
    if (x % 2) == 0:
        # Even number
        people.append(Male(name))
    else:
        # Odd number
        people.append(Female(name))


for p in people:
    print(f'People: {p.name}')

# filter male
def male(value):
    return isinstance(value, Male)

# filter female
def female(value):
    return isinstance(value, Female)

for m in list(filter(male, people)):
    print(f'Male: {m.name}')

for f in list(filter(female, people)):
    print(f'Female: {f.name}')
