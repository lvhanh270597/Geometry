import math
from segment import *
from line import *
from circle import *
from angle import *
from vector import *
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
def taoHam(a,b,point):
    c = -(a*point.x + b*point.y)
    return Line(a,b,c)
# return a point which is inside an angle
def insideAngle(angle):
    ax = angle.v1.a + angle.O.x
    ay = angle.v1.b + angle.O.y
    bx = angle.v2.a + angle.O.x
    by = angle.v2.b + angle.O.y
    k1= Point((ax + angle.O.x)/2,(ay+ angle.O.y)/2)
    k2 = Point((bx + angle.O.x)/2,(by + angle.O.y)/2)
    x = Point(2*(k1.x + k2.x)/2,2*(k1.y + k2.y)/2)
    return x 
    
# return a point which is on a line 
def onLine(line):
    x = random.randint(0,2)
    y = 0
    if line.b != 0:
        y = (line.a * x + line.c)/(-line.b)
    else:
        y = 0
        x = -c/a    
    return Point(x, y)

# return a point which is the center of a segment
def center(segment):
    x = (segment.end.x + segment.begin.x)/2
    y = (segment.end.y + segment.begin.y)/2
    return Point(x,y)
# return a point which is on a segment with the ratio between distance from Begin and End of the segment
def distanceRatio(segment, ratio):
    R = 1 / ratio
    x = (segment.end.x + (R - 1) * segment.begin.x) / R
    y = (segment.end.y + (R - 1) * segment.begin.y) / R
    return Point(x, y)    
# return a point which will be combined with another to create a segment that 'vuong goc' with the line
def combine_1(point, line):    
    b = -line.a
    a = line.b
    c = -(a*point.x + b* point.y)
    return onLine(Line(a, b, c))
# return a point which will be combined with anothor to create a segment that 'song song' with the line
def combine_2(point, line):
    a = line.a
    b = line.b
    c = -(a*point.x + b*point.y)
    return onLine(Line(a, b, c))    
# return a point whose segment with another is equal d
def combine_3(point, distance):
    x = random.randint(point.x -distance,point.x +distance)
    while x== point.x:
        x = random.randint(point.x-distance,point.x+distance)
    k = distance**2 - (point.x - x)**2
    if(point.y<0):
        y =-( -point.y - math.sqrt(k))
    else:
        y = point.y - math.sqrt(k)
    a = Point(x,y)
    return a
    
# return a point which is intersection between two lines
def intersection(line1, line2):
    D = line1.a*line2.b - line2.a*line1.b
    Dx = -line1.c*line2.b - line1.b*-line2.c
    Dy = line1.a*-line2.c - line2.a*-line1.c
    if D==0:
        a = onLine(line1)
        return a
    return Point(Dx/D,Dy/D)
#return a point which will be combined with the others to create a triangle
def combine_triangle(point1, point2):
    a = point1.y - point2.y
    b = -(point1.x - point2.x)
    c = -(a*point1.x + b*point1.y)
    k = False
    while k==False:
        x = random.randint(0,10)
        y = random.randint(0,10)
        if a*x + b*y + c !=0:
            k= True
    return Point(x,y)
# return a point which will be combined with the others to create a square
def combine_square(point1, point2, point3):
    if (( point1.x - point2.x)*(point1.x - point3.x) + ( point1.y - point2.y)*(point1.y - point3.y)) == 0:
        a = point1
        point1 = point2
        point2 = a
    if (( point3.x - point1.x)*(point3.x - point2.x) + ( point3.y - point1.y)*(point3.y - point2.y)) ==0:
        a = point3
        point3 = point2
        point2 = a
    Vt1x = point2.y - point1.y
    Vt1y = -(point2.x - point1.x)
    Vt2x = point2.y - point3.y
    Vt2y = -(point2.x - point3.x)
    n = (point2.x - point1.x)**2 + (point2.y - point1.y)**2
    m = (point2.x - point3.x)**2 + (point2.y - point3.y)**2
    if Vt1x*Vt2x + Vt1y*Vt2y != 0 or n != m:
        k = "Can not create square"
        return k
    else:
        x = taoHam(Vt1x,Vt1y,point3)
        y = taoHam(Vt2x,Vt2y, point1)
        k = intersection(x,y)
    return k 
        
# return a point which will be combined with the others to create a rectangle
def combine_rectangle(point1, point2, point3):
    if (( point1.x - point2.x)*(point1.x - point3.x) + ( point1.y - point2.y)*(point1.y - point3.y)) == 0:
        a = point1
        point1 = point2
        point2 = a
    if (( point3.x - point1.x)*(point3.x - point2.x) + ( point3.y - point1.y)*(point3.y - point2.y)) ==0:
        a = point3
        point3 = point2
        point2 = a
    Vt1x = point2.y - point1.y
    Vt1y = -(point2.x - point1.x)
    Vt2x = point2.y - point3.y
    Vt2y = -(point2.x - point3.x)
    n = (point2.x - point1.x)**2 + (point2.y - point1.y)**2
    m = (point2.x - point3.x)**2 + (point2.y - point3.y)**2
    if Vt1x*Vt2x + Vt1y*Vt2y != 0:
        k = "Can not create square"
        return k
    else:
        x = taoHam(Vt1x,Vt1y,point3)
        y = taoHam(Vt2x,Vt2y, point1)
        k = intersection(x,y)
    return k 
# return a list of point which is the intersection of two circles
def intersect_two_circles(circle1, circle2):
    d = math.sqrt((circle1.O.x-circle2.O.x)**2 + (circle1.O.y-circle2.O.y)**2)
    if( d > circle1.R + circle2.R) or d < abs(circle1.R-circle2.R):
        return "Cannot find point"
    if d == 0 and circle1.R == circle2.R:
        x = combine_3(circle1.O,cirle1.R)
        y = combine_3(circle1.O,cirle1.R)
        while y == x:
            y = combine_3(circle1.O,cirle1.R)
    a = ( circle1.R**2 - circle2.R**2 + d**2)/(2*d)
    h = math.sqrt(((circle1.R)**2 - a**2))
    px = circle1.O.x + a*(circle2.O.x - circle1.O.x)/d
    py = circle1.O.y + a*(circle2.O.y - circle1.O.y)/d
    x = Point(px + h*(circle2.O.y - circle1.O.y)/d,py - h*(circle2.O.x - circle1.O.x)/d)
    y = Point(px - h*(circle2.O.y - circle1.O.y)/d,py + h*(circle2.O.x - circle1.O.x)/d)
    list = [Point(x.x,x.y),Point(y.x,y.y)];
    return list
