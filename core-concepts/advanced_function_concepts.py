def add(*numbers):                  # veriable length positional argguments (*args)
    return sum(numbers)


numbers = add(10, 20, 20, 50, 100)
print(numbers)



def display(**details):                # Veriable length keyword arguements (**kwargs)
    for key, value in details.items():
        print(f"{key} --> {value}")

display(name="ashok", age=22)




add = lambda a, b : a + b   # Lambda function - used only when there is only one operation/expression is exist
print(add(3, 7))

double = lambda x : 2 * x
print(double(100))


# recrsion - a function calls itself

def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1)

print(factorial(4))


# Nested function

def calculate(a, b):
    def add():
        print(a + b)
    def sub():
        print(a - b)
    def mul():
        print(a * b)

    add()
    sub()
    mul()

calculate(10, 3)