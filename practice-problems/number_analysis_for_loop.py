# Number Analysis using For Loop

numbers = []

n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    value = int(input(f"Enter number {i+1}: "))
    numbers.append(value)

even_count = 0
odd_count = 0
total = 0

for num in numbers:
    total += num
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
average = total / n

print(f"Numbers: {numbers}")
print(f"Total: {total}")
print(f"Average: {average}")
print(f"Even count: {even_count}")
print(f"Odd count: {odd_count}")