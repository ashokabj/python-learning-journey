class Animal:
    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

d = Dog()

d.sound()

print("\n===============\n")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, branch):
        super().__init__(name, age)
        self.branch = branch

student = Student("Ashoka", 19, "AI & DS")

print(student.name)
print(student.age)
print(student.branch)
print("\n===============\n")

