#!/usr/bin/env python3

"""
Tim Meese
Au2018-Py210B
Circle Lab
"""

from circle import Circle
from math import pi


class Sphere(Circle):
    _volume = float(0.0)

    def __init__(self, radius):
        super().__init__(radius)
        self._volume = (float(4.0) / float(3.0)) * pi * (self._radius ** 3)
        self._area = float(4.0) * pi * (self._radius ** 2)

    @classmethod
    def from_diameter(self, dia):
        radius = dia // 2
        return Sphere(radius)

    def __str__(self):
        return "Sphere with radius [{0:6.2f}]".format(self._radius)

    def __repl__(self):
        return "Sphere({0:d})".format(int(self._radius))

#
# Properties
#

    @property
    def diameter(self):
        print("in diameter getter")
        return self._diameter

    @diameter.setter
    def diameter(self, dia):
        print("in Sphere diameter setter (overload)")
        radius_in = dia // 2
        self.__init__(radius_in)

    @property
    def volume(self):
        print("in Sphere volume getter")
        return self._volume
