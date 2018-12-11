"""
test code for circle.py and sphere.py
"""

import pytest

# import * is often bad form, but makes it easier to test everything in a module.
from circle import *
from sphere import *


# Step 1 tests

def test_radius():

    c = Circle(5)

    assert c.radius == 5


def test_emptycircle():

    c = Circle()

    assert c.radius == 0


# Step 2 tests

def test_diameter():

    c = Circle(5)

    assert c.diameter == 10


# Step 3 tests

def test_setdiameter():

    c = Circle()
    c.diameter = 6

    assert c.radius == 3
    assert c.diameter == 6


# Step 4 tests

def test_area():

    c = Circle(2)

    assert c.area == 12.566371


def test_setarea():

    c = Circle(2)

    with pytest.raises(AttributeError):
        c.area = 12


# Step 5 tests

def test_diametercontructor():

    c = Circle.from_diameter(8)

    assert c.radius == 4
    assert c.diameter == 8


# Step 6 tests

def test_repr():

    c = Circle(5)
    d = repr(c)
    assert eval(d) == c


# Step 7 tests

def test_add():

    c1 = Circle(5)
    c2 = Circle(3)
    c3 = c1 + c2

    assert c3.radius == 8


def test_multiply():

    c1 = Circle(5)

    c3 = c1 * 3

    assert c3.radius == 15
    assert isinstance(c3, Circle)


def test_multiply_reversearguments():

    c2 = Circle(6)

    c4 = 2 * c2

    assert c4.radius == 12


# Step 8 tests

def test_lessthan():

    c1 = Circle(5)
    c2 = Circle(8)
    c3 = Circle(8)

    assert c1 < c2
    assert not c2 < c1
    assert c1 <= c2
    assert c3 <= c2


def test_greaterthan():

    c1 = Circle(5)
    c2 = Circle(8)
    c3 = Circle(8)

    assert not c1 > c2
    assert c2 > c1
    assert c2 >= c1
    assert c3 >= c2


def test_notequal():

    c1 = Circle(5)
    c2 = Circle(8)
    c3 = Circle(8)

    assert not c2 != c3
    assert c1 != c2


def test_circlesort():

    circles = [Circle(2), Circle(1), Circle(5), Circle(4)]

    circles.sort()

    assert circles == [Circle(1), Circle(2), Circle(4), Circle(5)]


# Step 8 optional

def test_augmentedadd():

    c1 = Circle(5)
    c2 = Circle(3)
    c1 += c2

    assert c1.radius == 8


def test_augmentedmul():

    c1 = Circle(5)

    c1 *= 2

    assert c1.radius == 10


def test_reflected_comparison():

    c1 = Circle(2)
    c2 = Circle(3)

    assert c1 * 2 == 2 * c1
    assert not c1 * 2 == 2 * c2


# Step 9 tests

def test_sphere():

    s = Sphere(5)

    assert s.radius  == 5
    assert s.diameter  == 10
    assert s.volume  == 523.598776


def test_spherediameter():

    s = Sphere.from_diameter(8)

    assert s.radius == 4
    assert s.diameter == 8


def test_spherearea():

    s = Sphere(5)

    with pytest.raises(NotImplementedError):
        a = s.area


def test_sphereadd():

    s1 = Sphere(5)
    s2 = Sphere(8)
    s3 = s1 + s2

    assert s3.radius == 13
    assert type(s3) == Sphere


def test_spheremul():

    s1 = Sphere(5)

    s4 = s1 * 2

    assert s4.radius == 10
    assert type(s4) == Sphere


def test_sphereaugadd():

    s1 = Sphere(5)
    s2 = Sphere(2)

    s1 += s2

    assert s1.radius == 7
    assert type(s1) == Sphere


def test_sphereaugmul():

    s1 = Sphere(5)

    s1 *= 2

    assert s1.radius == 10
    assert type(s1) == Sphere
