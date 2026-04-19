price=float(input("Enter the price : "))

if price>=1000:
    discount = price*0.20
    label = "20%"
elif price>=500:
    discount = price*0.10
    label = "10%"
else:
    discount = 0
    label = "0%"

total = price - discount

print(f"Original : Rs {price:.2f} | Discount : {label} | You pay : Rs {total:.2f}")