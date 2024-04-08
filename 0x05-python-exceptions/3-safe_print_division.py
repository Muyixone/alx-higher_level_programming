#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except Exception as error:
        result = None
        pass
    else:
        return result
    finally:
        print("Inside result: {}".format(result))
