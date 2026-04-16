print("============ MENU ============")
print("1. PIZZA   -  199")
print("2. BURGER  -  119")
print("3. PASTA   -  129")
print("==============================")

customer=input("Enter your name: ").strip().title()
item=input("Enter item name : ").strip().lower()
qty=int(input("Enter quantity : "))

if item == "pizza":
    price = 199
elif item == "burger":
    price = 119
elif item == "pasta":
    price = 129
else:
    price = 0

if price == 0:
    print(f"{item} is not on the menu!")
else:
    subtotal = price * qty
    gst = subtotal * 0.05
    total = subtotal + gst

    print("\n============ BILL ============")
    print(f"Customer : {customer}")
    print(f"Item : {item.title()}")
    print(f"Quantity : {qty} * Rs {price}")
    print(f"Subtotal : Rs {subtotal}")
    print(f"GST (5%): Rs {gst:.2f}")
    print(f"Total : Rs {total:.2f}")
    print("==============================")