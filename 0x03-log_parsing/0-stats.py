#!/usr/bin/python3
"""log parsing"""

import sys
import signal
from collections import defaultdict

# Define signal handler function for CTRL+C
def signal_handler(signal, frame):
    print_metrics()
    sys.exit(0)

# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Define variables for metrics
total_file_size = 0
status_code_count = defaultdict(int)

# Define function to print metrics
def print_metrics():
    print("Total file size: {}".format(total_file_size))
    for status_code in sorted(status_code_count.keys()):
        print("{}: {}".format(status_code, status_code_count[status_code]))

# Read lines from stdin
for i, line in enumerate(sys.stdin):
    # Parse the line
    try:
        parts = line.split()
        file_size = int(parts[8])
        status_code = int(parts[7])
    except:
        continue

    # Update metrics
    total_file_size += file_size
    status_code_count[status_code] += 1

    # Print metrics every 10 lines
    if i > 0 and i % 10 == 0:
        print_metrics()