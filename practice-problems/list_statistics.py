marks = [78, 92, 85, 60, 89]
average = sum(marks) / len(marks)
print(f"Highest marks: {max(marks)}")
print(f"Lowest marks: {min(marks)}")
print(f"Average marks: {sum(marks)/len(marks):.2f}")
print(f"Sorted marks: {sorted(marks)}")

if average >= 75:
    print("Performance: Good")
else:
    print("Performance: Needs improvements")