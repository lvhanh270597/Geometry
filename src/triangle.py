
import point
import segment as sm
import mathfunctions
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

def isTamGiac(A, B, C):
    a = mathfunctions.distance([A, B])
    b = mathfunctions.distance([B, C])
    c = mathfunctions.distance([A, C])
    return (a + b > c) and (a + c > b) and (b + c > a)

def rand(L = None):
    A = point.rand()
    B = point.rand()
    C = point.rand()
    while not isTamGiac(A, B, C):
        A = point.rand()
        B = point.rand()
        C = point.rand()
    return Triangle([A, B, C])
