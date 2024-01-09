#!/usr/bin/python3
"""
a function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
writes a string with utf-8
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
