regestered = ("Alice", "Bob", "Charlie", "David")
attended = ["Bob", "Charlie", "Eve", "Frank", "Bob"]
regestered_set = set(regestered)
attended_set = set(attended)

print(f"People who regestered and attended: {regestered_set & attended_set}")
print(f"People who regestered but did not attended: {regestered_set - attended_set}")
print(f"People who attended without registering: {attended_set - regestered_set}")
print(f"All unique participants: {regestered_set | attended_set}")