#!/usr/bin/env python3

"""
Class to implement simple Circle

"""

from math import pi


class Circle:
    """
    Circle class with area and diameter properties
    numberic protocols added

    """

    def __init__(self, init_radius=0):
        """ Constructor using radius """

        self.radius = init_radius

    @classmethod
    def from_diameter(cls, init_diameter=0):
        """ Contructor using diameter """

        radius = init_diameter / 2
        return cls(radius)

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return round(pi * self.radius ** 2, 6)

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        return type(self)(self.radius + other.radius)

    def __iadd__(self, other):
        self.radius += other.radius
        return self

    def __mul__(self, value):
        return type(self)(self.radius * value)

    def __rmul__(self, value):
        return type(self)(self.radius * value)

    def __imul__(self, value):
        self.radius *= value
        return self

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ne__(self, other):
        return self.radius != other.radius
