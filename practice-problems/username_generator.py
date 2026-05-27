def generate_username(full_name):
    username = full_name.lower().replace(" ", "_")
    return f"{username}_{len(username)}"

full_name = input("Enter your full name: ") 

result = generate_username(full_name) 

print(result)