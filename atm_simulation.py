#smart ATM system

PIN = input("Enter your PIN: ").strip()

if not PIN:
    print("\nPIN required!")
elif PIN != "1234":
    print("\nIncorrect PIN.")
else:
    print("PIN: **")
    print("Login successful!")

    balance = 1000

    print("\nHow can I help you?")
    print("1. Check balance\n2. Deposit\n3. Withdraw\n4. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        print(f"\nCurrent Balance: Rs{balance}")

    elif choice == "2":
        amount = int(input("\nEnter deposit amount: "))
        if amount <= 0:
            print("\nInvalid amount! Try again.")
        else:
            balance += amount
            print(f"\nUpdated balance: Rs{balance}")

    elif choice == "3":
        amount = int(input("\nEnter amount to withdraw: "))
        if amount <= 0:
            print("\nInvalid amount! Try again.")
        elif amount > balance:
            print("\nInsufficient balance!")
        else:
            balance -= amount
            print(f"\nCurrent balance: Rs{balance}")

    elif choice == "4":
        print("\nThank you! Visit again!")

    else:
        print("\nInvalid choice!")


        