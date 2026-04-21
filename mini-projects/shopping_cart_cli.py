cart = []
prices = []

name = input("Enter your name: ").strip().title()

item1 = input("Enter item 1: ").strip().title()
price1 = float(input(f"Enter price of {item1}: ₹"))
cart.append(item1)       # append - add to list
prices.append(price1)

item2 = input("Enter item 2: ").strip().title()
price2 = float(input(f"Enter price of {item2}: ₹"))
cart.append(item2)
prices.append(price2)

item3 = input("Enter item 3: ").strip().title()
price3 = float(input(f"Enter price of {item3}: ₹"))
cart.append(item3)
prices.append(price3)

# List operations
total = sum(prices)                  # sum()
item_count = len(cart)               # len()
costliest = max(prices)              # max()
cheapest = min(prices)               # min()

# Comparison + logical
if total >= 1000:
    discount = total * 0.10
    offer = "10% Discount Applied "
elif total >= 500:
    discount = total * 0.05
    offer = "5% Discount Applied"
else:
    discount = 0
    offer = "No Discount"

final = total - discount

print(f"\n======  SHOPPING CART ======")
print(f"  Customer  : {name}")
print(f"  Items     : {cart}")
print(f"  Total Items: {item_count}")
print(f"  Costliest : ₹{costliest}")
print(f"  Cheapest  : ₹{cheapest}")
print(f"  Subtotal  : ₹{total:.2f}")
print(f"  Offer     : {offer}")
print(f"  Discount  : ₹{discount:.2f}")
print(f"  Final Bill: ₹{final:.2f}")
print(f"==============================")