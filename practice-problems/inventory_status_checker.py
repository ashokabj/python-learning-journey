stock = {
     "laptop": 5, 
     "mouse": 0, 
     "keyboard": 3, 
     "monitor": 0 
} 
for item, quantity in stock.items():
    if quantity: 
        print(f"{item} --> In stock") 
    else: 
        print(f"{item} --> Out of stock")