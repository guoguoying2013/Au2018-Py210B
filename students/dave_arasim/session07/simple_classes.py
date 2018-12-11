#!/usr/bin/env python
"""
simple_classes.py

demonstrating the basics of a class
"""

import math


# create a point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# create an instance of that class
p = Point(3, 4)

# access the attributes
print("p.x is:", p.x)
print("p.y is:", p.y)
print()


class Point2:
    size = 4
    color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

p2 = Point2(4, 5)
print('p2.size is:', p2.size)
print('p2.color is:', p2.color)
print('p2.x is:', p2.x)
print('p2.y is:', p2.y)
print()


class Point3:
    size = 4
    color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_color(self):
        return self.color

    def get_size(self):
        return  self.size

p3 = Point3(4, 5)
print('p3.size:', p3.size)
print('p3.get_color():', p3.get_color())
print()

        
class Rect:

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_size(self):
        return self.w * self.h

r1 = Rect(20, 25)
print('r1.w:', r1.w)
print('r1.h:', r1.h)
print('r1.get_size():', r1.get_size())
print()


class Circle:
    color = "red"
    styles = ['dashed']

    def __init__(self, diameter):
        self.diameter = diameter

    def grow(self, factor=2):
        """
        grows the circle's diameter

        :param factor=2: factor by which to grow the circle
        """
        self.diameter = self.diameter * factor

    def add_style(self, style):
        self.styles.append(style)

    def get_area(self):
        return math.pi * (self.diameter / 2.0)**2

c1 = Circle(10)
print('c1.diameter:', c1.diameter)
c1.grow()
print('c1.diameter:', c1.diameter)
c1.grow()
print('c1.diameter:', c1.diameter)
c1.grow(20)
print('c1.diameter:', c1.diameter)
print('c1.styles:', c1.styles)
c1.add_style('solid')
print('c1.styles:', c1.styles)
c1.add_style('dotted')
print('c1.styles:', c1.styles)
print('c1.get_area():', c1.get_area())
print()
        
        
class NewCircle(Circle):
    color = "blue"

    def grow(self, factor=2):
        """grows the area by factor..."""
        self.diameter = self.diameter * math.sqrt(factor)

nc = NewCircle(15)
print('nc.color:', nc.color)
print('nc.diameter:', nc.diameter)
nc.grow(16)
print('nc.diameter:', nc.diameter)
print()


class CircleR(Circle):
    def __init__(self, radius):
        diameter = radius*2
        Circle.__init__(self, diameter)

cr1 = CircleR(10)
print('cr1.diameter:', cr1.diameter)
print()
        

class CircleR2(Circle):
    def __init__(self, radius):
        self.radius = radius
        Circle.__init__(self, radius*2)

    def get_area(self):
        return Circle.get_area(self)

cr2 = CircleR2(200)
print('cr2.radius:', cr2.radius)
print('cr2.get_area():', cr2.get_area())
