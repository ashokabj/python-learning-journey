# Student Marks Analysis using List Comprehension

marks = [78, 92, 45, 67, 88, 34, 90]

# Passed students (>= 50)
passed = [m for m in marks if m >= 50]

# Failed students
failed = [m for m in marks if m < 50]

# Grades
grades = ["A" if m >= 85 else "B" if m >= 70 else "C" if m >= 50 else "F" for m in marks]

# Bonus marks (+5)
updated_marks = [m + 5 for m in marks]

print("Original marks:", marks)
print("Passed:", passed)
print("Failed:", failed)
print("Grades:", grades)
print("Updated marks (+5):", updated_marks)