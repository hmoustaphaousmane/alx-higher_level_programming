#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""
    new_list = [replace if el == search else el for el in my_list]
    return new_list
