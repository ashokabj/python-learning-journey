registered = {"Anil", "Rahul", "Anu", "Kiran", "David"}
attended = {"Rahul", "Anu", "David", "John"}
valid_participants = registered & attended

print(f"Attended without registering: {attended - registered}")

print(f"Registered but absent: {registered - attended}")

print(f"Total unique participants: {registered | attended}")

print(f"Count of valid participants: {len(valid_participants)}")

print("\nVerified participants:")
for participant in valid_participants:
    print(participant)