import os
import hashlib
import random
import string

def generate_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=25))
    return password

def encrypt_password(password):
    encrypted_password = hashlib.sha256(password.encode()).hexdigest()
    return encrypted_password

def write_to_file(username, password, encrypted_password, purpose):
    filename = f"your_passwords/{username}_{purpose}.txt"
    with open(filename, 'w') as f:
        f.write(f"username={username}\n")
        f.write(f"purpose={purpose}\n")
        f.write(f"password_generated={password}\n")
        f.write(f"password_encrypted={encrypted_password}\n")

if not os.path.exists("your_passwords"):
    os.makedirs("your_passwords")

while True:
    username = input("Enter your username: ")
    purpose = input("Enter the purpose for password generation (e.g. linkedin, facebook, instagram): ")
    filename = f"your_passwords/{username}_{purpose}.txt"
    if os.path.exists(filename):
        print(f"Username '{username}' for purpose '{purpose}' already exists. Please choose another.")
    else:
        break

password = generate_password()
print(f"Generated password: {password}")

while True:
    choice = input("Do you like the generated password? (y/n)")
    if choice.lower() == "y":
        encrypted_password = encrypt_password(password)
        write_to_file(username, password, encrypted_password, purpose)
        print("Password Generated Successfully!")
        break
    elif choice.lower() == "n":
        password = generate_password()
        print(f"Generated password: {password}")
    else:
        print("Invalid choice. Please enter 'y' for yes or 'n' for no.")
