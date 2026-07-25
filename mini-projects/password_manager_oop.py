class PasswordManager:
    def __init__(self, master_password):
        self.master_password = master_password
        self.passwords = []

    def add_password(self, password):
        if len(password) >= 8:
            digit_found = False
            for char in password:
                if char.isdigit():
                    digit_found = True
                    break
            if not digit_found:
                return "Password must contain atleast one digit."
            if password not in self.passwords:
                self.passwords.append(password)
                return "Password Added successfully."
            else:
                return "Password already exists."

        else:
            return "Password must be atleast 8 characters long."
        
    def remove_password(self, password):
        if password in self.passwords:
            self.passwords.remove(password)
            return "Password removed successfully."
        else:
            return "Password not exist."
        
    def show_passwords(self):
        if not self.passwords:
            return "No passwords saved."
        
        else:
            return self.passwords
        
    def total_passwords(self):
        return len(self.passwords)
    
    def check_strength(self, password):
        if len(password) >= 8:
            has_upper = False
            has_lower = False
            has_digit = False

            for char in password:
                if char.isupper():
                    has_upper = True
                elif char.islower():
                    has_lower = True
                elif char.isdigit():
                    has_digit = True
            if len(password) >= 8 and has_upper and has_lower and has_digit:
                return "Strong password"
            else:
                return "Weak password"
                
manager = PasswordManager("Ashoka@123")

print(manager.add_password("Python123"))
print(manager.add_password("Github2026"))
print(manager.add_password("Python123"))
print(manager.add_password("Learning100"))

print("\nSaved passwords")
print("-------------")
print(manager.show_passwords())

print("\nStrength Check")
print("-------------")
print(manager.check_strength("Python123"))

print("\nRemove password")
print("-------------")
print(manager.remove_password("Github2026"))

print("\nTotal passwords:",manager.total_passwords())
