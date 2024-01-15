#!/usr/bin/python3
""" a module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initiation method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns string info about this square.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """method that assigns an argument to each attribute"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """method that updates attributes"""
        if args:
            self.__update(*args)
        if kwargs:
            self.__update(**kwargs)
