# List Comprehension Basics

# 1. Basic syntax
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print("Squared:", squared)

print()

# 2. With condition
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)

print()

# 3. With if-else
labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print("Labels:", labels)

print()

# 4. From strings
word = "python"
upper_letters = [ch.upper() for ch in word]
print("Uppercase letters:", upper_letters)

print()

# 5. Nested loops
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print("Pairs:", pairs)

print()

# 6. Flattening a list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print("Flattened list:", flat)

print()

# 7. Filtering strings
names = ["Ashok", "Anil", "Bala", "Arjun"]
filtered = [name for name in names if name.startswith("A")]
print("Names starting with A:", filtered)