#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer with "{:d}".format()."""
    try:
        value = int(value)
        print("{:d}".format(value), end="\n")
        return True
    except Exception:
        return False
