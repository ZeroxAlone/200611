# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:47:43 2020

@author: lisa_
"""

#1

import math

class Point:
    def __init__(self, initx, inity):
        self.x = initx
        self.y = inity
        
    def GetX(self):
        return self.x
    
    def GetY(self):
        return self.y
    
    def DistanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def DistanceFromPoint(self, Points):
        dx=Points.GetX()-self.x
        dy=Points.GetY()-self.y
        return math.sqrt(dy**2 + dx**2)
    
    def reflect_x(self):
        self.y = -self.y
        return self.x, self.y
    
    def slope_from_origin(self):
        slope = self.y/self.x
        return slope

    def get_line_to(self, Points):
        m = (self.y-Points.y)/(self.x-Points.x)
        c = self.y-self.x * m
        return m, c
    
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        return self.x , self.y
    
    def center_and_radius(self, Pst, Pnd):
        self.x = (self.x + Pst.x) / 2
        self.y = (self.y + Pst.y) / 2
        Pnd.x = (Pnd.x + Pst.x) / 2
        Pnd.y = (Pnd.y + Pst.y) / 2
        k = -(self.x - Pst.x) / (self.y - Pst.y)
        m = -(Pnd.x - Pst.x) / (Pnd.y - Pst.y)
        x = (Pnd.y-self.y-m*Pnd.x+k*self.x)/(k-m)
        # y = self.y+k*(Pnd.y-self.y-m*Pnd.x+m*self.x)/(k-m)
        y = k*x+self.y-k*self.x
        r = math.sqrt((x-self.x)**2+(y-self.y)**2)
        return x, y, r
        
    
p = Point(3, 3)
q = Point(6, 7)

print(p.DistanceFromPoint(q))
print(Point(3, 5).reflect_x())
print(Point(4, 10).slope_from_origin())
print(Point(4, 11).get_line_to(Point(6, 15)))

p = Point(7, 6)
print(p.move(5, 10))


o = Point(1,2)
p = Point(0,1)
q = Point(1,0)
print(o.center_and_radius(p, q))