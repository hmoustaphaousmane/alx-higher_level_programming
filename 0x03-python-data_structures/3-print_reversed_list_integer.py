#!/bin/usr/python3
def print_reversed_list_integer(my_list=[]):
    """function that prints all integers of a list, in reverse order"""
    for i in range(1, len(my_list) + 1):
        print("{}".format(my_list[-i]))
