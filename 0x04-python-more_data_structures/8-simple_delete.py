#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):

    for i in a_dictionary.copy():
        if key in a_dictionary:
            del (a_dictionary[key])
        else:
            continue

    return a_dictionary
