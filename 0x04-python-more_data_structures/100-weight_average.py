#!/usr/bin/python3
def weight_average(my_list=[]):
    """Return the weighted average of all integers tuple (<score>, <weight>)"""

    if my_list == []:
        return 0

    numerator, denominator = 0, 0

    for tuple in my_list:
        numerator += tuple[0] * tuple[1]
        denominator += tuple[1]

    if denominator != 0:
        return numerator / denominator
