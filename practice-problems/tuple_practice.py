# tuple_practice.py

marks = (85, 90, 78, 92, 88)

print("Marks:", marks)

# Total and average
total = sum(marks)
average = total / len(marks)

print("Total:", total)
print("Average:", average)

# Highest and lowest
print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))

# Count a value
print("How many times 90 appears:", marks.count(90))