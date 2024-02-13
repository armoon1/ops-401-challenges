#!/usr/bin/env python3
# Script Name:                  
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      02/12/2024
# Purpose:                      Event Logging Tool Part 1 of 3
# Source:                       chatgpt


# Add logging capabilities to your Python tool using the logging library.
import logging
import os

# basic config for the log
logging.basicConfig(filename="lab26.log", format='%(asctime)s %(message)s', filemode='w')

# Experiment with log types. Build in some error handling, then induce some errors. Send log data to a file in the local directory.
# Confirm your logging feature is working as expected.
log = logging.getLogger()

# setting error level
log.setLevel(logging.WARNING)

# some log messages
log.debug("debug")
log.info("info")
log.warning("warning")