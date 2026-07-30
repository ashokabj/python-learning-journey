# Encapsulation

class BankAccount:
    def __init__(self):
        self.__balance = 50000   # Private attribute

    def show_balance(self):
        return self.__balance

account = BankAccount()
print(account.show_balance())

print("===============")
class Laptop:
    def __init__(self, brand):
        self.__brand = brand  #self._Laptop__brand = brand

    def show_brand(self):
        return self.__brand

laptop = Laptop("HP")
print(laptop.show_brand())

# print(laptop.__brand) # Raises AttributeError because __brand is private
