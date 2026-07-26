from abc import ABC, abstractmethod

# Abstraction
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass


# Inheritance
class Car(Vehicle):
    def __init__(self, brand, speed):
        self.brand = brand
        self.__speed = speed # Encapsulation


    # Encapsulation
    def set_speed(self, speed):
        if speed >= 0:
            self.__speed = speed

    def get_speed(self):
        return self.__speed

    # Polimorphism
    def start(self):
        return f"{self.brand} car starts with a key."


class ElectricCar(Vehicle):
    def __init__(self, brand, speed):
        self.brand = brand
        self.__speed = speed

    def start(self):
        return f"{self.brand} electric car starts silently."

car = Car("Tayota", 120)
electric_car = ElectricCar("Tesla", 150)

print("==== Four Pillers of OOP ====")
print(car.start())
print(electric_car.start())

print(f"\nCurrent Speed: {car.get_speed()} km/h")
car.set_speed(140)
print(f"Updated speed: {car.get_speed()} km/h")

