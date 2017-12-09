
import random
import point
import graphics
from RULE import *

class Circle(object):
    def __init__(self, L):
        O = L[0]
        R = L[1]
        self.O = O
        self.R = R
    def draw(self, color='black'):
        p = graphics.Point(self.O.dx, self.O.dy)
        c = graphics.Circle(p, self.R * ratio)
        c.setOutline(color)
        c.draw(win)
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
    point1 = point.center(segment.Segment(pointA, pointB))
    line1 = line.convertSegment(segment.Segment(pointA,pointB))
    line2 = line.combine_1(point1, line1)
    point2 = point.center(segment.Segment(pointA, pointC))
    line3 = line.convertSegment(segment.Segment(pointA,pointC))
    line4 = line.combine_1(point2, line3)
    O = point.intersection(line2, line4)
    R = math.sqrt(math.pow(O.x - pointA.x,2) + math.pow(O.y - pointA.y,2))
    return Circle(O, R)

        
