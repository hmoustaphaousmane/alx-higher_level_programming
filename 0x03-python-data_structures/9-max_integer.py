#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return
    max = 0
    for value in my_list:
        if value > max:
            max = value
    return max
