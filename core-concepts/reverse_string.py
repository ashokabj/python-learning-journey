string=input("Enter the string: ")
if not string:
    print("You entered the empty string.")
else:
    print(f"Reversed strring: {string[::-1]}")