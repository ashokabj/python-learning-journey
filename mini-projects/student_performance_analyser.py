students = {
    "Ashoka": 85,
    "Rahul": 32,
    "Anu": 91,
    "Kiran": 40
}

top_marks = 0
top_student = ""

total = 0
pass_count = 0
fail_count = 0

print("\nStudent Performance Report")
print("-"*30)

for student, marks in students.items():
    total += marks

    if marks > top_marks:
        top_student = student
        top_marks = marks

    if marks >= 40:
        print(f"{student} --> Pass")
        pass_count += 1
    else:
        print(f"{student} --> Fail")
        fail_count += 1

print(f"Top scorer: {top_student} ({top_marks})")
print(f"Average marks: {total / len(students):.2f}")
print(f"Passed students: {pass_count}")
print(f"Failed students: {fail_count}")