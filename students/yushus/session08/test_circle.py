#!/usr/bin/env/python3

"""
Yushu Song
Au2018-Py210B
Circle Class Assignment
"""

import pytest
from math import pi
from Circle import *

def test_circle_property():
    c = Circle(4)
    assert c.radius == 4
    assert c.diameter == 4*2

def test_circle_set_diameter():
    c = Circle (4)
    c.diameter = 2
    assert c.radius == 1

def test_circle_set_diameter_failure():
    c = Circle (4)
    with pytest.raises(ValueError):
        c.diameter = -8

def test_circle_area():
    c = Circle (2)
    assert c.area == pi * 4

def test_circle_area_failure():
    c = Circle (2)
    with pytest.raises(AttributeError):
        c.area = 4

def test_circle_from_diameter():
    c = Circle.from_diameter(8)
    assert int(c.diameter) == 8

def test_circle_add():
    assert repr(Circle(3)+Circle(3)) == repr(Circle(6))

def test_circle_add_failure():
    with pytest.raises(TypeError):
        Circle(2) + 5

def test_circle_mul():
    assert repr(Circle(2) * 3) == repr(Circle(6))

def test_circle_rmul():
    assert repr(3 * Circle(2)) == repr(Circle(6))

def test_circle_lt():
    assert Circle(1) < Circle(2)

def test_circle_le():
    assert Circle(2) <= Circle(2)

def test_circle_eq():
    assert Circle(1) == Circle(1)

def test_circle_ne():
    assert Circle(1) != Circle(2)

def test_circle_gt():
    assert Circle(5) > Circle(1)

def test_circle_ge():
    assert Circle(6) >= Circle(5)

def test_circle_sort():
    l = [Circle(1), Circle(10), Circle(2), Circle(9)]
    l.sort()
    assert l[-1] == Circle(10)

def test_circle_reflect_mul_eq():
    assert Circle(3)*3 == 3*Circle(3)

def test_circle_augmented_add():
    c1 = Circle(6) 
    c2 = Circle(2)
    c1 += c2
    assert c1 == Circle(8)

def test_circle_augmented_mul():
    c1 = Circle(3)
    c1 *= 3
    assert c1 == Circle(9)

def test_sphere_init():
    s = Sphere(5)
    assert s.diameter == 10

def test_sphere_diameter():
    s = Sphere.from_diameter(8)
    assert s.radius == 4

def test_sphere_add():
     assert Sphere(5) + Sphere(5) == Sphere(10)

def test_sphere_mul():
     assert Sphere(5)*3 == Sphere(15)

def test_sphere_imul_eq():
     assert Sphere(5)*3 == 3*Sphere(5)