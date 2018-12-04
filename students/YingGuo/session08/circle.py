#!/usr/bin/env python3

#homework session 08 Ying Guo

from math import pi


class Circle():

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        self.D = self.radius*2
        return self.D

    @diameter.setter
    def diameter(self, d):
        self.radius = d/2

    #The user should not be able to set the area. How to test this?
    @property
    def area(self):
        self.a = pi*(self.radius**2)
        return self.a
    
    @classmethod
    def re_construct(cls, D):
        cls.radius = D/2
        return cls.radius

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)
    
    def __repr__(self):
        return "Circle({})".format(self.radius)
    
    def __add__(self, other):
        new_r = self.radius + other.radius
        return Circle(new_r)

    def __mul__(self, a_num):
        new_r = self.radius*a_num
        return Circle(new_r)

    def __eq__(self, other):
        return self.radius == other.radius
    
    def __lt__(self,other):
        return self.radius < other.radius

class Sphere(Circle):
    def __str__(self):
        return "Sphere with radius: {}".format(self.radius)
    
    def __repr__(self):
        return "Sphere({})".format(self.radius)
    
    def volume(self):
        return (4/3)*pi*(self.radius**3)
    
    def area(self):
        raise NotImplementedError
