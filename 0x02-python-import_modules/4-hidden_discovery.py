#!/usr/bin/python3
import sys, hidden_4
if __name__ == "__main__":
    item = dir(hidden_4)
    for i in item:
        if not i.startswith("__"):
            print(i)
