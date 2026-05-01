#Expense Tracker

total_expense = 0
entries = 0
highest = None
lowest = None

print("\nExpense Tracker | Enter zero to finish\n")

while True:
    expense = float(input("Enter expense: "))
    
    if expense == 0:
        break

    if expense < 0:
        print("Invalid expense! Please enter positive number.")   
        continue

    total_expense += expense
    entries += 1

    if highest is None or expense > highest:
        highest = expense

    if lowest is None or expense < lowest:
        lowest = expense

if entries == 0:
    print("NO expenses entered.")

else:    
    print(f"\nTotal expense= {total_expense}")
    print(f"Total number of entries= {entries}")
    print(f"Highest expense= {highest}")
    print(f"Lowest expense= {lowest}")
