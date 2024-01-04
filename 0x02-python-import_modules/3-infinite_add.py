#!/usr/bin/python3
def infinite_add(args):
    result = 0
    for arg in args:
        result += int(arg)
    return result


if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    print(infinite_add(args))
