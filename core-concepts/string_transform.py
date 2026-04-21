s=input("Enter the string: ")
if not s:
    print("You entered the empty string.")
else:
    s=s.replace(" ","").lower().replace("a","@")
    print(f"Final result : {s}")
