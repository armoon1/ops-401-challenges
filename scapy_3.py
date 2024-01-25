#!/usr/bin/env python3
# Script Name:                  Scapy library
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      01/24/2024
# Purpose:                      Network Security Tool with Scapy
# Source:                       chatgpt

# Import necessary modules from Scapy library
from scapy.all import IP, TCP, ICMP, sr1, send

import random
from ipaddress import ip_network

# Define host IP
host = "scanme.nmap.org"

# Define port range or specific set of ports to scan
prt_range = [21, 22, 25, 80, 443]  # Corrected port number for HTTPS

# Define function for scanning ports
def port_scan(dst_port):
    src_port = random.randint(1024, 65535)  # Corrected typo in randint
    response = sr1(IP(dst=host) / TCP(sport=src_port, dport=dst_port, flags="S"), timeout=1, verbose=0)

    if response and response.haslayer(TCP) and response[TCP].flags == 0x12:
        # Flag 0x12 received (SYN-ACK), send a RST packet to close the connection
        send(IP(dst=host) / TCP(sport=src_port, dport=dst_port, flags="R"), verbose=0)
        print(f"Port {dst_port} is open")
    elif response and response.haslayer(TCP) and response[TCP].flags == 0x14:
        # Flag 0x14 received (RST-ACK), port is closed
        print(f"Port {dst_port} is closed")
    else:
        # No flag received, port is filtered and silently dropped
        print(f"Port {dst_port} is filtered and silently dropped")

# Prompt the user for an IP address to target
target_ip = input("Enter the target IP address: ")

# Check if the host is responsive to ICMP echo requests
response = sr1(IP(dst=target_ip) / ICMP(), timeout=1, verbose=0)

if response and response.haslayer(ICMP):
    icmp_type = response[ICMP].type
    icmp_code = response[ICMP].code

    if icmp_type == 0 and icmp_code == 0:
        # ICMP Echo Reply received, call the port scan function
        print(f"Host {target_ip} is responsive to ICMP")
        for port in prt_range:
            port_scan(port)
    elif icmp_type == 3 and icmp_code in [1, 2, 3, 9, 10, 13]:
        print(f"Host {target_ip} is actively blocking ICMP traffic")
    else:
        print(f"Host {target_ip} is unresponsive to ICMP")
else:
    print(f"Host {target_ip} is down or unresponsive")
