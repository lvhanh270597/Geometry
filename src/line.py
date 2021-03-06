
import random
import point
import segment
import vector
import math
import mathfunctions
import graphics
from RULE import *

class Line(object):
    def __init__(self, L):
        self.a = L[0]
        self.b = L[1]
        self.c = L[2]
        self.name = 'unknown'
        if len(L) > 3: self.name = L[3]
        self.drawn = False
    def draw(self):
        if self.a == 0:            
            p1 = point.Point([-100, -self.c / self.b])
            p2 = point.Point([100, -self.c / self.b])            

        else:
            if self.b == 0:            
                p1 = point.Point([-self.c / self.a, -100])
                p2 = point.Point([-self.c / self.a, 100])                
            else:
                a = -25
                b = 25
                p1 = point.Point([a, mathfunctions.getY(self, a)])
                p2 = point.Point([b, mathfunctions.getY(self, b)])                
        
        p1 = graphics.Point(p1.dx, p1.dy)
        p2 = graphics.Point(p2.dx, p2.dy)
        seg = graphics.Line(p1, p2)        
        seg.draw(win)
        self.drawn = True
    def __str__(self):
        return str(self.a) + "x + " + str(self.b) + "y + " + str(self.c) + " = 0"

# return a random line
def rand(L=None):
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    while a == 0 and b == 0:
        a = random.randint(s, t)
        b = random.randint(s, t)
    c = random.randint(-10, 10)
    return Line([a, b, c])

# return a line which is through the point
def throughPoint_1(L):
    point = L[0]
    a = random.randint(1,10)
    b = random.randint(1,10)
    while a == 0 and b == 0:
        a = random.randint(1,10)
        b = random.randint(1,10)
    c = -(a*point.x + b*point.y)
    return Line([a, b, c])


def duongTrungTruc(L):
    A = L[0]
    B = L[1]
    M = point.center([A, B])
    seg = segment.Segment([A, B])
    d = convertSegment([seg])
    d2 = combine_1([M, d])
    return combine_1([M, d])

def duongTrungTuyen(L):
    tri = L[0]
    (A, B, C) = (tri.A, tri.B, tri.C)
    M = point.center([B, C])
    seg = segment.Segment([A, M])
    d = convertSegment([seg])
    return d

def duongTrungBinh(L):
    tri = L[0]
    A = L[1]
    (D, B, C) = (tri.A, tri.B, tri.C)
    if A.name == B.name: B = D
    if A.name == C.name: C = D
        
    M = point.center([A, B])
    N = point.center([A, C])
    seg = segment.Segment([M, N])
    d = convertSegment([seg])
    return d

# return a line which is combined with another to create the angle
# note that: angle is float variable
def combine_angle(L):
    line = L[0]
    angle = L[1]
    num = math.pow(math.cos(math.radians(angle))*math.sqrt(math.pow(line.a,2) + math.pow(line.b,2)),2)
    a = mathfunctions.pt(line.a**2 - num, 2*line.a*line.b, line.b**2 - num)
    b = 1
    point1 = point.Point([0, 1]);
    c = -(a*point1.x + b*point1.y)
    return Line([a, b, c])
# return a line which is through the point and 'vuong goc' with the line
def combine_1(L):
    point = L[0]
    line = L[1]
    a = line.b
    b = -line.a
    c = -(a * point.x + b * point.y)
    return Line([a, b, c])
# return a line which is through the point and 'song song' with the line
def combine_2(L):
    point = L[0]
    line = L[1]
    a = line.a
    b = line.b
    c = -(a*point.x + b*point.y)
    return Line([a, b, c])
# return a line which is a convert of the segment
def convertSegment(L):
    segment = L[0]
    a = -segment.end.y + segment.begin.y
    b = segment.end.x - segment.begin.x
    c = -(a*segment.end.x + b*segment.end.y)
    return Line([a, b, c])
# return a line which is a convert of the ray
def convertRay(L):
    ray = L[0]
    a = -ray.v.b
    b = ray.v.a
    c = -(a*ray.start.x + b*ray.start.y)
    return Line([a, b, c])



