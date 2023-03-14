#!/usr/bin/python3
"""determines if a given data set represents a valid UTF-8 encoding"""
def validUTF8(data):
    """data"""
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    for byte in data:
        # Check if this is the start of a new UTF-8 character
        if num_bytes == 0:
            # Count the number of bytes in this UTF-8 character
            if byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            elif byte >> 7 != 0:
                # This is an invalid start byte
                return False
        else:
            # This byte should start with the 0b10 prefix
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    # All bytes have been consumed, so the UTF-8 encoding is valid if we have
    # processed all the bytes of a multi-byte character
    return num_bytes == 0