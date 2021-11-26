__author__ = "Ejie Emmanuel Ebuka"

# Underscore

"""
Underscore:

- _Single underscore
- __Double underscore
- __Before underscore
- After underscore__
- __Both underscore__
"""

# Skipping
for _ in range(5): # Using single underscore here means that python should overlook variable
    print("Hello") # Our program still runs as expected

# Using _ Before underscore in class
# Before (single) underscore
# Internal use only, called a weak private
class Person:
    _name = "Oops! No name" # weak private variable. Use internally
    
    # Before and After underscore
    # Considered special to Python, like in the __init__() and __str__() functions
    def __init__(self):
        print("Constructor")
    
    def setName(self, name):
        self._name = name
        print(self._name)
    
    # Double underscore
    # Internal use only, avoid conflict in subclasses
    # and tells python to rewrite the name (Mangling)
    # Strong private
    def __walk(self): # Strong private variable. Can only access inside its class scope 
        # To make something more private then go ahead and use double underscore
        print("Walking to get fit")
    
    def fit(self):
        self.__walk()
    
    # Our custom before and after underscore function
    def __go__(self):
        print("GO after me, move it move it don't give up")


class ChildP(Person):
    def testDouble(self):
        self.__walk(self)

person = Person()
person.setName("Chris")
print(f"Weak private variable {person._name}")
person._name = "Don't do this" # Use weak private variable unless you know what you are doing.
print(f"Weak private variable {person._name}")

person2 = Person()
person2.fit()
# person2.__walk() # We can never reach this point
cp = ChildP()
cp.fit()
# cp.__walk() # Oops! We can't reach this point even though we inherited the parent class
# cp.testDouble() # Oops! the same thing happened here

# After underscore (Any)
# Helps to avoid naming conflicts (collisions) with keywords in Python
class_ = Person() # After (Any) underscore
class_.fit()


# Before and after underscore
# Considered special to Python, like in the __init__() and __str__() functions
class_.__go__()