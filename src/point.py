
import random
import line
import segment
import ray
import circle

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y        
    def __str__(self):
        return "(" + str(self.x) + "; " + str(self.y) + ")"
	
def rand(a=100, b=500):
    x = random.randint(a, b)
    y = random.randint(a, b)
    return Point(x, y)

# return a point which is inside an angle
def insideAngle(angle):
	return None
# return a point which is on a line
def onLine(line):
	return None
# return a point which is the center of a segment
def center(segment):
	return None
# return a point which is on a segment with the ratio between distance from Begin and End of the segment
def distanceRatio(segment):
	return None
# return a point which will be combined with another to create a segment that 'vuong goc' with the line
def combine_1(point, line):
	return None
# return a point which will be combined with anothor to create a segment that 'song song' with the line
def combine_2(point, line):
	return None
# return a point whose segment with another is equal d
def combine_3(point, distance):
	return None
# return a point which is intersection between two lines
def intersection(line1, line2):
	return None
# return a point which will be combined with the others to create a triangle
def combine_triangle(point1, point2):
	return None
# return a point which will be combined with the others to create a square
def combine_square(point1, point2, point3):
	return None
# return a point which will be combined with the others to create a rectangle
def combine_rectangle(point1, point2, point3):
	return None
# return a list of point which is the intersection of two circles
def intersect_two_circles(circle1, circle2):
	return None		
