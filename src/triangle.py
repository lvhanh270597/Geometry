
import line
import point
import segment as sm
import mathfunctions
import random
from RULE import *


class Triangle(object):
    def __init__(self, L):        
        self.A = L[0]
        self.B = L[1]
        self.C = L[2]
        self.drawn = False
        self.name = 'unknown'
        if len(L) > 3: self.name = L[3]        
    def draw(self):
        if self.drawn: return
        AB = sm.Segment([self.A, self.B])
        AC = sm.Segment([self.A, self.C])
        BC = sm.Segment([self.B, self.C])
        AB.draw()
        AC.draw()
        BC.draw()
        self.drawn = True

def smaller(a, b, c):
    return (a * 2 <= b) or (a * 2 <= c)

def isTamGiac(A, B, C):
    a = mathfunctions.distance([A, B])
    b = mathfunctions.distance([B, C])
    c = mathfunctions.distance([A, C])
    if smaller(a, b, c) or smaller(b, a, c) or smaller(c, a, b):
        return False
    return (a + b > c) and (a + c > b) and (b + c > a)

def randABC():
    A = point.Point([-4, -2])
    B = point.Point([A.x + random.randint(8, 12), -2])
    
    seg = sm.Segment([A, B])
    ln = line.convertSegment([seg])
    C = point.rand()
    dist = mathfunctions.distance_line([C, ln])
    while (dist < 4) or (dist > 8):
        C = point.rand()
        dist = mathfunctions.distance_line([C, ln])
    return (A, B, C)

def rand():
    (A, B, C) = randABC()
    while not isTamGiac(A, B, C):
        (A, B, C) = randABC()
    return Triangle([A, B, C])
