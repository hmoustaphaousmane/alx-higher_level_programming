#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv[1:]
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = args[1]
    if operator not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(args[0])
        b = int(args[2])
        if operator == "+":
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
        elif operator == "-":
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        elif operator == "*":
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
        elif operator == "/":
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
