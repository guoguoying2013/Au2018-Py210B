#!/usr/bin/env python3

"""
Class to implement simple sphere

"""

from circle import *


class Sphere(Circle):
    """
    Sphere class with volume property
    sublcass of circle

    """

    @property
    def volume(self):
        return round(4 / 3 * pi * self.radius ** 3, 6)

    def __str__(self):
        return "Sphere with radius: {}".format(self.radius)

    def __repr__(self):
        return "Sphere({})".format(self.radius)

    @property
    def area(self):
        raise NotImplementedError
