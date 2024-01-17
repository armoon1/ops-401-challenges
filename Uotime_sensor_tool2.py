
# Script Name:                  Uptime sensor Part 2
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      01/10/2024
# Purpose:                      Useing ICMP packets to evaluate if hosts on the LAN are up or down

# Import necessary libraries
import subprocess
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# Function to check the status of a host by sending a ping
def check_host_status(destination_ip):
    try:
        # Run the ping command
        subprocess.check_output(['ping', '-c', '1', destination_ip])

        # If the command runs successfully, consider it a success
        return True
    except subprocess.CalledProcessError:
        # If the command fails, consider it a failure
        return False

# Function to send email notifications
def send_notification_email(sender_email, sender_password, recipient_email, subject, body):
    # Set up the email server
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Create the email message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # Send the email
    server.sendmail(sender_email, recipient_email, msg.as_string())

    # Close the server connection
    server.quit()

# Main function
def main():
    destination_ip = "8.8.8.8"
    previous_status = None

    # Get user input for email and password
    sender_email = input("Enter your email address: ")
    sender_password = input("Enter your email password: ")
    recipient_email = input("Enter the recipient's email address: ")

    while True:
        # Get the current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

        # Check the status of the host
        is_host_up = check_host_status(destination_ip)

        # Notify if status changes
        if previous_status is not None and previous_status != is_host_up:
            previous_status_str = "up" if previous_status else "down"
            current_status_str = "up" if is_host_up else "down"

            # Email notification
            subject = f"Host Status Change Notification - {destination_ip}"
            body = (
                f"Host status for {destination_ip} has changed from {previous_status_str} to {current_status_str} at {timestamp}."
            )
            send_notification_email(sender_email, sender_password, recipient_email, subject, body)

        # Print the result with timestamp and destination IP
        if is_host_up:
            print(f"{timestamp} Network Active to {destination_ip}")
        else:
            print(f"{timestamp} Network Inactive to {destination_ip}")

        # Update previous_status for the next iteration
        previous_status = is_host_up

        # Wait for 2 seconds before the next iteration
        time.sleep(2)

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
