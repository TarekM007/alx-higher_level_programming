#!/usr/bin/python3
"""
The lookup function container
"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: initial object
        a_class: a class type
        Returns: True or False
    """
    return type(obj) is a_class
