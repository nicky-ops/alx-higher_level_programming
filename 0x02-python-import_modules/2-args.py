#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("{} arguments.".format(0))
    elif len(sys.argv) == 2:
        print("{} argument:".format(1))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv)-1))
        for i in range(len(sys.argv)):
            i += 1
            if i < len(sys.argv):
                print("{}: ".format(i), end="")
                print("{}".format(sys.argv[i]))
