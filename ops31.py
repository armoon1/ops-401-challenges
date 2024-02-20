#!/usr/bin/env python3
# Script Name:                  Signature-based Malware Detection Part 1 of 3
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      02/19/2024
# Purpose:                      Signature-based Malware Detection
# Source:                       chatgpt

import os

def search_file(file_name, directory):
    file_count = 0
    hit_count = 0
    
    # Iterate over all files in the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_count += 1
            if file == file_name:
                hit_count += 1
                print("Found:", file_name, "at", os.path.join(root, file))
    
    print("\nSearch complete.")
    print("Total files searched:", file_count)
    print("Total hits found:", hit_count)

def main():
    # Prompt user for file name and directory
    file_name = input("Enter the file name to search for: ")
    directory = input("Enter the directory to search in: ")

    # Check if directory exists
    if not os.path.isdir(directory):
        print("Error: The specified directory does not exist.")
        return

    # Call the search function
    search_file(file_name, directory)

if __name__ == "__main__":
    main()
