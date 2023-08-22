#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = sys.argv[1]
        b = sys.argv[3]
        operators = ['+', "-", "*", "/"]
        if sys.argv[2] not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        elif sys.argv[2] == "+":
            print("{} + {} = {}".format(a, b, add(int(a), int(b))))
        elif sys.argv[2] == '-':
            print("{} - {} = {}".format(a, b, sub(int(a), int(b))))
        elif sys.argv[2] == '*':
            print("{} * {} = {}".format(a, b, mul(int(a), int(b))))

        elif sys.argv[2] == '/':
            print("{} / {} = {}".format(a, b, div(int(a), int(b))))
