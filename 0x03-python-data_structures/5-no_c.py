#!/bin/usr/python3
def no_c(my_string):
    """Function that removes all characters c and C from a string"""
    new_string = ""
    for character in my_string:
        if character != "c" and character != "C":
            new_string += character
    return new_string
