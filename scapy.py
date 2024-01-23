#!/usr/bin/env python3
# Script Name:                  Scapy library
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      01/22/2024
# Purpose:                      Create a TCP Port Range Scanner that tests whether a TCP port is open or closed.
# Source:                       chatgpt

# Import necessary modules from Scapy library
from scapy.all import IP, Ether, TCP, sr1, send, print, 
import random 
import sys

# Define host IP
host = "scanme.nmap.org"


# Define port range or specific set of ports to scan
prt_range = [21,22,25,80,433]

# define function for scanning ports
def port_scan(dst_port):
    src_port = random.randiant(1024, 65535)
    response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags="s"), timeout=1, verboe=1)
 
 
    if response.haslayer(TCP) and response[TCP].flags == 0x12:
            # Flag 0x12 received (SYN-ACK), send a RST packet to close the connection
            send(IP(dst=host) / TCP(sport=src_port, dport=dst_port, flags="R"), verbose=0)
            print(f"Port {dst_port} is open")
    elif response.haslayer(TCP) and response[TCP].flags == 0x14:
            # Flag 0x14 received (RST-ACK), port is closed
            print(f"Port {dst_port} is closed")
    else:
            # No flag received, port is filtered and silently dropped
            print(f"Port {dst_port} is filtered and silently dropped")
   
# print(f"Port {dst_port} is filtered and silently dropped")

# Loop through the port range and perform the scan
for port in prt_range:
    port_scan(port)