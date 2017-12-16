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

def V():
    return value.keys()

# PHan Doan - Doan
# VD List A
# M, A, B
def TrungDiem(L):
    Var = V()
    
    M = L[0]
    A = L[1]
    B = L[2]
    if A not in  Var: return
    if B not in Var: return
    
    pA = value[A]
    pB = value[B]
    pM = point.center([pA, pB])

    pA.name = A
    pB.name = B
    pM.name = M
    
    value[M] = pM
    pM.draw()

# L = [M, AB]
# M nam giua A va B
# AB la segment
def NamGiua(L):
    Var = V()
    M = L[0]
    AB = L[1]

    if AB not in Var: return
    
    AB = value[AB]
    
    k = random.random()
    pM = point.distanceRatio([AB, k])

    pM.name = M
    value[M] = pM
    
    pM.draw()

def KhongNamGiua(L):    
    Var = V()
    M = L[0]
    AB = L[1]

    if AB not in Var: return
    
    AB = value[AB]
    
    k = random.choice([1.25, 1.5, 1.75, 2, 2.25])
    
    pM = point.distanceRatio([AB, k])
    pM.name = M
    
    value[M] = pM
    pM.draw()
# vd Giaodiem(ABCDE) nghia la A la giao diem BC DE
# L = [M, AB, CD]
def GiaoDiemDoan(L):
    Var = V()
    M = L[0]
    AB = L[1]
    CD = L[2]

    if AB not in Var: return
    if CD not in Var: return
    
    d1 = line.convertSegment([value[AB]])
    d2 = line.convertSegment([value[CD]])
    pM = point.intersection([d1, d2])
    pM.name = M
    value[M]= pM
    M.draw()
    
