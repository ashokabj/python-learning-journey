# student_marks_analysis.py

marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92
}

print("Student marks:", marks)

# Total students
print("Total students:", len(marks))

# Average marks
total = sum(marks.values())
average = total / len(marks)
print("Average marks:", average)

# Highest & lowest
highest = max(marks, key=marks.get)
lowest = min(marks, key=marks.get)

print("Top scorer:", highest, "-", marks[highest])
print("Lowest scorer:", lowest, "-", marks[lowest])

# Check student
name = "Bob"
if name in marks:
    print(name, "scored", marks[name])
else:
    print(name, "not found")