#!/usr/bin/python3
"""
function that writes a string (UTF8), returns the number of characters written:
"""


def write_file(filename="", text=""):
    """
writes a string with utf-8
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return(file.write(text))
