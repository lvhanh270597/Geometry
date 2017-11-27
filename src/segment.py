
import random
import point

class Segment(object):

    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
    def __str__(self):
        return "(" + str(self.begin) + ", " + str(self.end) + ")"
       
def rand():
	a = point.rand()
	b = point.rand()
	return Segment(a, b)