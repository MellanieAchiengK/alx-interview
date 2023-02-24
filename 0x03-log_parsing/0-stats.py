#!/usr/bin/python3
"""log parsing"""
import sys


total_size = 0  # pylint: disable=invalid-name
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    line_count = 0  # pylint: disable=invalid-name
    for line in sys.stdin:
        line_count += 1

        # Parse input and calculate total size
        parts = line.split(' ')
        if len(parts) != 6:
            continue

        status_code = int(parts[5])
        file_size = int(parts[6][:-1])
        total_size += file_size

        # Calculate the number of lines by status code
        if status_code in status_codes:
            status_codes[str(status_code)] += 1

        # Output metrics
        if line_count % 10 == 0:
            print("Total file size:", total_size)
            print("Number of lines by status code:")
            for k in sorted(status_codes.keys()):
                print(f"{k}: {status_codes[k]}")

except KeyboardInterrupt:
    print("Total file size:", total_size)
    print("Number of lines by status code:")
    for k in sorted(status_codes.keys()):
        print(f"{k}: {status_codes[k]}")
