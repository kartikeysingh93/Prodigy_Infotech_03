import random
import re

def generate_password(length=8):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_password_strength(password):
    score = 0
    length = len(password)

    # Criteria for scoring
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special_char = bool(re.search(r'[!@#$%^&*()-_=+]', password))

    # Increment score based on criteria
    score += 2 if has_lowercase else 0
    score += 2 if has_uppercase else 0
    score += 2 if has_digit else 0
    score += 2 if has_special_char else 0

    # Additional considerations
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1

    # Translate score into strength category
    if score >= 8:
        return "Very Strong"
    elif score >= 6:
        return "Strong"
    elif score >= 4:
        return "Moderate"
    else:
        return "Weak"

def additive_cipher_encrypt(password, key):
    encrypted_password = ''.join(chr((ord(char) + key) % 128) for char in password)
    return encrypted_password

def additive_cipher_decrypt(encrypted_password, key):
    decrypted_password = ''.join(chr((ord(char) - key) % 128) for char in encrypted_password)
    return decrypted_password

def multiplicative_cipher_encrypt(password, key):
    encrypted_password = ''.join(chr((ord(char) * key) % 128) for char in password)
    return encrypted_password

def multiplicative_cipher_decrypt(encrypted_password, key):
    modinv_result = modinv(key, 128)
    if modinv_result is not None:
        decrypted_password = ''.join(chr((ord(char) * modinv_result) % 128) for char in encrypted_password)
        return decrypted_password
    else:
        print("Error: Modular inverse does not exist for the given key.")
        return None

def modinv(a, m):
    # Modular multiplicative inverse
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def menu():
    print("\nWelcome to the Password Management Tool!")
    while True:
        print("\nChoose an option:")
        print("1. Password Strength Checker")
        print("2. Password Encryption")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            password_strength_menu()
        elif choice == '2':
            password_encryption_menu()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def password_strength_menu():
    while True:
        print("\nPassword Strength Checker:")
        print("1. Generate a Password")
        print("2. Check Password Strength")
        print("3. Go back to main menu")

        sub_choice = input("Enter your choice (1, 2, or 3): ")

        if sub_choice == '1':
            length = int(input("Enter the password length: "))
            password = generate_password(length)
            print("Generated Password:", password)
        elif sub_choice == '2':
            password = input("Enter the password to check strength: ")
            strength = check_password_strength(password)
            print("Password Strength:", strength)
        elif sub_choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def password_encryption_menu():
    while True:
        print("\nPassword Encryption:")
        print("1. Additive Cipher")
        print("2. Multiplicative Cipher")
        print("3. Go back to main menu")

        cipher_choice = input("Enter your choice (1, 2, or 3): ")

        if cipher_choice == '1':
            additive_cipher_menu()
        elif cipher_choice == '2':
            multiplicative_cipher_menu()
        elif cipher_choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def additive_cipher_menu():
    while True:
        print("\nAdditive Cipher:")
        print("1. Encrypt the Password")
        print("2. Decrypt the Password")
        print("3. Go back to encryption menu")

        enc_dec_choice = input("Enter your choice (1, 2, or 3): ")

        if enc_dec_choice == '1':
            password = input("Enter the password to encrypt: ")
            key = int(input("Enter the additive cipher key: "))
            encrypted_password = additive_cipher_encrypt(password, key)
            print("Encrypted Password:", encrypted_password)
        elif enc_dec_choice == '2':
            encrypted_password = input("Enter the encrypted password to decrypt: ")
            key = int(input("Enter the additive cipher key: "))
            decrypted_password = additive_cipher_decrypt(encrypted_password, key)
            print("Decrypted Password:", decrypted_password)
        elif enc_dec_choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def multiplicative_cipher_menu():
    while True:
        print("\nMultiplicative Cipher:")
        print("1. Encrypt the Password")
        print("2. Decrypt the Password")
        print("3. Go back to encryption menu")

        enc_dec_choice = input("Enter your choice (1, 2, or 3): ")

        if enc_dec_choice == '1':
            password = input("Enter the password to encrypt: ")
            key = int(input("Enter the multiplicative cipher key: "))
            encrypted_password = multiplicative_cipher_encrypt(password, key)
            print("Encrypted Password:", encrypted_password)
        elif enc_dec_choice == '2':
            encrypted_password = input("Enter the encrypted password to decrypt: ")
            key = int(input("Enter the multiplicative cipher key: "))
            decrypted_password = multiplicative_cipher_decrypt(encrypted_password, key)
            if decrypted_password is not None:
                print("Decrypted Password:", decrypted_password)
        elif enc_dec_choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    menu()
