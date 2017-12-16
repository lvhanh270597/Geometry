
import random
import point
import graphics
import vector
import mathfunctions
from RULE import *

class Segment(object):

    def __init__(self, L):
        self.begin = L[0]
        self.end = L[1]
        self.drawn = False
        self.name = L[0].name + L[1].name
        if len(L) > 2: self.name = L[2]
    def draw(self):
        if self.drawn: return
        self.begin.draw()
        self.end.draw()
        p1 = graphics.Point(self.begin.dx, self.begin.dy)
        p2 = graphics.Point(self.end.dx, self.end.dy)
        line = graphics.Line(p1, p2)                
        line.draw(win)
        self.drawn = True
    def __str__(self):
        return "(" + str(self.begin) + ", " + str(self.end) + ")"    
       
def rand(L=None):
	a = point.rand()
	b = point.rand()
	return Segment(a, b)
def convertRay(L):
    ray = L[0]
    size = vector.size(ray.v)
    dx = 10/size
    dy = 10/size
    a = ray.start
    x = ray.v.a * dx + a.x
    y = ray.v.b * dy + a.y
    b = point.Point([x,y])
    return Segment([a,b])
    
