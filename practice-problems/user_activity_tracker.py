user_logins = {
    "Alice": 15,
    "Bob": 2,
    "Charlie": 9,
    "Alex": 0,
    "rose": 20
}

activity_status = {
    user: "Active" if logins >= 5 else "Inactive"
    for user, logins in user_logins.items()
}

print("\nUser activity status:")
print(activity_status)