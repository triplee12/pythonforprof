import random


__author__ = "Ejie Emmanuel Ebuka"

# Iterators
# Making counting easy

tuples = (1, 2, 3, 4, 5)
for t in tuples:
    print(t) # How does it work?

# Iter basic
# Lists, tuples, dictionaries, and sets are all iterable objects.
# They are iterable objects which we can get an iterator from.

people = ["Chris", "John", "Philip"]
i = iter(people)
print(list(i)) # Works as for loop. The same thing as for loop above but iter is more time efficient
# print(next(i)) # Using next() method to print the elements

# Iterable class
class Lottery:
    def __init__(self):
        self._max = 10
    
    def __iter__(self):
        # Using yield to return results
        # The yield statement suspends funtion's execution
        # and sends a value back to the caller, but retains enough
        # state to enable function to resume where it left off.
        for _ in range(self._max):
            yield random.randrange(0, 100)
    
    def setMax(self, max):
        self._max = max

print("-" * 20)
lottery = Lottery()
lottery.setMax(50)
for i in lottery:
    print(i)
print("-" * 20)
