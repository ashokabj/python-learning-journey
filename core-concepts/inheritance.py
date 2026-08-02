# Inheritance

class Person:
    """Parent class"""

    def __init__(self, name, age):
        # Parent constructor
        self.name = name
        self.age = age

    def introduce(self):
        # Parent mothod
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def work(self):
        # This method will be overridden
        print("Person is working.")


class Student(Person):
    """Child class"""

    def __init__(self, name, age, branch):
        # Calling parent constructor
        super().__init__(name, age)

        # Child-speciific attribute
        self.branch = branch

    # Method overriding
    def work(self):
        # super().work() : It executes parent class method
        print(f"{self.name} is studying {self.branch}")

    # Child specific method
    def show_branch(self):
        print(f"Branch: {self.branch}")

# Creatinng object of self class
student = Student("Ashoka", 19, "AI & DS")

print("----- Parent method -----")
student.introduce()

print("----- Child class method -----")
student.show_branch()

print("----- Method overriding -----")
student.work()