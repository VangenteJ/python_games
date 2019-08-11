import collections
import math
import os
from turtle import Turtle

def path(filename):
    filepath = os.path.realpath(__file__)
    dirpath = os.path.dirname(filepath)
    fullpath = os.path.join(dirpath, filename)
    return fullpath

def line(a,b,x,y):
    turtle = Turtle()
    turtle.up()
    turtle.goto(a,b)
    turtle.down()
    turtle.goto(x,y)

class Vector(collections.Sequence):
    PRECISION = 6
    __slot__ = ('_x','_y','_hash')

    def __init__(self, x, y):
        self._hash = None
        self._x = round(x, self.PRECISION)
        self._y = round(y, self.PRECISION)
    
    @property
    #Getter
    def x(self):
        return self._x

    #Setter
    @x.setter
    def x(self, value):
        if self._hash is not None:
            raise ValueError("Cannot set value after hashing")
        self._x = round(value, self.PRECISION)

    @property
    #Getter
    def y(self):
        return self._y

    #Setter
    @y.setter
    def y(self, value):
        if self._hash is not None:
            raise ValueError("Cannot set value after hashing")
        self._y = round(value, self.PRECISION)
    
    def __hash__(self):
        # v = vector(1,2)
        # v.__hash__() -> hash(v)
        if self._hash is None:
            pair = (self.x, self.y)
            self._hash = hash(pair)
        return self._hash

    def __len__(self):
        return 2

    def __getitem__(self, index):
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        else:
            raise IndexError
    
    def copy(self):
        type_self = type(self)
        return type_self(self.x, self.y)

    def __eq__(self, other):
        # v = vector(1, 2)
        # v.__eq__(w) is true if (v = vector(1, 2)) = (w = vector(1, 2)) and false if otherwise
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y 
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Vector):
            return self.x != other.x and self.y != other.y 
        return NotImplemented
    
    def __iadd__(self, other):
        # v = vector(1, 2)
        # v.__iadd__(w) => v += w
        if self._hash is not None:
            ValueError("Cannot assign value after hashing")
        
        elif isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other
        
        return self

    def __add__(self, other):
        # v = vector(1, 2)
        # v.__add__(w) => v + w
        
        copy = self.copy()
        return copy.__iadd__(other)

    __radd__ = __add__

    def move(self, other):
        # Move vector by other (n place)
        # v = vector(1, 2)   w = vector(3, 2)   v.move(w) => vector(4, 4)
        return self.__iadd__(other)

    def __isub__(self, other):
        # v = vector(1, 2)
        # v.__isub__(w) => v -= w
        if self._hash is not None:
            ValueError("Cannot assign value after hashing")
        
        elif isinstance(other, Vector):
            self.x -= other.x
            self.y -= other.y
        else:
            self.x -= other
            self.y -= other
        
        return self

    def __sub__(self, other):
        # v = vector(1, 2)
        # v.__sub__(w) => v - w
        
        copy = self.copy()
        return copy.__isub__(other)

    def __imul__(self, other):
        # v = vector(1, 2)
        # v.__imul__(w) => v *= w
        if self._hash is not None:
            ValueError("Cannot assign value after hashing")
        
        if isinstance(other, Vector):
            self.x *= other.x
            self.y *= other.y
        else:
            self.x *= other
            self.y *= other
        
        return self

    def __mul__(self, other):
        # v = vector(1, 2)
        # v.__mul__(w) => v * w
        
        copy = self.copy()
        return copy.__imul__(other)

    __rmul__ = __mul__

    def scale(self, other):
        self.__imul__(other)

    def __itruediv__(self, other):
        # v = vector(1, 2)
        # v.__itruediv__(w) => v /= w
        if self._hash is not None:
            ValueError("Cannot assign value after hashing")
        
        if isinstance(other, Vector):
            self.x /= other.x
            self.y /= other.y
        else:
            self.x /= other
            self.y /= other
        
        return self

    def __truediv__(self, other):
        # v = vector(1, 2)
        # v.__truediv__(w) => v / w
        
        copy = self.copy()
        return copy.__itruediv__(other)
    
    def __neg__(self):
        # v = vector(1, 2)
        # v.__neg__()  => vector(-1, -2)
        copy = self.copy()
        copy.x = -copy.x
        copy.y = -copy.y
        return copy

    def __abs__(self):
        # v = vector(3, 4)  => 5
        # sqrt(x**2 + y**2)
        return (self.x**2 + self.y**2)**0.5

    def rotate(self, angle):
        if self._hash is not None:
            raise ValueError("Cannot rotate after hashing")
        radians = angle * math.pi / 180.0
        cosine = math.cos(radians)
        sine = math.sin(radians)

        x = self.x
        y = self.y

        self.x = x * cosine - y * sine
        self.y = x * cosine + y * sine

    def __repr__(self):

        self_type = type(self)
        name = self_type.__name__
        return "{} ({!r}, {!r})".format(name, self.x, self.y)
