#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("Type exception")
    except TypeError as te:
        raise te
