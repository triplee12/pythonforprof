import pickle

__author__ = "Ejie Emmanuel Ebuka"

# Pickle
# dill
# Serializing objects
# Saving and loading objects and their properties
# Python data types, and top level classes

def outline(func):
    def inner(*args, **kwargs):
        print("-" * 20)
        print(f"Function: {func.__name__}")
        func(*args, **kwargs)
        print("-" * 20)
    return inner

# Serialization
class Animal:
    def __init__(self, name, age, description):
        self._name = name
        self._age = age
        self._description = description
    
    @outline
    def display(self, message=""):
        print(message)
        print(f"{self._name} is {self._age} years old.")
        for k, v in self._description.items():
            print(f"{k} : {v}")

animal = Animal("Blue D", 3, dict(color="gray", weight="4.63", hairy=True))
animal.display("I love Blue D.")

# Serialize
animal_s = pickle.dumps(animal)
print(animal_s)

# save
with open("mypickle/animal.txt", "wb") as f:
    pickle.dump(animal, f)

# Deserialization
myAnimal = pickle.loads(animal_s)
myAnimal.display("Display deseriazed")

with open("mypickle/animal.txt", "rb") as f:
    myAnimal_d = pickle.loads(animal_s)
    myAnimal_d.display("Display deseriazed from disk")
