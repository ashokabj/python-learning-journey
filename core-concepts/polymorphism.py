"""
Polymorphism

Concepts covered:
1. Polymorphism
2. Method overriding
3. Runtime polymorphism
4. Duck typimg
"""

class Animal:
    # Parent class

    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    # Child class

    # Method overriding
    def sound(self):
        print("Dog barks.")

class Cat(Animal):
    # Child class

    # Method overriding
    def sound(self):
        print("Cat meows.")

class Robot:
    # Unrelated class
    
    # Duck typing
    def sound(self):
        print("Robot says: Hello Human!")

# Runtime polymorphism using Duck Typing
def make_sound(obj):
    obj.sound()

# Different objects responding differently
objects = [Dog(), Cat(), Robot()]

for obj in objects:
    make_sound(obj)