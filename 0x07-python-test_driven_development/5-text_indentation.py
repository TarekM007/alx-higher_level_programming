#!/usr/bin/python3
"""a module"""


def text_indentation(text):
    """
    prints a text

    Args:
    text: inital string to work on
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        if char not in ['.', '?', ':']:
            print(char, end='')
        else:
            print(char)
            print()
            print()
