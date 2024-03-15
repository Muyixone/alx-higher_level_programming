#!/usr/bin/python3

def print_last_digit(number):
    str_val = str(number)
    str_val = str_val[-1]
    str_val = int(str_val)
    print("{}".format(str_val), end='')
    return str_val
