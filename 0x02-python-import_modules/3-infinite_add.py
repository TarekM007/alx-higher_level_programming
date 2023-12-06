#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv) - 1
    sum = 0
    if argc == 0:
        print("{:d}".format(argc))
    else:
        for i in range(0, len(argv)):
            if i > 0:
                sum = sum + int(argv[i])
        print("{:d}".format(sum))
