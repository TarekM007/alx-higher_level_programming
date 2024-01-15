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
        def get_width(self):
            """width of this triangle"""
            return self.__width

        @get_width.setter
        def set_width(self, value):
            self.__width = value

        @property
        def get_height(self):
            """height of this triangle"""
            return self.__height

        @get_height.setter
        def set_height(self, value):
            self.__height = value

        @property
        def get_x(self):
            """x of this triangle"""
            return self.__x

        @get_x.setter
        def set_x(self, value):
            self.__x = value

        @property
        def get_y(self):
            """y of this triangle"""
            return self.__y

        @get_y.setter
        def set_y(self, value):
            self.__y = value
