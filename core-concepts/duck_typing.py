class Dog:
    def sound(self):
        print("Dog barks.")

class Cat:
    def sound(self):
        print("Cat meows.")

class Robot:
    def sound(self):
        print("Robot speaking.")

def make_sound(obj):
    obj.sound()

make_sound(Dog())
make_sound(Cat())
make_sound(Robot())