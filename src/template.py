

import random
import point
import line
import segment
import circle
import angle
import ray
import graphics
import triangle
import fourangle
import vector
import mathfunctions
from RULE import *


value = {}
variables = []


def V():
    return value.keys()

def Tia(Ox):
    Var = V()
    if Ox in Var: return
    O = Ox[0]
    x = Ox[1]    
    if O not in Var:        
        value[O] = point.rand()
        value[O].name = O
    if x not in Var:                
        value[x] = vector.rand()
        value[x].name = x
        
    ray_Ox = ray.Ray([value[O], value[x]])    
    value[Ox] = ray_Ox
    ray_Ox.draw()

def Doan(AB):
    Var = V()
    if AB in Var: return
    A = AB[0]
    B = AB[1]
    if A not in Var:        
        value[A] = point.rand()
        value[A].name = A
    if B not in variables:                
        value[B] = point.rand()
        value[B].name = B 
    seg = segment.Segment([value[A], value[B]])
    value[AB] = seg
    seg.draw()

def Duong(d):
    if d in variables: return
    active[d] = True
    variables.append(d)
    value[d] = line.rand()
    return value[d]

def TamGiac(ABC):
    if ABC in variables: return
    (A, B, C) = map(str, list(ABC))
    if A not in variables:
        active[A] = True
        value[A] = point.rand([A])
        variables.append(A)        
    if B not in variables:        
        active[B] = True
        value[B] = point.rand([B])
        variables.append(B)
    if C not in variables:
        active[C] = True
        value[C] = point.rand([C])
        variables.append(C)
    tgABC = triangle.Triangle([ABC, value[A], value[B], value[C]])
    value[ABC] = tgABC
    return tgABC
        
def TamGiacVuong(ABC):
    if ABC in variables: return
    (A, B, C) = map(str, list(ABC))
    AB = A+B
    if A not in variables:
        active[A] = True
        value[A] = point.rand([A])
        variables.append(A)        
    if B not in variables:        
        active[B] = True
        value[B] = point.rand([B])
        variables.append(B)
    else:
        d = line.convertSegment([segment.Segment([AB, value[A], value[B]])])
        point_C = point.combine_1([value[A], d])
        point_C.name = C
        active[C] = True
        value[C] = point_C
        variables.append(C)
    if C not in variables:
        d = line.convertSegment([segment.Segment([AB, value[A], value[B]])])
        point_C = point.combine_1([value[A], d])
        point_C.name = C
        active[C] = True
        value[C] = point_C
        variables.append(C)

    tgABC = triangle.Triangle([ABC, value[A], value[B], value[C]])
    value[ABC] = tgABC
    return tgABC

def TamGiacCan(ABC):
    if ABC in variables: return
    (A, B, C) = map(str, list(ABC))
    AB = A+B
    if A not in variables:
        active[A] = True
        value[A] = point.rand([A])
        variables.append(A)        
    if B not in variables:        
        active[B] = True
        value[B] = point.rand([B])
        variables.append(B)
    else:
        d = line.convertSegment([segment.Segment([AB, value[A], value[B]])])
        point_C = point.combine_1([value[A], d])
        point_C.name = C
        active[C] = True
        value[C] = point_C
        variables.append(C)
    if C not in variables:
        d = line.convertSegment([segment.Segment([AB, value[A], value[B]])])
        point_C = point.combine_1([value[A], d])
        point_C.name = C
        active[C] = True
        value[C] = point_C
        variables.append(C)

def main():    
    Tia('Oy')
    Doan('OB')
    
    TamGiacVuong('COA')

main()
    

















