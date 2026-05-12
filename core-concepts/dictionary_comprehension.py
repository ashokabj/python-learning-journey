# Dictionary Comprehension Basics

# 1. Basic dictionary comprehension
numbers = [1, 2, 3, 4, 5]

squares = {num: num ** 2 for num in numbers}
print("Squares:", squares)

print()

# 2. With condition
even_squares = {num: num ** 2 for num in numbers if num % 2 == 0}
print("Even Squares:", even_squares)

print()

# 3. String length mapping
words = ["python", "java", "javascript"]

word_lengths = {word: len(word) for word in words}
print("Word Lengths:", word_lengths)

print()

# 4. Temperature conversion
celsius = [0, 20, 30, 40]

fahrenheit = {
    temp: (temp * 9/5) + 32
    for temp in celsius
}

print("Temperature Conversion:", fahrenheit)

print()

# 5. Existing dictionary transformation
prices = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1500
}

discount_prices = {
    item: price * 0.9
    for item, price in prices.items()
}

print("Discounted Prices:", discount_prices)