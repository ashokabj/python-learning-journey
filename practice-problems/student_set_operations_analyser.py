classA = ["A", "B", "C", "D"]
classB = ["C", "D", "E", "F"]

setA = set(classA)
setB = set(classB)

print(f"Class A students: {setA}")
print(f"Class B students: {setB}")
print(f"Common students: {setA & setB}")
print(f"All students: {setA | setB}")
print(f"Only in class A: {setA - setB}")
print(f"Only in class B: {setB - setA}")

#Removing duplicates
roll_numbers = [10, 20, 28, 10, 37, 28, 77, 77]
unique_rolls = set(roll_numbers)

print(f"Unique roll numbers: {unique_rolls}")