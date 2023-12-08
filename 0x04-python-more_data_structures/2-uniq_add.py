#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set()
    for element in my_list:
        if isinstance(element, int):
            new_set.add(element)
    sum_list = sum(new_set)

    return sum_list
