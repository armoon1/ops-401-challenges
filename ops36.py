#!/usr/bin/env python3
# Script Name:                  Web Application Fingerprinting
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      02/26/2024
# Purpose:                      Web Application Fingerprinting
# Source:                       chatgpt

import subprocess  # Import the subprocess module to execute shell commands

def banner_grabbing_nc(target, port):
    try:
        # Execute Netcat command to perform banner grabbing
        result = subprocess.check_output(['nc', '-v', '-n', '-z', '-w', '1', target, str(port)],
                                         stderr=subprocess.STDOUT, universal_newlines=True)
        print("Banner grabbing result using Netcat:")
        print(result)  # Print the result of Netcat banner grabbing
    except subprocess.CalledProcessError as e:
        print("Error executing Netcat command:", e.output)  # Print error if Netcat command fails

def banner_grabbing_telnet(target, port):
    try:
        # Execute Telnet command to perform banner grabbing
        result = subprocess.check_output(['telnet', target, str(port)],
                                         stderr=subprocess.STDOUT, universal_newlines=True)
        print("Banner grabbing result using Telnet:")
        print(result)  # Print the result of Telnet banner grabbing
    except subprocess.CalledProcessError as e:
        print("Error executing Telnet command:", e.output)  # Print error if Telnet command fails

def banner_grabbing_nmap(target):
    try:
        # Execute Nmap command to perform banner grabbing
        result = subprocess.check_output(['nmap', '-p', '-', '--script=banner', target],
                                         stderr=subprocess.STDOUT, universal_newlines=True)
        print("Banner grabbing result using Nmap:")
        print(result)  # Print the result of Nmap banner grabbing
    except subprocess.CalledProcessError as e:
        print("Error executing Nmap command:", e.output)  # Print error if Nmap command fails

def main():
    target = input("Enter the target URL or IP address: ")  # Prompt user to enter target URL or IP address
    port = int(input("Enter the target port number: "))  # Prompt user to enter target port number

    # Perform banner grabbing using Netcat, Telnet, and Nmap
    banner_grabbing_nc(target, port)
    banner_grabbing_telnet(target, port)
    banner_grabbing_nmap(target)

if __name__ == "__main__":
    main()  # Call the main function when the script is executed
