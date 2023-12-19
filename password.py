import json
import os
import hashlib
import getpass
import random
import string

class PasswordManager:
    def __init__(self, master_password, data_file="passwords.json"):
        self.master_password = master_password.encode()
        self.data_file = data_file
        self.passwords = self.load_passwords()

    def load_passwords(self):
        try:
            with open(self.data_file, 'r') as file:
                encrypted_data = file.read()

            decrypted_data = self.decrypt(encrypted_data)
            passwords = json.loads(decrypted_data)
            return passwords
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_passwords(self):
        encrypted_data = self.encrypt(json.dumps(self.passwords))
        with open(self.data_file, 'w') as file:
            file.write(encrypted_data)

    def encrypt(self, data):
        return hashlib.sha256(data.encode()).hexdigest()

    def decrypt(self, data):
        return data  # In a more secure implementation, you would need proper decryption

    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def add_password(self, category, username, password):
        if category not in self.passwords:
            self.passwords[category] = {}
        self.passwords[category][username] = password
        self.save_passwords()

    def get_password(self, category, username):
        if category in self.passwords and username in self.passwords[category]:
            return self.passwords[category][username]
        else:
            return None

# Example usage:
master_password = getpass.getpass("Enter your master password: ")
password_manager = PasswordManager(master_password)

while True:
    print("\nPassword Manager Menu:")
    print("1. Add Password")
    print("2. Retrieve Password")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        category = input("Enter category: ")
        username = input("Enter username: ")
        password = password_manager.generate_password()
        password_manager.add_password(category, username, password)
        print("Password added successfully!")
    elif choice == "2":
        category = input("Enter category: ")
        username = input("Enter username: ")
        retrieved_password = password_manager.get_password(category, username)
        if retrieved_password:
            print("Retrieved Password:", retrieved_password)
        else:
            print("Password not found.")
    elif choice == "3":
        print("Exiting Password Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
