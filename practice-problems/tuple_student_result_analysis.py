students = (
    ("Anil", 85),
    ("Rahul", 35),
    ("Anu", 91),
    ("kiran", 40)
)
pass_count = 0
fail_count = 0

for name,marks in students:
    if marks >= 40:
        pass_count += 1
        print(f"{name} : {marks} - Pass")
    else:
        fail_count += 1
        print(f"{name} : {marks} - Fail")

print(f"Passed students: {pass_count}")
print(f"Failed students: {fail_count}")