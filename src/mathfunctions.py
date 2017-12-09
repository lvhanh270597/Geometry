import math
import point
import line
import random
import vector

def pt(L):
    a = L[0]
    b = L[1]
    c = L[2]
    denta = b**2 - 4*a*c
    if denta < 0:
        return 0
    if denta == 0:
        return -b/(2*a)
    if denta > 0:
        return (-b + math.sqrt(denta))/(2*a)


def cos_between_two_vector(v1, v2):
    t = v1.a * v2.a + v1.b * v2.b
    m = vector.size(v1) * vector.size(v2)
    return t / m 

def degToRad(x):
    return (x / 180) * math.pi
def radToDeg(x):
    return (x / math.pi) * 180

def expr_degree_two(a, b, c):
    delta = b * b - 4 * a * c
    if delta < 0:
        return []
    if delta == 0:
        return [-b / (2 * a)]
    root_delta = math.sqrt(delta)
    return [(-b - root_delta) / (2 * a), (- b + root_delta) / (2 * a)]

def distance(L):
    p1 = L[0]
    p2 = L[1]
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
def distance_line(T):
    p = T[0]
    L = T[1]
    A = abs(L.a * p.x + L.b * p.y + L.c)
    return A / math.sqrt(L.a ** 2 + L.b ** 2)
# return y if x is known
def getY(L, x0):
    if L.b == 0: return random.randint(-100, 100)
    return (L.a * x0 + L.c) / (-L.b)
# return x if y is known
def getX(L, y0):
    if L.a == 0: return random.randint(-100, 100)
    return (L.b * y0 + L.c) / (-L.a)
