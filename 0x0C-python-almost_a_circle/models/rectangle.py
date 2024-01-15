#!/usr/bin/python3
""" a module"""


from models.base import Base


class Rectangle(Base):
    """ Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initiation method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        def get_width(self):
            """width of this triangle"""
            return self.__width

        def set_width(self, value):
            self.__width = value

        def get_height(self):
            """height of this triangle"""
            return self.__height

        def set_height(self, value):
            self.__height = value

        def get_x(self):
            """x of this triangle"""
            return self.__x

        def set_x(self, value):
            self.__x = value

        def get_y(self):
            """y of this triangle"""
            return self.__y

        def set_y(self, value):
            self.__y = value
