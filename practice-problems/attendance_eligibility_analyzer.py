# Attendance Eligibility Mapping

attendance = {
    "Alex": 92,
    "Joseph": 68,
    "Alice": 81,
    "John": 55,
    "Bob": 77
}

eligibility = {
    student: "Eligible" if percentage >= 75 else "Not Eligible"
    for student, percentage in attendance.items()
}

print("\nAttendance Eligibility Report")
print("-" * 35)

for student, status in eligibility.items():
    print(f"{student} ({attendance[student]}%) --> {status}")