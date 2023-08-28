#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                elem_1 = my_list_1[i] if i < len(my_list_1) else 0
                elem_2 = my_list_2[i] if i < len(my_list_2) else 0
                if not isinstance(elem_1, (int, float)) or \
                   not isinstance(elem_2, (int, float)):
                    print("wrong type")
                    result_list.append(0)
                elif elem_2 == 0:
                    print("division by 0")
                    result_list.append(0)
                else:
                    result = elem_1 / elem_2
                    result_list.append(result)
            except IndexError:
                print("out of range")
                result_list.append(0)
    finally:
        return result_list
