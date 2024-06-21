#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Return a set of all elements present in only one set."""
    return set_1.union(set_2).difference(set_1.intersection(set_2))
