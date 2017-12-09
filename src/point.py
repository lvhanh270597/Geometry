import math
import segment
import line
import triangle
from circle import *
from angle import *
from vector import *
import mathfunctions
import graphics
from RULE import *

class Point(object):
    def __init__(self, L):
        x = L[0]
        y = L[1]
        self.x = x
        self.y = y
        self.dx = Ox + x * ratio
        self.dy = Oy - y * ratio 
    def draw(self, name='none', color='black', arrow='none'):
        p = graphics.Point(self.dx, self.dy)
        p.setOutline(color)
        label = graphics.Text(graphics.Point(self.dx + 10, self.dy + 10), name)
        label.draw(win)
        p.draw(win)
    def __str__(self):
        return "(" + str(self.x) + "; " + str(self.y) + ")"
	
def rand(L = []):
    if len(L) > 0:
        d = L[0]
    else:
        d = 5
    sx = int(-MAX_W / (2 * ratio) + d)
    tx = int(MAX_W / (2 * ratio) - d)
    sy = int(-MAX_H / (2 * ratio) + d)
    ty = int(MAX_H / (2 * ratio) - d)
    x = random.randint(sx, tx)
    y = random.randint(sy, ty)
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

    seg = segment.Segment([B, C])
    BC = line.convertSegment([seg])
    d = mathfunctions.distance_line([A, BC])

    R = random.random() * d
    O = A

    v1 = vector.make_from_two_points(A, B)
    v2 = vector.make_from_two_points(A, C)
    
    cosBAC = mathfunctions.cos_between_two_vector(v1, v2)

    while True:
        alpha = random.randint(1, 360)
        x = O.x + R * math.cos(mathfunctions.degToRad(alpha))
        y = O.y + R * math.sin(mathfunctions.degToRad(alpha))
        M = Point([x, y])
        v = vector.make_from_two_points(A, M)
        cos1 = mathfunctions.cos_between_two_vector(v1, v)
        cos2 = mathfunctions.cos_between_two_vector(v2, v)
        if cos1 > cosBAC and cos2 > cosBAC:
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
    
# return a point which is on a line 
def onLine(L):
    line = L[0]
    x = random.randint(-10, 10)
    return Point([x, mathfunctions.getY(line, x)])
def onSegment(L):
    seg = L[0]
    u = vector.directVector_2([seg])
    t = random.random()
    return Point([seg.begin.x + u.a * t, seg.begin.y + u.b * t])
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
    x = (seg.end.x + seg.begin.x)/2
    y = (seg.end.y + seg.begin.y)/2
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
    point = L[0]
    L = L[1]
    b = -L.a
    a = L.b
    c = -(a*point.x + b* point.y)
    d = line.Line([a, b, c])
    return onLine([d])
# return a point which will be combined with anothor to create a segment that 'song song' with the line
def combine_2(L):
    point = L[0]
    line = L[1]
    a = line.a
    b = line.b
    c = -(a*point.x + b*point.y)
    return onLine([Line(a, b, c)])
# return a point whose segment with another is equal d
def combine_3(L):
    point = L[0]
    distance = L[1]
    x = random.randint(point.x - distance, point.x)
    k = distance**2 - (point.x - x)**2
    c = random.choice([-1, 1])    
    y = point.y + c * math.sqrt(k)    
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
    while k==False:
        x = random.randint(0,10)
        y = random.randint(0,10)
        if a*x + b*y + c !=0:
            k= True
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
        n0 = mathfunctions.expr_degree_two([a, b, c])
        if len(n0) == 0: return []
        xA = n0[0]
        yA = mathfunctions.getY(L, xA)
        res = [Point(xA, yA)]
        if len(n0) > 1:
            xB = n0[1]
            yB = mathfunctions.getY(L, xB)
            res += [Point(xB, yB)]
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
        res = [Point(xA, yA)]        
        if len(n0) > 1:
            yB = n0[1]
            xB = mathfunctions.getX(L, yB)
            res += [Point(xB, yB)]
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

    d1 = mathfunctions.distance(C1.O, C2.O)
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

