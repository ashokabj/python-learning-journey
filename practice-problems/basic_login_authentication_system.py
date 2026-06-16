username=input("Enter your name : ").lower()
password=int(input("Enter the passworrd : "))

if username == "admin" and password == 1234:
    print("Login succesful")
elif username == "admin":
    print("Wrong password")
else:
    print("Invalid username")