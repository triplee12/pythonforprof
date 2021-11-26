__author__ = "Ejie Emmanuel Ebuka"

# Decorators

"""
Decorator: A decorator takes in a function, adds some functionalities and returns it.

Everything in Python is an object
That means functions can be used as objects
So we can do some really cool stuffs
"""

# Basic decorator
# Bad decorator
def test_decorator(func):
    print("Testing decorator")
    print("Before decorating")
    func()
    print("After decorating")

@test_decorator
def do_stuff():
    print("Doing stuff")

# Real decorator
def makeItalic(func):
    def inner():
        print("<i>")
        func()
        print("</i>")
    return inner # Return the inner function

@makeItalic
def test_italic():
    print("Testing italic decorator")

test_italic()

# Decorator with parameters
def number_check(func):
    def checkInt(o):
        if isinstance(o, int):
            if o == 0:
                print("Can not divide by zero")
                return False
            return True
        print(f"{o} is not a number")
        return False
    
    def inner(x, y):
        if not checkInt(x) or not checkInt(y):
            return
        return func(x, y)
    return inner

@number_check
def divide(a, b):
    print(a / b)

divide(20, "0")

# Decorator chaining
# Decorator with unknown number of parameters
# We want a decorator that can pass parameters and handle anything
# We also want to chain them together
# Here *args and **kwargs play a good role

def outline(func):
    def inner(*args, **kwargs):
        print("-" * 20)
        func(*args, **kwargs)
        print("-" * 20)
    return inner

def list_items(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print(f"args = {args}")
        for arg in args:
            print(f"arg = {arg}")
        print(f"kwargs = {kwargs}")
        for k, v in kwargs.items():
            print(f"key={k}, value={v}")
    return inner

@outline
@list_items
def display(message):
    print(message)

display("I love Python programming language",)

@outline
@list_items
def birthday( message, name, age):
    print(f"{message} {name}, you are {age} years old today.")

birthday("Happy birthday, age gracefully", "Chris", age=30)
