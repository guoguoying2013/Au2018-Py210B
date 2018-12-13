#!/usr/bin/env python3

"""
Tim Meese
Au2018-Py210B
Circle Lab
"""

from math import pi


class Circle():

    def __init__(self, radius):
        self._radius = float(radius)
        self._diameter = float(2.0) * self._radius
        self._area = pi * (self._radius * self._radius)
        self._circumference = float(2.0) * pi * self._radius

    @classmethod
    def from_diameter(self, dia):
        radius_in = dia // 2
        return Circle(radius_in)

    def __str__(self):
        return "Circle with radius [{0:6.2f}]".format(self._radius)

    def __repl__(self):
        return "Circle({0:d})".format(int(self._radius))

    def __add__(self, other):
        return Circle(self._radius + other.radius)

    def __mul__(self, other):
        return Circle(self._radius * float(other))

    def __eq__(self, other):
        return self._radius == other.radius

    def __lt__(self, other):
        return self._radius < other.radius

#
# Properties
#

    @property
    def radius(self):
        print("in radius getter")
        return self._radius

    @property
    def diameter(self):
        print("in diameter getter")
        return self._diameter

    @diameter.setter
    def diameter(self, dia):
        print("in diameter setter")
        radius_in = dia // 2
        self.__init__(radius_in)

    @property
    def area(self):
        print("in area getter")
        return self._area

    @property
    def circumference(self):
        print("in circumference getter")
        return self._circumference
