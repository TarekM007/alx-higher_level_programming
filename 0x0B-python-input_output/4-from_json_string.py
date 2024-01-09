#!/usr/bin/python3
"""
a function that returns an object from JSON
"""

import json


def from_json_string(my_str):
    """
 returns object from JSON
    """
    return json.loads(my_str)
