#!/usr/bin/env python3
# Script Name:                  
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      02/14/2024 *Happy Valentine's day*
# Purpose:                      Event Logging Tool Part 3 of 3
# Source:                       chatgpt

import logging  # Import the logging module

# Configure logging with a basic configuration
logging.basicConfig(level=logging.DEBUG)

# Create a FileHandler instance to handle logging to a file named 'app.log'
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)  # Set the logging level for the file handler

# Create a StreamHandler instance to handle logging to the terminal
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Set the logging level for the stream handler

# Create a formatter to specify the format of the log messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set the formatter for the file handler and stream handler
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Get the logger for the current module (__name__) and add the file handler to it
logger = logging.getLogger(__name__)
logger.addHandler(file_handler)

# Add the stream handler to the logger as well
logger.addHandler(stream_handler)

# Log some messages with different logging levels
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

