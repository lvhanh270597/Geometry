
import random
import point
import vector

class Ray(object):
    def __init__(self, S, v):
        self.start = S
        self.v = v
    def __str__(self):
    	return "(" + str(self.start) + ", " + str(v) + ')'    	
    
# return a random ray    
def rand():
	start = point.rand()
	v = vector.rand()
	return Ray(start, v)