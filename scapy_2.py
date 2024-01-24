#!/usr/bin/env python3
# Script Name:                  Scapy library
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      01/23/2024
# Purpose:                      Network security tool
# Source:                       ----

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

# User menu for choosing scan mode
print("Choose scan mode:")
print("1. TCP Port Range Scanner mode")
print("2. ICMP Ping Sweep mode")

scan_mode = input("Enter your choice (1 or 2): ")

# ICMP Ping Sweep mode
if scan_mode == "2":
    network_address = input("Enter network address (CIDR format, e.g., 10.10.0.0/24): ")

    # Create a list of all addresses in the given network
    ip_list = [str(ip) for ip in ip_network(network_address, strict=False).hosts()]

    # Count how many hosts are online
    online_hosts = 0

    for ip in ip_list:
        # Ping all addresses on the given network except for network address and broadcast address
        if not ip_network(network_address, strict=False).network_address == ip and not ip_network(network_address, strict=False).broadcast_address == ip:
            response = sr1(IP(dst=ip) / ICMP(), timeout=1, verbose=0)

            if response and response.haslayer(ICMP):
                icmp_type = response[ICMP].type
                icmp_code = response[ICMP].code

                if icmp_type == 3 and icmp_code in [1, 2, 3, 9, 10, 13]:
                    print(f"Host {ip} is actively blocking ICMP traffic")
                else:
                    print(f"Host {ip} is responding")
                    online_hosts += 1
            else:
                print(f"Host {ip} is down or unresponsive")

    print(f"Number of online hosts: {online_hosts}")

# TCP Port Range Scanner mode
elif scan_mode == "1":
    # Loop through the port range and perform the scan
    for port in prt_range:
        port_scan(port)

else:
    print("Invalid choice. Please enter either 1 or 2.")
