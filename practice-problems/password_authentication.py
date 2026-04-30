#Passeord vallidator

password = "python123"
attempts = 0

while attempts < 3:
    guess = input("Enter password: ")
    attempts += 1
    if guess == password:
        print("Access granted!")
        break
    else:
        print(f"Wrong! {3-attempts} attempts remaining.")
else:
    print("Account locked! Too many failed attempts.")