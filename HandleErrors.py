__author__ = "Ejie Emmanuel Ebuka"

# Try, Except and Finally

# Errors handling
# Bad thing happens, we need to know how to handle them

"""
Errors mostly occur at runtime that's they belong to an unchecked type.
Exceptions are the problems which can occur at runtime and compile time.
It mainly occurs un the code written by the developers.
Exceptions are divided into two categories such as:
Checked exceptions and Unchecked exceptions.
"""

def outline(func):
    def inner(*args, **kwargs):
        print("-" * 20)
        print(f"Function: {func.__name__}")
        func(*args, **kwargs)
        print("-" * 20)
    return inner

@outline
def test_check_one(x, y):
    try:
        result = x / y
        print(f"Result: {result}")
    except:
        print(f"Something bad happened x: {x}, y:{y}")
    finally:
        print('Check completed')

test_check_one(4, 0)

@outline
def test_check_two(x, y):
    try:
        assert(x > 0)
        assert(y > 0)
    except AssertionError as e:
        print(f"AssertionError occured x: {x} and y: {y} failed to assert.")
    except Exception as e:
        print(f"Something bad happened x: {x}, y:{y}, error: {e}")
    else:
        result = x / y
        print(f"Result: {result}")
    finally:
        print('Check completed')

test_check_two(56, "a")
test_check_two(3, 0)
test_check_two(3, 2)

# User defined exceptions and raising
class MyException(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

@outline
def test_myexcpt(qty):
    try:
        if not isinstance(qty,int):
            raise TypeError("Must be an integer")
        if qty < 9 :
            raise MyException("Must own more than 9 animals")
    except Exception as e:
        print(f"Oops! Something went wrong {e.args}")
    finally:
        print("MyException working")

test_myexcpt(1)
test_myexcpt("Dog")
test_myexcpt(100)