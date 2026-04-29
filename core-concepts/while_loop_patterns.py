# while_loop_patterns.py

# 1. Basic while loop
i = 1
while i <= 5:
    print("Count:", i)
    i += 1

print("-----")

# 2. While with condition
password = "admin"
user_input = ""

while user_input != password:
    user_input = input("Enter password: ")

print("Access granted")

print("-----")

# 3. Infinite loop with break
while True:
    n = int(input("Enter a number (0 to exit): "))
    if n == 0:
        print("Exiting loop")
        break
    print("You entered:", n)

print("-----")

# 4. Continue usage
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print("Value:", i)

print("-----")

# 5. While with counter logic
total = 0
count = 1

while count <= 5:
    total += count
    count += 1

print("Sum of first 5 numbers:", total)