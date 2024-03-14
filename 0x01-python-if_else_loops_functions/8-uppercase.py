#!/usr/bin/python3

def uppercase(str):
    new_string = ''
    for char in str:
        if ord(char) >= 97:
            new_string += chr(ord(char) - 32)
        else:
            new_string += chr(ord(char))

    print("{}".format(new_string))
