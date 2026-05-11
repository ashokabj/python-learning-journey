usernames = ["  ashoka ", "RAHUL", " anu", "KIRAN  ", "python"]

cleaned_usernames = [
    username.strip().lower()
    for username in usernames
]

print(f"\nCleaned usernames: {cleaned_usernames}")