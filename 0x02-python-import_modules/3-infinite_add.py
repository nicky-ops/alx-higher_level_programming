#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 0:
        print("{}".format(0))
    else:
        sum = 0
        for i in range(len(sys.argv)):
            i += 1
            if i < len(sys.argv):
                sum += int(sys.argv[i])
        print(sum)
