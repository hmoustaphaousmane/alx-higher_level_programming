#!/usr/bin/python3
def remove_char_at(str, n):
    """
    Create a copy of the string, removing the character at the position n
    (not the Python way, the “C array index”).
    """
    chars = list(str)
    if n < len(chars) and n > 0:
        chars.pop(n)
    new_str = "".join(chars)

    return new_str
