#!/usr/bin/env python3

"""
Tim Meese
Au2018-Py210B
Circle Tests
"""

import pytest
from circle import Circle
from sphere import Sphere
from math import pi

test_radius_int = 4
test_radius = float(4)
test_diameter = test_radius * float(2)
test_circum = float(2.0) * pi * test_radius
test_area = pi * (test_radius ** 2)
test_sphere_area = float(4.0) * pi * (test_radius ** 2)
test_sphere_volume = (float(4.0) / float(3.0)) * pi * (test_radius ** 3)


def test_circle_init_methods():
    c = Circle(test_radius_int)
    assert(c.radius == test_radius)
    assert(c.diameter == test_diameter)
    assert(c.circumference == test_circum)
    assert(c.area == test_area)
    # Test diameter property setter
    c.diameter = test_diameter * float(2.0)
    assert(c.radius == test_radius * float(2.0))
    assert(c.diameter == test_diameter * float(2.0))
    assert(c.circumference == test_circum * float(2.0))
    assert(c.area == test_area * float(4.0))


def test_sphere_init_methods():
    s = Sphere(test_radius_int)
    assert(s.radius == test_radius)
    assert(s.diameter == test_diameter)
    assert(s.circumference == test_circum)
    assert(s.area == test_sphere_area)
    assert(s.volume == test_sphere_volume)
    # Test diameter property setter
    s.diameter = test_diameter * float(2.0)
    assert(s.radius == test_radius * float(2.0))
    assert(s.diameter == test_diameter * float(2.0))
    assert(s.circumference == test_circum * float(2.0))
    assert(s.area == test_sphere_area * float(4.0))
    assert(s.volume == test_sphere_volume * float(8.0))


def test_circle_alt_constructor():
    c2 = Circle.from_diameter(test_diameter)
    assert(c2.radius == test_radius)
    assert(c2.diameter == test_diameter)
    assert(c2.circumference == test_circum)
    assert(c2.area == test_area)


def test_sphere_alt_constructor():
    s = Sphere.from_diameter(test_diameter)
    assert(s.radius == test_radius)
    assert(s.diameter == test_diameter)
    assert(s.circumference == test_circum)
    assert(s.area == test_sphere_area)
    assert(s.volume == test_sphere_volume)


def test_circle_logical_ops():
    c = Circle(test_radius_int)
    c2 = Circle(test_radius_int * 2)
    c3 = c + c2
    assert(c2 > c)
    assert(c3.radius == float(12.0))


def test_sphere_logical_ops():
    s = Sphere(test_radius_int)
    s2 = Sphere(test_radius_int * 2)
    s3 = s + s2
    assert(s2 > s)
    assert(s3.radius == float(12.0))
