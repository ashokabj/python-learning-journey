class Car:
    # Constructor
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # Return formatted car information
    def display_details(self):
        return (f"======= Car details =======\n"
                f"Brand: {self.brand}\n"
                f"Model: {self.model}\n"
                f"Year: {self.year}"
        )

    # Determines whether the car is classic or modern
    def is_classic(self):
        if self.year < 2000:
            return "This is a classic Car.\n"
        
        return "This is a Modern Car."

# Creating car objects
car1 = Car("Tayota", "Supra", 1998)
car2 = Car("BMW", "M4", 2024)

# Displaying car details
print(car1.display_details())
print(car1.is_classic())
print(car2.display_details())
print(car2.is_classic())