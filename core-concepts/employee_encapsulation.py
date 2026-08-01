class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary   # Private attribute

    def show_salary(self):
        return f"{self.name}'s salary is {self.__salary}"

    def increase_salary(self, amount):
        if amount <= 0:
            return "Inavalid increment amount"
        
        else:
            self.__salary += amount
            return "Salary updated successfully."

    def decrease_salary(self, amount):
        if amount > self.__salary:
            return "Cannot reduce salary below Rs. 0"
        
        elif 0 < amount <= self.__salary:
            self.__salary -= amount
            return "Salary reduced successfully."
        
        elif amount <= 0:
            return "Invalid decrement amount."

emp = Employee("Ashok", 50000)

print(emp.show_salary())

print(emp.increase_salary(5000))
print(emp.show_salary())

print(emp.decrease_salary(10000))
print(emp.show_salary())


