# List creation
numbers = [1, 2, 3, 4]

# Access
print(numbers[0])
print(numbers[-1])

# Modify
numbers[1] = 10

# Add
numbers.append(5)
numbers.insert(1, 7)

# Remove
numbers.remove(3)
numbers.pop()

# Length
print(len(numbers))


# List comprehension 
squares = [x**2 for x in numbers]
print(squares)

# Sorting
numbers.sort()
print(numbers)
