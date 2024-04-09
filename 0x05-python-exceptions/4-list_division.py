#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    items = []
    for val in range(list_length):
        try:
            result = my_list_1[val] / my_list_2[val]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            items.append(result)
    return items
