
import random
import point

class Circle(object):
    def __init__(self, O, R):
        self.O = O
        self.R = R
    def __str__(self):
    	return "(" + str(O) + ", " + str(R) + ")"

def rand():
	O = point.rand()
	R = random.randint(1, 100)
	return Circle(O, R)

# return a circle which goes through three points
def through_three():
	return None

        
