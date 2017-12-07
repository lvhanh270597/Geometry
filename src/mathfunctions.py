import math
import point
import line
import random

def pt(a,b,c):
    denta = b**2 - 4*a*c
    if denta < 0:
        return 0
    if denta == 0:
        return -b/(2*a)
    if denta > 0:
        return (-b + math.sqrt(denta))/(2*a)

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
# return y if x is known
def getY(L, x0):
    if L.b == 0: return random.randint(-100, 100)
    return (L.a * x0 + L.c) / (-L.b)
# return x if y is known
def getX(L, y0):
    if L.a == 0: return random.randint(-100, 100)
    return (L.b * y0 + L.c) / (-L.a)
