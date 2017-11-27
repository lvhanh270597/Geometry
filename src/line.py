
import random

class Line(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c            

# return a random line
def rand(s=1, t=10):
	a = random.randint(s, t)
	b = random.randint(s, t)
	while a == 0 and b == 0:
		a = random.randint(s, t)
		b = random.randint(s, t)
	c = random.randint(s, t)
	return Line(a, b, c)

# return a line which is through the point
def throughPoint(point):
	return None
# return a line which is combined with another to create the angle
# note that: angle is float variable
def combine_angle(line, angle):
	return None
# return a line which is through the point and 'vuong goc' with the line
def combine_1(point, line):
	return None
# return a line which is through the point and 'song song' with the line
def combine_2(point, line):
	return None
# return a line which is a convert of the segment
def convertSegment(segment):
	return None
# return a line which is a convert of the ray
def convertRay(ray):
	return None
