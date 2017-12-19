import math
import segment
import line
import triangle
from circle import *
from angle import *
from vector import *
import mathfunctions
import random
import graphics
from RULE import *

class Point(object):
    def __init__(self, L):        
        self.name = 'unknown'
        if len(L) > 2:
            self.name = L[2]
        self.x = L[0]
        self.y = L[1]
        self.dx = Ox + self.x * ratio
        self.dy = Oy - self.y * ratio
        self.drawn = False
    def draw(self):
        if self.drawn: return
        p = graphics.Point(self.dx, self.dy)        
        label = graphics.Text(graphics.Point(self.dx + 10, self.dy + 10),
                              self.name)
        label.draw(win)
        p.draw(win)
        self.drawn = True
    def __str__(self):
        return "(" + str(self.x) + "; " + str(self.y) + ")"
	
def rand():
    x = random.randint(-TOP_X, TOP_X)
    y = random.randint(-TOP_Y, TOP_Y)
    return Point([x, y])
def taoHam(a, b, point):
    c = -(a*point.x + b*point.y)
    return line.Line([a, b, c])
# return a point which is inside an angle
def insideTriangle(L):
    triangle = L[0]
    A = triangle.A
    B = triangle.B
    C = triangle.C

    M = onSegment([segment.Segment([B, C])])
    v = vector.make_from_two_points(A, M)
    r = random.random()
    M = Point([M.x - r * v.a, M.y - r * v.b])
    return M
        
    
def insideAngle(L):
    angle = L[0]
    O = angle.v1.start
    v1 = angle.v1.v
    v2 = angle.v2.v

    size1 = vector.size(v1)
    size2 = vector.size(v2)
    d1 = 10 / size1
    d2 = 10 / size2        
    x1 = O.x + d1 * v1.a
    y1 = O.y + d1 * v1.b
    t = random.randint(1, 10)
    x2 = O.x + d2 * v2.a
    y2 = O.y + d2 * v2.b
    A = O
    B = Point([x1, y1])
    C = Point([x2, y2])    
    return insideTriangle([triangle.Triangle([A, B, C])])

def outsideTriangle(L):
    triangle = L[0]
    A = triangle.A
    B = triangle.B
    C = triangle.C

    M = onSegment([segment.Segment([B, C])])
    
    v = vector.make_from_two_points(A, M)
    r = random.random()    
    x = M.x + r * v.a
    y = M.y + r * v.b
    M = Point([x, y])
    if (x > TOP_X) or (y > TOP_Y):
        M = Point([M.x - r * v.a, M.y - r * v.b])
    return M
    
# return a point which is on a line
# sao cho, diem do luon nam trong man hinh
def onLine(L):
    line = L[0]
    a = line.a
    b = line.b
    c = line.c

    if a == 0:
        x = random.randint(-TOP_X, TOP_X)
        return Point([x, -c / b])
    if b == 0:
        y = random.randint(-TOP_Y, TOP_Y)
        return Point([-c / a, y])
    
    Left = (-TOP_Y * b - c) / a
    Right = (TOP_Y * b - c) / a
    if Left > Right: (Left, Right) = (Right, Left)        

    Left = max(Left, -TOP_X)
    Right = min(Right, TOP_X)

    x = Left + (Right - Left) * random.random()

    M = Point([x, mathfunctions.getY(line, x)])
    return M
    
def onSegment(L):
    seg = L[0]
    u = vector.directVector_2([L[0]])
    t = random.random()
    return Point([seg.begin.x + u.a * t, \
                  seg.begin.y + u.b * t])
def onCircle(L):
    C = L[0]
    alpha = random.randint(30, 180)
    alpha = mathfunctions.degToRad(alpha)
    sinA = math.sin(alpha)
    cosA = math.cos(alpha)
    x = C.O.x
    y = C.O.y
    R = C.R
    return Point([x + R * sinA, y + R * cosA])
def pos_line(T):
    A = T[0]
    L = T[1]
    L_tmp = line.combine_1([A, L])
    I = intersection([L, L_tmp])
    xB = 2 * I.x - A.x
    yB = 2 * I.y - A.y
    return Point([xB, yB])
def pos_point(L):
    A = L[0]
    B = L[1]
    xC = 2 * B.x - A.x
    yC = 2 * B.y - A.y
    return Point([xC, yC])
# return a point which is the center of a segment
def center(L):
    A = L[0]
    B = L[1]
    seg = segment.Segment([A, B])
    x = (seg.end.x + seg.begin.x) / 2
    y = (seg.end.y + seg.begin.y) / 2
    return Point([x, y])
# return a point which is on a segment with the ratio between distance from Begin and End of the segment
def distanceRatio(L):
    segment = L[0]
    ratio = L[1]
    R = 1 / ratio
    x = (segment.end.x + (R - 1) * segment.begin.x) / R
    y = (segment.end.y + (R - 1) * segment.begin.y) / R
    return Point([x, y])    
# return a point which will be combined with another to create a segment that 'vuong goc' with the line
def combine_1(L):
    (P, L1) = L
    (b, a) = (-L1.a, L1.b)
    c = -(a * P.x + b * P.y)
    return onLine([line.Line([a, b, c])])
# return a point which will be combined with anothor to create a segment that 'song song' with the line
def combine_2(L):
    (P, L1) = L
    (a, b, c) = (L1.a, L1.b, -(a * P.x + b * P.y))
    return onLine([Line(a, b, c)])
# return a point whose segment with another is equal d
def combine_3(L):
    (P, Dist) = L

    x = P.x + Dist * random.random()
    if (x > TOP_X): x = P.x - Dist * random.random()
    
    delta_y = Dist ** 2 - (P.x - x) ** 2
    y = P.y + math.sqrt(delta_y)
    if (y > TOP_Y): y = P.y - math.sqrt(delta_y)
    return Point([x, y])
    
# return a point which is intersection between two lines
def intersection(L):
    line1 = L[0]
    line2 = L[1]
    D = line1.a*line2.b - line2.a*line1.b
    Dx = -line1.c * line2.b - line1.b*-line2.c
    Dy = line1.a * (-line2.c) - line2.a*-line1.c
    if D == 0: return onLine([line1])
    return Point([Dx/D, Dy/D])
#return a point which will be combined with the others to create a triangle
def combine_triangle(L):
    point1 = L[0]
    point2 = L[1]
    a = point1.y - point2.y
    b = -(point1.x - point2.x)
    c = -(a*point1.x + b*point1.y)
    k = False
    while not k:
        x = random.randint(0,10)
        y = random.randint(0,10)
        if a*x + b*y + c !=0:
            k = True
    return Point([x, y])
# return a point which will be combined with the others to create a square
def combine_square(L):
    point1 = L[0]
    point2 = L[1]
    point3 = L[2]
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
def combine_rectangle(L):
    A = L[0]
    B = L[1]
    C = L[2]
    # AB = DC
    dx = B.x - A.x
    dy = B.y - A.y
    xD = C.x - dx
    yD = C.y - dy
    D = Point([xD, yD])
    return D

#return a list of points which is the intersectiojn of a line and circle
def sgn(x):
    if x < 0: return -1
    return 1
def intersect_line_circle(T):

    L = T[0]
    C = T[1]

    d = mathfunctions.distance_line([C.O, L])

    if d > C.R: return []

    if d == C.R:
        L_tmp = line.combine_1([C.O, L])
        return [intersection(L_tmp, L)]

    # pt: (x - x0)^2 + (y - y0)^2 = R^2
    # <=> x^2 + y^2 - 2*x0*x - 2y0*y - R^2 + x0^2 + y0 ^ 2 = 0
    x0 = C.O.x
    y0 = C.O.y
    if L.a == 0:
        y = -L.c / L.b
        a = 1
        b = -2 * x0            
        c = x0 * x0 + (y - y0)**2 - C.R*C.R
        n0 = mathfunctions.expr_degree_two(a, b, c)
        if len(n0) == 0: return []
        xA = n0[0]
        yA = mathfunctions.getY(L, xA)
        res = [Point([xA, yA])]
        if len(n0) > 1:
            xB = n0[1]
            yB = mathfunctions.getY(L, xB)
            res += [Point([xB, yB])]
        return res

    if L.b == 0:
        x = -L.c / L.a
        a = 1
        b = -2 * y0
        c = y0 * y0 + (x - x0)**2 - C.R * C.R
        n0 = mathfunctions.expr_degree_two(a, b, c)
        if len(n0) == 0: return []
        yA = n0[0]
        xA = mathfunctions.getX(L, yA)
        res = [Point([xA, yA])]        
        if len(n0) > 1:
            yB = n0[1]
            xB = mathfunctions.getX(L, yB)
            res += [Point([xB, yB])]
        return res
    
    x1 = -10
    y1 = mathfunctions.getY(L, x1)
    x2 = 10
    y2 = mathfunctions.getY(L, x2)
    x1 = C.O.x - x1
    x2 = C.O.x - x2
    y1 = C.O.y - y1
    y2 = C.O.y - y2

    dx = x2 - x1
    dy = y2 - y1
    dr = math.sqrt(dx*dx + dy*dy)
    D = x1 * y2 - x2 * y1
    delta = math.sqrt(C.R*C.R * dr*dr - D*D)
    xA = (D * dy + sgn(dy)* dx * delta)/(dr * dr)
    yA = (-D * dx + abs(dy) * delta) / (dr * dr)
    A = Point([C.O.x - xA, C.O.y - yA])
    xB = (D * dy - sgn(dy)* dx * delta)/(dr * dr)
    yB = (-D * dx - abs(dy) * delta) / (dr * dr)
    B = Point([C.O.x - xB, C.O.y - yB])
    return [A, B]

# return a list of point which is the intersection of two circles
def intersect_two_circles(L):

    C1 = L[0]
    C2 = L[1]

    d1 = mathfunctions.distance([C1.O, C2.O])
    d2 = C1.R + C2.R
    if d1 > d2: return []
    a = (C1.R ** 2 - C2.R ** 2 + d1 * d1) / (2 * d1)
    
    if C1.R ** 2 < a * a: return []
    
    xA = C1.O.x + a * (C2.O.x - C1.O.x) / d1
    yA = C1.O.y + a * (C2.O.y - C1.O.y) / d1
    
    h = math.sqrt(C1.R ** 2 - a*a)

    xB1 = xA + h * (C2.O.y - C1.O.y) / d1
    xB2 = xA - h * (C2.O.y - C1.O.y) / d1
    yB1 = yA + h * (C2.O.x - C1.O.x) / d1
    yB2 = yA - h * (C2.O.x - C1.O.x) / d1

    A = Point([xB1, yB2])
    B = Point([xB2, yB1])

    return [A, B]
