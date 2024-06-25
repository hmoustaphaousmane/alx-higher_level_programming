#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer with "{:d}".format()."""
    if isinstance(value, int):
        print("{:d}".format(value), end='\n')
        return True
    return False
