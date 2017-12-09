
import point
import segment as sm
from RULE import *


class Triangle(object):
    def __init__(self, L):        
        self.A = L[0]
        self.B = L[1]
        self.C = L[2]
    def draw(self, color='black'):
        AB = sm.Segment([self.A, self.B])
        AC = sm.Segment([self.A, self.C])
        BC = sm.Segment([self.B, self.C])
        AB.draw(color)
        AC.draw(color)
        BC.draw(color)

def equal(A, B):
    return A.x == B.x and A.y == B.y

def rand(L = None):
    A = point.rand()
    B = point.rand()
    C = point.rand()
    while equal(A, B) or equal(B, C) or equal(A, C):
        A = point.rand()
        B = point.rand()
        C = point.rand()
    return Triangle([A, B, C])
