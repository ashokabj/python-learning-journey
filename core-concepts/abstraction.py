# Abstraction

from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Abstract base class for all vehicles."""

    @abstractmethod
    def start(self):
        """Every vehicle must implements its own start method."""
        pass

class Car(Vehicle):
    def start(self):
        print("Car engine started.")

class Bike(Vehicle):
    def start(self):
        print("Bike engine started.")

# Creating objects
car = Car()
bike = Bike()

#Calling methods
car.start()
bike.start()
