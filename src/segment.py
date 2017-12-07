
import random
import point
import graphics

class Segment(object):

    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
    def draw(self, win, color='black'):
        p1 = graphics.Point(self.begin.x + 250, self.begin.y + 250)
        p2 = graphics.Point(self.end.x + 250, self.end.y + 250)
        line = graphics.Line(p1, p2)
        line.setOutline(color)
        line.draw(win)
    def __str__(self):
        return "(" + str(self.begin) + ", " + str(self.end) + ")"    
       
def rand():
	a = point.rand()
	b = point.rand()
	return Segment(a, b)
