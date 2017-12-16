
import point
import segment as sm
import line

class Fourangle(object):
    def __init__(self, L):
        self.A = L[0]
        self.B = L[1]
        self.C = L[2]
        self.D = L[3]
        self.drawn = False
        self.name = L[0].name + L[1].name + L[2].name + L[3].name
        if len(L) > 4: self.name = L[4]
    def draw(self):
        if self.drawn: return 
        AB = sm.Segment([self.A, self.B])
        BC = sm.Segment([self.B, self.C])
        CD = sm.Segment([self.C, self.D])
        DA = sm.Segment([self.D, self.A])
        AB.draw()
        BC.draw()
        CD.draw()
        DA.draw()
        self.drawn = True

def equal(A, B):
    return A.x == B.x and A.y == B.y

def rand(L=None):
    A = point.rand()
    B = point.rand()
    C = point.rand()
    D = point.rand()
    while equal(A, B) or equal(B, C) or equal(A, C) or equal(D, A):
        A = point.rand()
        B = point.rand()
        C = point.rand()
        D = point.rand()
    return Fourangle([A, B, C, D])

def rand_rectangle(L=None):
    A = point.rand()
    B = point.combine_3([A, 4])
    seg = sm.Segment([A, B])
    d = line.convertSegment([seg])
    C = point.combine_1([B, d])
    D = point.combine_rectangle([A, B, C])
    return Fourangle([A, B, C, D])
    
def rand_hinhBinhHanh(L=None):
    A = point.rand()
    B = point.combine_3([A, 4])
    C = point.rand()
    D = point.combine_rectangle([A, B, C])
    return Fourangle([A, B, C, D])










    
