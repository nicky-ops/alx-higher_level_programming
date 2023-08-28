#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(int(x)):
        try:
            print("{}".format(my_list[i]), end="")
        except TypeError:
            print('Enter a valid integer')
