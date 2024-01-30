#!/usr/bin/env python3
# Script Name:                  Brute Force
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      01/29/2024
# Purpose:                      Automated Brute Force Wordlist Attack 1
# Source:                       chatgpt

import time

def offensive_mode(word_list_path): # defining offensive mode function
    # Accepts a word list file path and iterates through the word list, printing each word with a delay.
    with open(word_list_path, 'r') as file: # with for closing the function after execution, 'r' read mode
        for word in file:
            word = word.strip()
            print(word)
            time.sleep(1)  # adding delay as needed

def defensive_mode(user_input, word_list_path): # defining defensive mode function
    # Accepts a user input string and a word list file path.
    # Searches the word list for the user input string and prints whether it appeared in the word list.
    with open(word_list_path, 'r') as file:  # with for closing the function after execution, 'r' read mode
        word_list = [line.strip() for line in file] # loop
        if user_input in word_list:   # checking the list if password exists
            print("Password recognized!")
        else:
            print("Password not recognized.")

def main(): # defining execution function
    # Main function to drive the program.
    # Prompts the user to select a mode (Offensive or Defensive) and takes inputs for the mode
    mode = int(input("Select mode (1 for Offensive, 2 for Defensive): ")) # integer input
    if mode == 1: # boolian statement if true or false
        word_list_path = input("Enter word list file path: ")
        offensive_mode(word_list_path) # offensive_mode function print word with 1 sec delay as defined
    elif mode == 2:
        user_input = input("Enter a string to search in the word list: ")
        word_list_path = input("Enter word list file path: ")
        defensive_mode(user_input, word_list_path) # defensive_mode function either prints recognized or not recognized
    else:
        print("Invalid mode selection.") # for other situations to prevent breaking down the codes

if __name__ == "__main__":
    main()
