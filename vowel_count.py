s=input("Enter the string: ")

if not s:
    print("You entered the empty string.")
else:
  count=sum(s.count(v) for v in "aeiouAEIOU")
  
print(f"count = {count}")
