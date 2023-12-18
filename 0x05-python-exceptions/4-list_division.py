#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                val_1 = my_list_1[i]
                val_2 = my_list_2[i]

                valid_type_1 = isinstance(val_1, (int, float))
                valid_type_2 = isinstance(val_2, (int, float))

                if not valid_type_1 or not valid_type_2:
                    raise TypeError("wrong type")

                if val_2 == 0:
                    raise ZeroDivisionError("division by 0")

                division = val_1 / val_2
                result.append(division)
            except IndexError:
                print("out of range")
                result.append(0)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
            except TypeError:
                print("wrong type")
                result.append(0)
    finally:
        return result
