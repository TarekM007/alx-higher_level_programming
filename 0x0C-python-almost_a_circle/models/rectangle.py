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
        self.validate_int("width", value, False)
        self.__width = value

    @property
    def height(self):
        """height of this triangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_int("height", value, False)
        self.__height = value

    @property
    def x(self):
        """x of this triangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_int("x", value)
        self.__x = value

    @property
    def y(self):
        """y of this triangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_int("y", value)
        self.__y = value

    def validate_int(self, name, value, eq=True):
        """method to validate value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """method to get area"""
        return self.width * self.height

    def display(self):
        """method to display"""
        s = self.y * '\n' + \
            (self.x * ' ' + self.width * '#' + '\n') * self.height
        print(s, end='')

    def __str__(self):
        """method to document"""
        return "[{}] ({}) {}/{} - {}/{}"\
            .format(type(self).__name__, self.id, self.x, self.y,
                    self.width, self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """method that assigns an argument to each attribute"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
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

    def to_dictionary(self):
        '''Returns dictionary representation of this class.'''
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
