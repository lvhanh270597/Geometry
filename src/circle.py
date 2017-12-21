
import random
import segment
import point
import line
import graphics
import math
from RULE import *

class Circle(object):
    def __init__(self, L):        
        self.O = L[0]
        self.R = L[1]
        self.drawn = False
        self.name = 'unknown'
        if len(L) > 2: self.name = L[2]
    def draw(self):
        if self.drawn: return
        p = graphics.Point(self.O.dx, self.O.dy)
        C = graphics.Circle(p, self.R * ratio)
        C.draw(win)
        self.O.name = self.name
        self.O.draw()
        self.drawn = True
    def __str__(self):
    	return "(" + str(self.O) + ", " + str(self.R) + ")"

def rand(L = None):
    O = point.rand()
    R = random.randint(1, 100)
    return Circle(O, R)

# return a circle which goes through three points
def through_three(L):
    pointA = L[0]
    pointB = L[1]
    pointC = L[2]
    point1 = point.center([pointA, pointB])
    line1 = line.convertSegment([segment.Segment([pointA,pointB])])
    line2 = line.combine_1([point1, line1])
    point2 = point.center([pointA, pointC])
    line3 = line.convertSegment([segment.Segment([pointA,pointC])])
    line4 = line.combine_1([point2, line3])
    O = point.intersection([line2, line4])
    R = math.sqrt(math.pow(O.x - pointA.x,2) + math.pow(O.y - pointA.y,2))
    return Circle([O, R])

        
