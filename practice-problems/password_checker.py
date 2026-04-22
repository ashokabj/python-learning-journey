password=input("Enter the password: ")

has_length=len(password)>=8
has_digit=any(char.isdigit() for char in password)

if has_length and has_digit:
    print("Your password is strong")
else:
    print("Your password is weak")
