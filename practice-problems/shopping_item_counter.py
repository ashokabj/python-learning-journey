items = input("Enter your shopping items: ")

item_list = items.split()

item_quantities = {
    item: item_list.count(item)
    for item in item_list
}

print(f"Item quantities: {item_quantities}")