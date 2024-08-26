#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x elements of a list"""
    number_of_elements = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            number_of_elements += 1
    except IndexError:
        pass
    finally:
        print()
    return number_of_elements
