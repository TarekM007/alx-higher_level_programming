#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv)-1
    if argc == 0:
        print("{:d} {:s}.".format(argc, "arguments"))
    elif argc == 1:
        print("{:d} {:s}:".format(argc, "argument"))
    else:
        print("{:d} {:s}:".format(argc, "arguments"))
    for i in range(0, len(argv)):
        if i > 0:
            print("{:d}: {:s}".format(i, argv[i]))
