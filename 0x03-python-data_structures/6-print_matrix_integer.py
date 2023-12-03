#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        space = ""
        for element in row:
            print("{:s}{:d}".format(space, element), end="")
            space = " "
        print()
