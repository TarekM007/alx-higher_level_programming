#!/usr/bin/python3
"""
The lookup function container
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: initial object
        a_class: a class type
        Returns: True or False
    """
    return isinstance(obj, a_class)
