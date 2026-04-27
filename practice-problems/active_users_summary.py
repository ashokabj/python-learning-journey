users = {
    "user1": {"name": "A", "active": True},
    "user2": {"name": "B", "active": False},
    "user3": {"name": "C", "active": True}
}

count = 0

# Check user1
if users["user1"]["active"]:
    print(users["user1"]["name"])
    count += 1

# Check user2
if users["user2"]["active"]:
    print(users["user2"]["name"])
    count += 1

# Check user3
if users["user3"]["active"]:
    print(users["user3"]["name"])
    count += 1

print(f"Active users count: {count}")