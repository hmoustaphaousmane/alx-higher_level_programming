#!/usr/bin/python3
def roman_to_int(roman_string):
    """Return a roman numeral converted to integer"""
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    int_value = 0

    for i in range(len(roman_string)):
        if roman_string[i] in roman_numerals:
            current_roman_numeral = roman_numerals[roman_string[i]]
            if (
                i + 1 < len(roman_string) and
                current_roman_numeral < roman_numerals[roman_string[i + 1]]
            ):
                int_value -= current_roman_numeral
            else:
                int_value += current_roman_numeral
        else:
            return 0
    return int_value
