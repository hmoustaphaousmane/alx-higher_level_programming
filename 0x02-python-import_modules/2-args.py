#!/usr/bin/python3
def print_arguments(args):
    number_of_arguments = len(args)
    print("{}".format(number_of_arguments), end="")
    if number_of_arguments == 0:
        print(" arguments.")
    elif number_of_arguments == 1:
        print(" argument:")
        print("{}: {}".format(1, args[0]))
    else:
        print(" arguments:")
        for i, arg in enumerate(args, start=1):
            print("{}: {}".format(i, arg))


if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    print_arguments(args)
