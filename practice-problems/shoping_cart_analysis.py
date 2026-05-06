prices = [120, 450, 80, 999, 250]
count = 0
for price in prices:
    if price > 200:
        count += 1

total = sum(prices)
average = total / len(prices)

print(f"Total bill: {total}")
print(f"Highest price: {max(prices)}")
print(f"Lowest price: {min(prices)}")
print(f"Items above Rs. 200: {count}")
print(f"Average price: {average:.2f}")