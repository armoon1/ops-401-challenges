# Script Name:                  Uptime sensor Part 1
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      01/09/2024
# Purpose:                      Useing ICMP packets to evaluate if hosts on the LAN are up or down


# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
# Evaluate the response as either success or failure.
# Assign success or failure to a status variable.
# For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
# Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8

import subprocess  # Import the subprocess module for running shell commands
import time  # Import the time module for handling time-related functionality
from datetime import datetime  # Import datetime module for working with dates and times

def ping_host(host):
    try:
        # Use subprocess to run the ping command with a single packet (-c 1)
        subprocess.check_output(["ping", "-c", "1", host])
        # This module allows you to spawn processes, connect to their input/output/error pipes, 
        # and obtain their return codes.
        # If the ping is successful, return True
        return True
    except subprocess.CalledProcessError:
        # If the ping fails, return False
        return False

def main():
    target_ip = "127.0.0.1"  # Specify the target IP address to monitor (my loopback IP)

    while True:
        # Get the current timestamp in a specific format (as example)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-5] # [:-5] removing last 5 microsecond

        # Check the status of the network by pinging the target IP
        status = "Active" if ping_host(target_ip) else "Inactive"

        # Print the timestamp, network status, and target IP
        print(f"{timestamp} Network {status} to {target_ip}")

        # Pause the loop for 5 seconds before the next iteration
        time.sleep(5)

if __name__ == "__main__":
    main()
