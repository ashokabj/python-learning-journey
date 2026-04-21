string=input("Enter the string: ")
if len(string)==0:
    print("You entered the Empty string.")
else:
    print(string)
    print(f"Length: {len(string)}")
    print(f"First character: {string[0]}")
    print(f"Last character: {string[-1]}")
