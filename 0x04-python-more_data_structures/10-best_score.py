#!/usr/bin/python3
def best_score(a_dictionary):
    """Return a key with the biggest integer value."""
    best_score_key = None
    best_score_value = 0
    if a_dictionary is None:
        return best_score_key
    for key, value in a_dictionary.items():
        if value > best_score_value:
            best_score_key = key
            best_score_value = value
    return best_score_key
