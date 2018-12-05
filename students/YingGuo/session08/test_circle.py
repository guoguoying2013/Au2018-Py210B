from circle import Circle
from math import pi
from circle import Sphere
import pytest

def test_initiation():
    example = Circle(2)
    assert example.radius == 2

def test_diameter():
    example = Circle(2)
    assert example.diameter == 4

def test_set_diameter():
    example = Circle(2)
    example.diameter = 6
    print(example.diameter)
    print(example.radius)
    assert example.radius == 3
    
def test_area():
    example = Circle(2)
    assert example.area == 4*pi

#The test below i got invalid syntax. why is that?
def test_area_attribute():
    example = Circle(2)
    with pytest.raises(AttributeError):
        example.area = 8

def test_re_construct():
    assert Circle.re_construct(8) == 4 

def test_str():
    example = Circle(2)
    assert str(example) == "Circle with radius: 2"

def test_repr():
    example = Circle(2)
    assert repr(example) == "Circle(2)"

def test_add():
    print(Circle(2)+Circle(4))
    print(Circle(6))
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    assert c3 == Circle(6)

def test_mul():
    c1 = Circle(2)*3
    print(c1)
    assert c1 == Circle(6)

def test_sort():
    list=[Circle(6), Circle(7), Circle(3)]
    list.sort()
    assert list == [Circle(3), Circle(6), Circle(7)]

def test_sphere():
    example = Sphere(2)
    assert example.volume() == (4/3)*pi*8