# tuple operations

t = (10, 20, 30, 40, 50)

print("Original tuple: ",t)

#Length
print(f"Length: {len(t)}")

#indexing
print(f"First element: {t[0]}")
print(f"Last element: {t[-1]}")

#slicing
print(f"Slice(1:4): {t[1:4]}")

#Count and index
print(f"Count of 30: {t.count(30)}")
print(f"Count of 70: {t.count(70)}")

#tuple unpacking
a, b, c, d, e = t
print(f"Unpacked values: {a, b, c, d, e}")

print("Note: Tuples are immutable (cannot change values)")