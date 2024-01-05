#!/bin/usr/python3
def new_in_list(my_list, idx, element):
    """
    Function that replaces an element in a list at a specific position without
    modifying the original list (like in C).
    """
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
