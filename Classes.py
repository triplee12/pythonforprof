import json
import os


__author__ = "Ejie Emmanuel Ebuka"

# Introduction to classes

"""
Class: A class is a blue print for creating object.
Object is an instance of a class

- OOP - Object Oriented Programming
- Blue prints for creating objects
"""

# Creat class
# self is the first parameter and it is equal to "this" in some languages
class Dog:
    def __init__(self, name=None, age=None, color=None): # Constructor: self is required and other parameters are optional
        self.name = name
        self.age = age
        self.color = color
    
    def bark(self): # Object
        print(f"{self.name} bark")
    
    def eat(self): # Object
        print(f"{self.name} eating")
    
    def sleep(self): # Object
        print(f"{self.name} zzzzz sleeping")
    
    def detail(self): # Object
        print(f"{self.name} is {self.age} years old and it is {self.color}")

# Let us test our class
def test():
    dog = Dog("Cruker", 5, "clay") # instance of Dog class
    dog.bark()
    dog.eat()
    dog.sleep()
    dog.detail()

if __name__ == "__main__":
    test()

# Class inheritance
# A class can inherit or include the attributes of other classes.
# Feline class
class Feline:
    def __init__(self, name):
        self.name = name
        print("Feline class: {name}")
    
    def bark(self):
        print(f"{self.name} bark")
    
    def eat(self):
        print(f"{self.name} eating")
    
    def setName(self, name):
        print(f"{self} setting name: {name}")
        self.name = name

# Shita class
class Shita(Feline):
    def bark(self):
        print(f"{self.name} bark")


# Tiger class
class Tiger(Feline):
    def __init__(self):
        # Super allows us to access the parent class
        # if we forget this, we will have a bad time later
        super().__init__("Tiger")
        print("Creating Tiger")
    
    def run(self):
        # Have to make sure name is set in the parent class
        # this is considered - LBYL (look before you leap)
        # here we are dynamically adding the attributes
        
        # if we did not initialize the super, then we will have to be careful
        # if not hasattr(self, 'name'): super.setName("any name")
        print(f"{self.name} running")
    
    def rename(self, name):
        super().setName(name)
        print(f"{self.name} renamed")

def animals():
    f = Feline("Jaspe")
    f.bark()
    f.setName("Notcha")
    s = Shita("Crawa")
    s.bark()
    s.setName("Brower")
    s.eat()
    t = Tiger()
    t.run()
    t.rename("Tigeress")

if __name__ == "__main__":
    anim = animals()

# Multiple Inheritance
# Inherit from multiple classes at the same time

# Vihical class
class Vihical:
    speed = 0
    def drive(self, speed):
        self.speed = speed
        print("Driving...")
    
    def stop(self):
        self.speed = 0
        print("Stopped")
    
    def display(self):
        print(f"Driving at {self.speed} speed")


# Freezer class
class Freezer:
    temp = 0
    def freeze(self, temp):
        self.temp = temp
        print("Freezing...")
    
    def display(self):
        print(f"Freezing at {self.temp} temp")

# Freezer Truck class
class FreezerTruck(Freezer, Vihical): # Here we define the Method Resolution Order  (MRO). First come First serve
    def display(self):
        print(f"Is a freezer: {issubclass(FreezerTruck, Freezer)}")
        print(f"Is a vihical: {issubclass(FreezerTruck, Vihical)}")

        # super(Freezer, self).display() # work because of MRO
        # super(Vihical, self).display() # fails because of MRO
        
        # If we want to inherit multiple classes, we have to independently call them
        Freezer.display(self)
        Vihical.display(self)


ft = FreezerTruck()
ft.drive(100)
ft.freeze(-35)
print("_" * 20)
ft.display()


# Pet Shop Application
# Mini-inventory system

class PetShop:
    pets = {}

    def __init__(self):
        self.load()
    
    def add(self, key, quantity):
        qty = 0
        if key in self.pets:
            val = self.pets[key]
            qty = val + quantity
        else:
            qty = quantity
        self.pets[key] = qty
        print(f"Added {quantity} {key} : total = {self.pets[key]}")
    
    def remove(self, key, quantity):
        qty = 0
        if key in self.pets:
            val = self.pets[key]
            qty = val - quantity
        if qty < 0:
            qty = 0
        self.pets[key] = qty
        print(f"Removed {quantity} {key} : total = {self.pets[key]}")
    
    def display(self):
        for k, v in self.pets.items():
            print(f"{k} = {v}")
    
    def save(self):
        print("saving.... pets")
        with open("petshop/animals.txt", "w") as f:
            json.dump(self.pets, f)
        print("saved!")
    
    def load(self):
        print("Loading.... pets")
        if not os.path.exists("petshop/animals.txt"):
            print("Skipping... failed to load")
            return
        with open("petshop/animals.txt", "r") as f:
            self.pets = json.load(f)
        print("Loaded!")

def main():
    petshop = PetShop()
    while True:
        action = input("Actions: add, remove, save, list, exit: ")
        if action == "exit":
            break
        if action == "list":
            petshop.display()
        if action == "save":
            petshop.save()
        if action == "remove":
            key = str(input("Enter name of animal to remove: "))
            qty = int(input("Enter number of animal to remove: "))
            petshop.remove(key, qty)
        if action == "add":
            key = str(input("Enter name of animal to add: "))
            qty = int(input("Enter number of animal to add: "))
            petshop.add(key, qty)
    petshop.save()

if __name__ == "__main__":
    main()

