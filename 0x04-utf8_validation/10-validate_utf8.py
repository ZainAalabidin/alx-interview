#!/usr/bin/env python3
'''module for utf-8 validation'''


def validUTF8(data):
    ''' method that determines if a given data set represents
    a valid UTF-8 encoding.
    '''
    num_bytes = 0

    mask_1_byte = 0b10000000
    mask_2_byte = 0b11100000
    mask_3_byte = 0b11110000
    mask_continuation = 0b11000000

    num_bytes = 0
    for byte in data:
        byte = byte & 0xff
        if num_bytes == 0:
            if byte & mask_1_byte == 0:
                continue
            elif byte & mask_2_byte == 0b11000000:
                num_bytes = 1
            elif byte & mask_2_byte == 0b11100000:
                num_bytes = 2
            elif byte & mask_3_byte == 0b11110000:
                num_bytes = 3
            else:
                return False
        else:
            if byte & mask_continuation != 0b10000000:
                return False

            num_bytes -= num_bytes
    return num_bytes == 0
