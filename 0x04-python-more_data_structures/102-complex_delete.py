#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in a dictionary."""
    keys = [key for key in a_dictionary if a_dictionary[key] == value]
    for key in keys:
        a_dictionary.pop(key)
    return a_dictionary
