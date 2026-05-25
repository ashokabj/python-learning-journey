# Function without parameters
def greet():
    print("Hello, welcome to Python Functions")


greet()


# Function with parameters
def introduce(name, role):
    print(f"My name is {name} and I am a {role}")


introduce("Ashoka", "Python Learner")


# Function with return value
def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)
print(f"Addition Result: {result}")


# Function with default parameter
def greet_user(name="Guest"):
    print(f"Welcome, {name}")


greet_user()
greet_user("Rahul")


# Function returning multiple values
def calculate_marks(total_marks, subjects):
    average = total_marks / subjects
    return total_marks, average


total, avg = calculate_marks(450, 5)

print(f"Total Marks: {total}")
print(f"Average Marks: {avg}")


# Function using loop
def print_numbers(limit):
    for number in range(1, limit + 1):
        print(number)


print_numbers(5)


# Function using conditional statements
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_even_odd(7))