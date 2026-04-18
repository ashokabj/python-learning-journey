name=input("Enter your name : ")
age=int(input("Enter your age : "))
movie=input("Enter movie name : ")

if age <= 5:
    price = 0
    catagory = "Free (Under 5)"
elif age <= 12:
    price =100
    catagory = "Child"
elif age <= 60:
    price = 250
    catagory = "Adult"
else:
    price = 150
    catagory = "Senior citizen"

print("============ TICKET BOOKING ============")
print(f"NAME : {name}")
print(f"MOVIE NAME : {movie}")
print(f"CATAGORY : {catagory}")
print(f"TICKET PRICE : Rs {price}")
print("=========================================")