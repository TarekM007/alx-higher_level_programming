#!/usr/bin/python3
"""
The lookup function container
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: initial object
        a_class: a class type
        Returns: True or False
    """
    return isinstance(obj, type) and issubclass(type(obj), a_class)
