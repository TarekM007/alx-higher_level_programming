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

    @property
    def width(self):
        """width of this triangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """height of this triangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """x of this triangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """y of this triangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
