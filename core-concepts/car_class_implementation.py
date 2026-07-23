class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        return (f"======= Car details =======\n"
                f"Brand: {self.brand}\n"
                f"Model: {self.model}\n"
                f"Year: {self.year}"
        )
    
    def is_classic(self):
        if self.year < 2000:
            return "This is a classic Car.\n"
        
        return "This is a Modern Car."

car1 = Car("Tayota", "Supra", 1998)
car2 = Car("BMW", "M4", 2024)

print(car1.display_details())
print(car1.is_classic())
print(car2.display_details())
print(car2.is_classic())