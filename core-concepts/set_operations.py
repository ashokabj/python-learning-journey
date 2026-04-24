# Set operations

A = {1, 2, 3, 4}
B = {3, 4, 5, 6, 7}

print(f"Set A: {A}")
print(f"Set B: {B}")

#Add and remove
A.add(8)
A.remove(1)
print(f"After add/remove(A): {A}")

# Union
print(f"Union: {A | B}")

# Intersection
print(f"Intersection: {A & B}")

# Difference
print(f"Difference(A-B): {A-B}")
print(f"Difference(B-A): {B-A}")

# Symmetric difference (Elements that are in A or B, but NOT in both)
print(f"Symmetric difference: {A ^ B}")

# Membership
print(f"Is 3 in A?: {3 in A}")