class BankAccount:
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance

    def deposite(self, amount):
        if amount <= 0:
            return "Invalid amount"
        self.balance += amount
        return "Deposite successful"
        
    def withdraw(self, amount):
        if amount >= self.balance:
            return "Insufficient moneny"
        self.balance -= amount
        return "Withdraw successfull"


    def display_balance(self):
        return f"{self.account_holder}'s balance is {self.balance}"

account = BankAccount("Ashok")
print(account.deposite(5000))
print(account.withdraw(1000))
print(account.display_balance())
    