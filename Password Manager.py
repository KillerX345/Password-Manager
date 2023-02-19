import secrets
import string
import json
import re
from cryptography.fernet import Fernet


def load_passwords(key):
    try:
        with open("passwords.json", "rb") as f:
            data = f.read()
            fernet = Fernet(key)
            decrypted_data = fernet.decrypt(data)
            passwords = json.loads(decrypted_data)
    except (FileNotFoundError, json.JSONDecodeError):
        passwords = {}
    return passwords


def save_passwords(passwords, key):
    data = json.dumps(passwords).encode()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open("passwords.json", "wb") as f:
        f.write(encrypted_data)


def add_password(passwords):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    check_password_strength(password)  # Check password strength
    passwords[username] = password
    save_passwords(passwords, key)
    print("Password saved.")


def get_password(passwords):
    username = input("Enter your username: ")
    if username in passwords:
        print("Your password is:", passwords[username])
    else:
        print("Username not found.")


def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password


def decrypt_passwords(key):
    try:
        with open("passwords.json", "rb") as f:
            data = f.read()
            fernet = Fernet(key)
            decrypted_data = fernet.decrypt(data)
            passwords = json.loads(decrypted_data)
            with open("decrypted_passwords.json", "w") as f2:
                json.dump(passwords, f2, indent=4)
        print("Passwords decrypted.")
    except (FileNotFoundError, json.JSONDecodeError):
        passwords = {}
    return passwords


def check_password_strength(password):
    # Check the length of the password
    length_error = len(password) < 8
    # Search for digits, upper and lower case letters and punctuation
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    punctuation_error = re.search(r"[ !\"#$%&@'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None

    # Give feedback to the user based on the password strength
    if length_error:
        print("Password is too short. Should be at least 8 characters.")
    if digit_error:
        print("Password should contain at least one digit.")
    if uppercase_error:
        print("Password should contain at least one uppercase letter.")
    if lowercase_error:
        print("Password should contain at least one lowercase letter.")
    if punctuation_error:
        print("Password should contain at least one special character.")
    if not (length_error or digit_error or uppercase_error or lowercase_error or punctuation_error):
        print("Password is strong!")


key = Fernet.generate_key()
passwords = load_passwords(key)

while True:
    print("\nPassword Manager")
    print("1. Add password")
    print("2. Get password")
    print("3. Generate password")
    print("4. Decrypt passwords")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_password(passwords)
    elif choice == "2":
        get_password(passwords)
    elif choice == "3":
        length = int(input("Enter password length: "))
        password = generate_password(length)
        print("Your generated password is:", password)
    elif choice == "4":
        passwords = decrypt_passwords(key)
    elif choice == "5":
        save_passwords(passwords, key)
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
