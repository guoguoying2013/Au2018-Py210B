#! usr/bin/env phtyon

""" Testing Circle class assignment by
Arun Nalla 12/08/2018"""

from math import pi
import pytest
from circle import Circle, Sphere
import random


def test_radius():
    x_radius = 2
    c = Circle(x_radius)
    assert c.radius == x_radius


def test_area():
    x_radius = 3
    area = pi * x_radius **2
    c = Circle(x_radius)
    assert c.area == area

def test_diameter():
    x_diameter = 4
    area = pi * (4/2) **2
    c = Circle(x_diameter/2)
    assert c.area == area
    assert c.radius == x_diameter/2

def test_setter():
    x_diameter = 4
    area = pi * (4/2) **2
    c = Circle(x_diameter/2)
    assert c.area == area
    x_diameter = 6
    c1 = Circle(x_diameter/2)
    assert c1.radius == 3

def test_str_():
    c = Circle(2)
    assert str(c) == 'Circle with radius 2'

def test_repr_():
    c = Circle (2)
    assert repr (c) == 'Circle (2)'

def test_add_():
    c1 = Circle(1)
    c2 = Circle(3)
    c3 = c1 + c2
    assert c3.radius == 4 

def test_mul_():
    c1 = Circle(3)
    mul_factor = 2
    c2 = c1 * mul_factor
    assert c2.radius ==6

def test_sort():
    circles = [Circle(r) for r in range(1,4)]
    random.shuffle(circles)
    circles.sort()
    assert circles == [Circle(1), Circle(2), Circle(3)]

    
def test_sphere ():
    x_raidus = 3
    s1 = Sphere(3)
    test_vol = 4/3 * pi * x_raidus**3
    assert s1.volume == test_vol
    