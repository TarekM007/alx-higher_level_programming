#!/usr/bin/python3
"""
class student
"""


class Student:
    """attributes of the class student"""
    def __init__(self, first_name, last_name, age):
        """initializes the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        method that retrieves a dictionary
        """
        return self.__dict__
