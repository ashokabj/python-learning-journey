# for loop basics

# 1. interacting over a list
fruits = ["Apple", "Banana", "Cherry", "Watermellon", "Grapes"]
for fruit in fruits:
    print(fruit)
print("----------")

# 2. Using range
for i in range(1, 6):
    print(i)           # 1 to 5
print("----------")

# 3. range(start, stop)
for i in range(2, 7):
    print(i)           #  2 to 6
print("----------")

# 4. range(start, stop, step)
for i in range(1, 10, 2):
    print(i)           # Odd numbers
print("----------")

# 5. loop with condition
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even.")
print("----------")

# 6. break and continue
for i in range(1,6):
    if i == 2:
        continue
    if i == 5:
        break
    print(i)
print("----------")

# 7. enumerate
names = ["A", "B", "C"]
for index, name in enumerate(names):
    print(index,name)