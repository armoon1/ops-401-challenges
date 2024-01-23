#!/usr/bin/env python3
# Script Name:                  Scapy library
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      01/22/2024
# Purpose:                      Create a TCP Port Range Scanner that tests whether a TCP port is open or closed.
# Source:                       chatgpt

# Import necessary modules from Scapy library
from scapy.all import *

# Function to perform TCP port scanning
def tcp_port_scanner(target_ip, port_range):
    # Iterate through the specified port range
    for port in range(port_range[0], port_range[1] + 1):
        # Craft a TCP SYN packet for the specified port
        packet = IP(dst=target_ip) / TCP(dport=port, flags="S")

        # Send the packet and receive the response
        response = sr1(packet, timeout=1, verbose=0)

        # Check if a response was received
        if response is not None:
            # Check TCP flags in the response
            if response.haslayer(TCP):
                flags = response[TCP].flags

                # Open port (SYN-ACK received)
                if flags == 0x12:
                    print(f"Port {port} is open")
                    
                    # Send a RST packet to gracefully close the open connection
                    rst_packet = IP(dst=target_ip) / TCP(dport=port, flags="R")
                    send(rst_packet, verbose=0)
                    
                # Closed port (RST-ACK received)
                elif flags == 0x14:
                    print(f"Port {port} is closed")
                    
                # Filtered port (No response received)
                else:
                    print(f"Port {port} is filtered (silently dropped)")

# Main execution when the script is run
if __name__ == "__main__":
    # Replace 'your_target_ip' and 'your_port_range' with your actual target IP and port range
    target_ip = 'your_target_ip'
    port_range = (1, 100)  # Example port range
    
    # Call the function to perform TCP port scanning
    tcp_port_scanner(target_ip, port_range)
