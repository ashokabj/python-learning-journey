# dictionary_operations.py

student = {
    "name": "Ashoka",
    "age": 18,
    "branch": "AI & DS"
}

print("Original dictionary:", student)

# Access
print("Name:", student["name"])
print("Age:", student.get("age"))

# Add / update
student["college"] = "VES"
student["age"] = 19
print("After add/update:", student)

# Remove
student.pop("branch")
print("After removal:", student)

# Keys, values, items
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Check key
print("Is 'name' present?", "name" in student)