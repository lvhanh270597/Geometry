
import random
import point
import graphics
from RULE import *

class Segment(object):

    def __init__(self, L):
        begin = L[0]
        end = L[1]
        self.begin = begin
        self.end = end
    def draw(self, name='none', color='black', arrow='none'):
        p1 = graphics.Point(self.begin.dx, self.begin.dy)
        p2 = graphics.Point(self.end.dx, self.end.dy)
        line = graphics.Line(p1, p2)
        line.setOutline(color)
        line.setArrow(arrow)
        line.draw(win)
    def __str__(self):
        return "(" + str(self.begin) + ", " + str(self.end) + ")"    
       
def rand(L=None):
	a = point.rand()
	b = point.rand()
	return Segment(a, b)
