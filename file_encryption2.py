# Script Name:                  File encryption
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      01/17/2024
# Purpose:                      File encryption2

# Import the Fernet class from the cryptography library
from cryptography.fernet import Fernet
import os

# Function to generate a new encryption key using Fernet
def generate_key():
    return Fernet.generate_key()

# Function to load the encryption key from a file named "secret.key"
def load_key():
    return open("secret.key", "rb").read()

# Function to save the encryption key to a file named "secret.key"
def save_key(key):
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Function to encrypt a target file using Fernet encryption
def encrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

# Function to decrypt a target file using Fernet encryption
def decrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

# Function to encrypt a string and print the ciphertext
def encrypt_string(data, key):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    print("Encrypted String:", encrypted_data)

# Function to decrypt a string and print the cleartext
def decrypt_string(data, key):
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(data).decode()
    print("Decrypted String:", decrypted_data)

# Function to recursively encrypt a folder and its contents
def encrypt_folder(folder_path, key):
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            encrypt_file(filepath, key)

# Function to recursively decrypt a folder that was encrypted by this tool
def decrypt_folder(folder_path, key):
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            decrypt_file(filepath, key)

# Main function to drive the script
def main():
    print("Select a mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")
    print("5. Recursively Encrypt a folder")
    print("6. Recursively Decrypt a folder")

    # Read user input for the selected mode
    mode = int(input("Enter the mode (1-6): "))
    
    # Generate or load the encryption key
    key = generate_key()  

    # Check the selected mode and prompt for additional input accordingly
    if mode in [1, 2]:
        filepath = input("Enter the file path: ")
    elif mode in [3, 4]:
        user_input = input("Enter the cleartext string: ")
    elif mode in [5, 6]:
        folder_path = input("Enter the folder path: ")

    # Perform the corresponding action based on the selected mode
    if mode == 1:
        encrypt_file(filepath, key)
        print("File encrypted successfully.")

    elif mode == 2:
        decrypt_file(filepath, key)
        print("File decrypted successfully.")

    elif mode == 3:
        encrypt_string(user_input, key)

    elif mode == 4:
        decrypt_string(user_input, key)

    elif mode == 5:
        encrypt_folder(folder_path, key)
        print("Folder encrypted successfully.")

    elif mode == 6:
        decrypt_folder(folder_path, key)
        print("Folder decrypted successfully.")

# Entry point to execute the main function if the script is run directly
if __name__ == "__main__":
    main()

