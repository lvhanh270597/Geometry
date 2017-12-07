
import random
import point
import segment
import vector
import math
import mathfunctions
import graphics

class Line(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def draw(self, win, color='black'):
        a = -250
        b = 250
        p1 = point.Point(a, mathfunctions.getY(self, a))
        p2 = point.Point(b, mathfunctions.getY(self, b))
        print(p1, p2)
        
        p1 = graphics.Point(p1.x + 250, p1.y + 250)
        p2 = graphics.Point(p2.x + 250, p2.y + 250)
        seg = graphics.Line(p1, p2)
        seg.setOutline(color)        
        seg.draw(win)
    def __str__(self):
        return str(self.a) + "x + " + str(self.b) + "y + " + str(self.c) + " = 0"

# return a random line
def rand(s=-10, t=10):
    a = random.randint(s, t)
    b = random.randint(s, t)
    while a == 0 and b == 0:
        a = random.randint(s, t)
        b = random.randint(s, t)
    c = random.randint(-1000, 1000)
    return Line(a, b, c)

# return a line which is through the point
def throughPoint_1(point):
    a = random.randint(1,10)
    b = random.randint(1,10)
    while a == 0 and b == 0:
        a = random.randint(1,10)
        b = random.randint(1,10)
    c = -(a*point.x + b*point.y)
    return Line(a, b, c)


# return a line which is combined with another to create the angle
# note that: angle is float variable
def combine_angle(line, angle):
    num = math.pow(math.cos(math.radians(angle))*math.sqrt(math.pow(line.a,2) + math.pow(line.b,2)),2)
    a = mathfunctions.pt(pow(line.a,2) - num, 2*line.a*line.b, pow(line.b,2) - num)
    b = 1
    point1 = point.Point(0,1);
    c = -(a*point1.x + b*point1.y)
    return Line(a, b, c)
# return a line which is through the point and 'vuong goc' with the line
def combine_1(point, line):    
    a = line.b
    b = -line.a
    c = -(a*point.x + b*point.y)
    return Line(a, b, c)
# return a line which is through the point and 'song song' with the line
def combine_2(point, line):
    a = line.a
    b = line.b
    c = -(a*point.x + b*point.y)
    return Line(a, b, c)
# return a line which is a convert of the segment
def convertSegment(segment):
    a = - segment.end.y + segment.begin.y
    b = segment.end.x - segment.begin.x
    c = -(a*segment.end.x + b*segment.end.y)
    return Line(a, b, c)
# return a line which is a convert of the ray
def convertRay(ray):
    a = -ray.v.b
    b = ray.v.a
    c = -(a*ray.start.x + b*ray.start.y)
    return Line(a, b, c)



