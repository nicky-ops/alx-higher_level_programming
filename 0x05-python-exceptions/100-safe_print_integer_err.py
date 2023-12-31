#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        if int(value):
            print("{:d}".format(value))
            return True
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return False
