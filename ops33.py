#!/usr/bin/env python3
# Script Name:                  Signature-based Malware Detection Part 3 of 3
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      02/21/2024
# Purpose:                      Signature-based Malware Detection
# Source:                       chatgpt

import os
import hashlib
import datetime
import requests

VIRUSTOTAL_API_KEY = "YOUR_VIRUSTOTAL_API_KEY_HERE"  # Replace this with your VirusTotal API key

def get_file_info(file_path):
    # Get file size
    file_size = os.path.getsize(file_path)

    # Get last modified timestamp
    modified_time = os.path.getmtime(file_path)
    modified_time_str = datetime.datetime.fromtimestamp(modified_time).strftime('%Y-%m-%d %H:%M:%S')

    # Calculate MD5 hash
    with open(file_path, "rb") as f:
        md5_hash = hashlib.md5()
        while chunk := f.read(4096):
            md5_hash.update(chunk)
        md5_digest = md5_hash.hexdigest()

    return {
        "file_name": os.path.basename(file_path),
        "file_size": file_size,
        "modified_time": modified_time_str,
        "md5_hash": md5_digest,
        "file_path": file_path
    }

def search_file(file_name, directory):
    file_count = 0
    hit_count = 0
    
    # Iterate over all files in the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_count += 1
            if file == file_name:
                hit_count += 1
                file_path = os.path.join(root, file)
                file_info = get_file_info(file_path)
                print("Timestamp:", file_info["modified_time"])
                print("File Name:", file_info["file_name"])
                print("File Size:", file_info["file_size"], "bytes")
                print("MD5 Hash:", file_info["md5_hash"])
                print("File Path:", file_info["file_path"])
                print()

                # Check the file hash against VirusTotal
                check_virustotal(file_info["md5_hash"])

    print("\nSearch complete.")
    print("Total files searched:", file_count)
    print("Total hits found:", hit_count)

def check_virustotal(md5_hash):
    url = f"https://www.virustotal.com/api/v3/files/{md5_hash}"
    headers = {
        "x-apikey": VIRUSTOTAL_API_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if "data" in data:
            positives = data["data"]["attributes"]["last_analysis_stats"]["malicious"]
            total = data["data"]["attributes"]["last_analysis_stats"]["total"]
            print("VirusTotal Detection Results:")
            print("Positives Detected:", positives)
            print("Total Files Scanned:", total)
        else:
            print("No results found on VirusTotal for this file hash.")
    else:
        print("Error occurred while querying VirusTotal API:", response.status_code)

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
