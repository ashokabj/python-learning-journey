expenses = []

print("===== Expense Tracker =====")

while True:

    amount = input("Enter expense amount (or type 'done'): ")

    if amount == "done":
        break

    expenses.append(float(amount))

total = sum(expenses)

print("\nYour Expenses:")
for money in expenses:
    print(money)

print("\nTotal Expense:", total)

if total > 5000:
    print("You spent a lot this month ")

else:
    print("Good budget control ")

