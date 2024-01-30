#!/usr/bin/env python3
# Script Name:                  Brute Force
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      01/20/2024
# Purpose:                      Automated Brute Force Wordlist Attack 1
# Source:                       chatgpt

import time

def offensive_mode(word_list_path):
    # Accepts a word list file path and iterates through the word list, printing each word with a delay.
    with open(word_list_path, 'r') as file:
        for word in file:
            word = word.strip()
            print(word)
            time.sleep(1)  # Adjust delay as needed

def defensive_mode(user_input, word_list_path):
    # Accepts a user input string and a word list file path.
    # Searches the word list for the user input string and prints whether it appeared in the word list.
    with open(word_list_path, 'r') as file:
        word_list = [line.strip() for line in file]
        if user_input in word_list:
            print("Password recognized!")
        else:
            print("Password not recognized.")

def main():
    # Main function to drive the program.
    # Prompts the user to select a mode (Offensive or Defensive) and takes necessary inputs accordingly.
    mode = int(input("Select mode (1 for Offensive, 2 for Defensive): "))
    if mode == 1:
        word_list_path = input("Enter word list file path: ")
        offensive_mode(word_list_path)
    elif mode == 2:
        user_input = input("Enter a string to search in the word list: ")
        word_list_path = input("Enter word list file path: ")
        defensive_mode(user_input, word_list_path)
    else:
        print("Invalid mode selection.")

if __name__ == "__main__":
    main()
