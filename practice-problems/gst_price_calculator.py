prices = {
    "Laptop": 50000,
    "Mouse": 1000,
    "Keyboard": 2000
}

prices_with_gst = {
    item: round(price * 1.18, 2)
    for item, price in prices.items()
}

print(f"\nPrices with 18% GST: {prices_with_gst}")