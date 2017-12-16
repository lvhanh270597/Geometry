
import math
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

def V(): return value.keys()

def ganHoanVi(S, v):
    n = len(S)
    for i in range(n):
        value[S] = v
        value[S].name = S
        S += S[0]
        S = S[1 : ]
    S = S[::-1]
    for i in range(n):
        value[S] = v
        value[S].name = S
        S += S[0]
        S = S[1 : ]

############################################################
############################################################
########################### Hanh ###########################
############################################################
############################################################
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
        
    ray_Ox = ray.Ray([value[O], value[x], Ox])    
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
    if B not in Var:                
        value[B] = point.rand()
        value[B].name = B 

    seg = segment.Segment([value[A], value[B], AB])
    ganHoanVi(AB, seg)
    #value[AB] = seg
    seg.draw()

def Duong(d):
    Var = V()
    if d in Var: return    
    value[d] = line.rand()    
    return value[d]

def TamGiac(ABC, show=1):
    Var = V()
    if ABC in Var: return
    (A, B, C) = map(str, list(ABC))
    if (A not in Var) and \
       (B not in Var) and \
       (C not in Var):
        tri = triangle.rand()
        value[A] = tri.A
        value[B] = tri.B
        value[C] = tri.C
        value[A].name = A
        value[B].name = B
        value[C].name = C
        tgABC = tri
        tgABC.name = ABC
        value[ABC] = tgABC
        if (show == 1):
            tgABC.draw()
        return tgABC
    if (A in Var) and \
       (B in Var) and \
       (C in Var):
        tgABC = triangle.Triangle([value[A], value[B], value[C], ABC])
        value[ABC] = tgABC
        if (show == 1):
            tgABC.draw()
        return tgABC
        
def TamGiacVuong(ABC, show=1):
    Var = V()
    if ABC in Var: return
    (A, B, C) = map(str, list(ABC))
    if (A not in Var) and \
       (B not in Var) and \
       (C not in Var):        
        value[A] = point.rand()
        value[B] = point.rand()        
        value[A].name = A
        value[B].name = B
        
        d = line.convertSegment([segment.Segment([value[A], value[B]])])
        point_C = point.combine_1([value[A], d])

        while not triangle.isTamGiac(value[A], value[B], point_C):
            value[A] = point.rand()
            value[B] = point.rand()        
            value[A].name = A
            value[B].name = B
            
            d = line.convertSegment([segment.Segment([value[A], value[B]])])
            point_C = point.combine_1([value[A], d])
        
        point_C.name = C        
        value[C] = point_C        
        tgABC = triangle.Triangle([value[A], value[B], value[C], ABC])
        value[ABC] = tgABC
        if (show == 1):
            tgABC.draw()
        Goc(B + A + C)
        return tgABC
    TamGiac(ABC)

def TamGiacCan(ABC, show=1):
    Var = V()
    if ABC in Var: return
    (A, B, C) = map(str, list(ABC))
    if (A not in Var) and \
       (B not in Var) and \
       (C not in Var):        
        value[B] = point.rand()
        value[B].name = B
        value[C] = point.rand()
        value[C].name = C
        
        d = line.duongTrungTruc([value[B], value[C]])
        value[A] = point.onLine([d])
        value[A].name = A
        
        tgABC = triangle.Triangle([value[A], value[B], value[C], ABC])
        value[ABC] = tgABC
        if show == 1:
            tgABC.draw()
        return tgABC
    TamGiac(ABC)

def TamGiacVuongCan(ABC, show=1):
    Var = V()
    if ABC in Var: return
    (A, B, C) = map(str, list(ABC))
    if (A not in Var) and \
       (B not in Var) and \
       (C not in Var):        
        value[B] = point.rand()
        value[B].name = B
        value[C] = point.rand()
        value[C].name = C
        
        d = line.duongTrungTruc([value[B], value[C]])

        M = point.center([value[B], value[C]])
        dis = mathfunctions.distance([value[B], value[C]])
        c = circle.Circle([M, dis / 2])        
        
        value[A] = point.intersect_line_circle([d, c])[0]
        value[A].name = A
        
        tgABC = triangle.Triangle([value[A], value[B], value[C], ABC])
        value[ABC] = tgABC
        if show == 1:
            tgABC.draw()
        return tgABC
    TamGiac(ABC)

def TamGiacDeu(ABC):
    Var = V()
    if ABC in Var: return
    (A, B, C) = map(str, list(ABC))
    if (A not in Var) and \
       (B not in Var) and \
       (C not in Var):        
        value[B] = point.rand()
        value[B].name = B
        value[C] = point.rand()
        value[C].name = C

        dis = mathfunctions.distance([value[B], value[C]])
        c1 = circle.Circle([value[B], dis])
        c2 = circle.Circle([value[C], dis])
        
        value[A] = point.intersect_two_circles([c1, c2])[0]
        value[A].name = A
        
        tgABC = triangle.Triangle([value[A], value[B], value[C], ABC])
        value[ABC] = tgABC
        tgABC.draw()
        return
    TamGiac(ABC)

def TuGiac(ABCD):
    Var = V()
    if ABCD in Var: return
    (A, B, C, D) = map(str, list(ABCD))
    if (A not in Var) and \
       (B not in Var) and \
       (C not in Var) and \
       (D not in Var):

        tg = triangle.rand()
        pA = tg.A
        pB = tg.B
        pC = tg.C

        vBA = vector.make_from_two_points(pB, pA)
        vBC = vector.make_from_two_points(pB, pC)
        r1 = ray.Ray([pB, vBA])
        r2 = ray.Ray([pB, vBC])
        angl = angle.Angle([r1, r2])
        pD = point.insideAngle2([angl])
        
        pA.name = A
        pB.name = B
        pC.name = C
        pD.name = D
        value[A] = pA
        value[B] = pB
        value[C] = pC
        value[D] = pD

        tgABCD = fourangle.Fourangle([pA, pB, pC, pD, ABCD])
        value[ABCD] = tgABCD
        tgABCD.draw()

def HinhThang(ABCD):
    Var = V()
    if ABCD in Var: return
    (A, B, C, D) = map(str, list(ABCD))

    if (A not in Var) and \
       (B not in Var) and \
       (C not in Var) and \
       (D not in Var):    
        pD = point.rand()
        dis = random.randint(4, 8)
        pC = point.combine_3([pD, dis])
        DC = segment.Segment([pD, pC])
        dDC = line.convertSegment([DC])
        ratio1 = random.random() * 0.2
        ratio2 = 0.5 + random.random() * 0.5
        print(ratio1, ' ', ratio2)
        M = point.distanceRatio([DC, ratio1])
        N = point.distanceRatio([DC, ratio2])
        d1 = line.combine_1([M, dDC])
        
        pA = point.onLine([d1])
                
        d2 = line.combine_2([pA, dDC])
        d1 = line.combine_1([N, dDC])
        pB = point.intersection([d1, d2])

        pA.name = A
        pB.name = B
        pC.name = C
        pD.name = D

        value[A] = pA
        value[B] = pB
        value[C] = pC
        value[D] = pD        

        tgABCD = fourangle.Fourangle([pA, pB, pC, pD, ABCD])
        value[ABCD] = tgABCD
        tgABCD.draw()

def HinhThangCan(ABCD):
    Var = V()
    if ABCD in Var: return
    (A, B, C, D) = map(str, list(ABCD))

    if (A not in Var) and \
       (B not in Var) and \
       (C not in Var) and \
       (D not in Var):    
        pD = point.rand()
        dis = random.randint(4, 8)
        pC = point.combine_3([pD, dis])
        DC = segment.Segment([pD, pC])
        dDC = line.convertSegment([DC])
        r = random.random()
        ratio1 = r * 0.5
        ratio2 = 1 - r * 0.5
        print(ratio1, ' ', ratio2)
        M = point.distanceRatio([DC, ratio1])
        N = point.distanceRatio([DC, ratio2])
        d1 = line.combine_1([M, dDC])
        
        pA = point.onLine([d1])
                
        d2 = line.combine_2([pA, dDC])
        d1 = line.combine_1([N, dDC])
        pB = point.intersection([d1, d2])

        pA.name = A
        pB.name = B
        pC.name = C
        pD.name = D

        value[A] = pA
        value[B] = pB
        value[C] = pC
        value[D] = pD        

        tgABCD = fourangle.Fourangle([pA, pB, pC, pD, ABCD])
        value[ABCD] = tgABCD
        tgABCD.draw()

def HinhThangVuong(ABCD):
    Var = V()
    if ABCD in Var: return
    (A, B, C, D) = map(str, list(ABCD))

    if (A not in Var) and \
       (B not in Var) and \
       (C not in Var) and \
       (D not in Var):
        ADB = A + D + B
        tri = TamGiacVuong(ADB, show=0)
        pA = tri.A
        pB = tri.B
        pD = tri.C

        vAB = vector.make_from_two_points(pA, pB)
        r = random.random()
        pC = point.Point([pD.x + (1 + r) * vAB.a, pD.y + (1 + r) * vAB.b])
        
        pA.name = A
        pB.name = B
        pC.name = C
        pD.name = D

        value[A] = pA
        value[B] = pB
        value[C] = pC
        value[D] = pD        

        tgABCD = fourangle.Fourangle([pA, pB, pC, pD, ABCD])
        value[ABCD] = tgABCD
        tgABCD.draw()

def HinhBinhHanh(ABCD):
    Var = V()
    if ABCD in Var: return
    (A, B, C, D) = map(str, list(ABCD))

    if (A not in Var) and \
       (B not in Var) and \
       (C not in Var) and \
       (D not in Var):
        ADB = A + D + B
        tri = TamGiac(ADB, show=0)
        pA = tri.A
        pB = tri.B
        pD = tri.C
        
        vAB = vector.make_from_two_points(pA, pB)
        pC = point.Point([pD.x + vAB.a, pD.y + vAB.b])
        
        pA.name = A
        pB.name = B
        pC.name = C
        pD.name = D

        value[A] = pA
        value[B] = pB
        value[C] = pC
        value[D] = pD        

        tgABCD = fourangle.Fourangle([pA, pB, pC, pD, ABCD])
        value[ABCD] = tgABCD
        tgABCD.draw()

def HinhThoi(ABCD):
    Var = V()
    if ABCD in Var: return
    (A, B, C, D) = map(str, list(ABCD))

    if (A not in Var) and \
       (B not in Var) and \
       (C not in Var) and \
       (D not in Var):
        ADB = A + D + B
        tri = TamGiacCan(ADB, show=0)
        pA = tri.A
        pB = tri.B
        pD = tri.C
        
        M = point.center([pB, pD])
        pC = point.Point([2 * M.x - pA.x, 2 * M.y - pA.y])
        
        pA.name = A
        pB.name = B
        pC.name = C
        pD.name = D

        value[A] = pA
        value[B] = pB
        value[C] = pC
        value[D] = pD        

        tgABCD = fourangle.Fourangle([pA, pB, pC, pD, ABCD])

        ganHoanVi(ABCD, tgABCD)

        #value[ABCD] = tgABCD
        
        tgABCD.draw()

def HinhVuong(ABCD):
    Var = V()
    if ABCD in Var: return
    (A, B, C, D) = map(str, list(ABCD))

    if (A not in Var) and \
       (B not in Var) and \
       (C not in Var) and \
       (D not in Var):
        ADB = A + D + B
        tri = TamGiacVuongCan(ADB, show=0)
        pA = tri.A
        pB = tri.B
        pD = tri.C
        
        M = point.center([pB, pD])
        pC = point.Point([2 * M.x - pA.x, 2 * M.y - pA.y])
        
        pA.name = A
        pB.name = B
        pC.name = C
        pD.name = D

        value[A] = pA
        value[B] = pB
        value[C] = pC
        value[D] = pD        

        tgABCD = fourangle.Fourangle([pA, pB, pC, pD, ABCD])
        value[ABCD] = tgABCD
        tgABCD.draw()

def HinhChuNhat(ABCD):
    Var = V()
    if ABCD in Var: return
    (A, B, C, D) = map(str, list(ABCD))

    if (A not in Var) and \
       (B not in Var) and \
       (C not in Var) and \
       (D not in Var):
        ADB = A + D + B
        tri = TamGiacVuong(ADB, show=0)
        pA = tri.A
        pB = tri.B
        pD = tri.C
        
        M = point.center([pB, pD])
        pC = point.Point([2 * M.x - pA.x, 2 * M.y - pA.y])
        
        pA.name = A
        pB.name = B
        pC.name = C
        pD.name = D

        value[A] = pA
        value[B] = pB
        value[C] = pC
        value[D] = pD        

        tgABCD = fourangle.Fourangle([pA, pB, pC, pD, ABCD])
        value[ABCD] = tgABCD
        tgABCD.draw()

# [O; R]
# R is a float of number
def DuongTron(OR):
    Var = V()
    O = OR[0]
    R = OR[1]
    pO = None
    if O not in Var:
        pO = point.rand()
        pO.name = O
        value[O] = pO
    else:
        pO = value[O]
    C = circle.Circle([pO, R])
    C.draw()

def Goc(ABC):
    Var = V()
    (A, B, C) = map(str, list(ABC))
    if (A not in Var) and \
       (B not in Var) and \
       (C not in Var):
        pA = point.rand()
        pB = point.rand()
        pC = point.rand()
        (pA.name, pB.name, pC.name) = (A, B, C)
        (value[A], value[B], value[C]) = (pA, pB, pC)

    if (A not in Var) or \
       (B not in Var) or \
       (C not in Var): return

    vBA = vector.make_from_two_points(value[B], value[A])
    vBC = vector.make_from_two_points(value[B], value[C])

    size1 = vector.size(vBA)
    size2 = vector.size(vBC)
    
    r1 = 0.5 / size1
    r2 = 0.5 / size2
    
    pA = point.Point([value[B].x + vBA.a * r1, value[B].y + vBA.b * r1])
    pC = point.Point([value[B].x + vBC.a * r2, value[B].y + vBC.b * r2])
    pA.drawn = pC.drawn = True
    if (mathfunctions.angle_between_two_vector(vBA, vBC) - math.pi / 2) < e:
        M = point.center([pA, pC])
        pBC = point.Point([2 * M.x - value[B].x, 2 * M.y - value[B].y])
        pBC.drawn = True
        s1 = segment.Segment([pBC, pC])
        s2 = segment.Segment([pBC, pA])
        s1.draw()
        s2.draw()
        
def DoanPhanGiac(E, ABC):
    Var = V()
    (A, B, C) = map(str, list(ABC))

    if E in Var: return
    
    if (A not in Var) or \
       (B not in Var) or \
       (C not in Var):
        return 
    
    vBA = vector.make_from_two_points(value[B], value[A])
    vBC = vector.make_from_two_points(value[B], value[C])

    size1 = vector.size(vBA)
    size2 = vector.size(vBC)
    
    r1 = 0.5 / size1
    r2 = 0.5 / size2
    
    pA = point.Point([value[B].x + vBA.a * r1, value[B].y + vBA.b * r1])
    pC = point.Point([value[B].x + vBC.a * r2, value[B].y + vBC.b * r2])
    pA.drawn = pC.drawn = True

    M = point.center([pA, pC])
    vBM = vector.make_from_two_points(value[B], M)

    r = 10
    pE = point.Point([value[B].x + vBM.a * r, value[B].y + vBM.b *  r])
    pE.name = E
    value[E] = pE

    BE = segment.Segment([value[B], pE, B + E])
    value[B + E] = BE
    BE.draw()
    

def TiaPhanGiac(Oz, Ox, Oy):
    Var = V()
    O = Oz[0]
    
    if Oz in Var: return
    
    if (Ox not in Var) or \
       (Oy not in Var):
        return 

    if O not in Var: return

    x = Ox[1]
    y = Oy[1]
    z = Oz[1]
    
    vx = value[x]
    vy = value[y]

    pO = value[O]

    size1 = vector.size(vx)
    size2 = vector.size(vy)
    
    r1 = 0.5 / size1
    r2 = 0.5 / size2
    
    pA = point.Point([pO.x + vx.a * r1, pO.y + vx.b * r1])
    pC = point.Point([pO.x + vy.a * r2, pO.y + vy.b * r2])
    pA.drawn = pC.drawn = True

    M = point.center([pA, pC])
    vz = vector.make_from_two_points(pO, M)
    vz.name = z
    value[z] = vz
    rayOz = ray.Ray([pO, vz, Oz])
    rayOz.draw()
    value[Oz] = rayOz
    
############################################################
############################################################
########################### Minh ###########################
############################################################
############################################################

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


def ThuocDuongTron(a):
    Var = V()
    if a[1] not in Var: return
    C1 = value[a[1]]
    M = point.onCircle([C1])
    M.name = a[0]
    value[a[0]] = M
    M.draw()
#   a = ["M","(O,R)"]
def NgoaiDuongTron(a):
    Var = V()
    if a[1] not in Var: return
    if a[0] in Var: return 
    C1 = value[a[1]]
    Temp = point.onCircle([C1])
    M = point.pos_point([C1.O,Temp])
    M.name = a[0]
    value[a[0]] = M
    M.draw()
# Vd Tieptuyen(["AB","C1")
def TiepTuyen(a):
    Var = V()
    if a[1] not  in Var: return
    if a[0][0]  in Var: return
    if a[0][1] in Var: return 
    C1 = value[a[1]]
    value[a[0][0]] = point.onCircle([C1])
    value[a[0][0]].name = a[0][0]
    value[a[0][0]].draw()
    S1 = segment.Segment([C1.O,value[a[0][0]]])
    Line1 = line.convertSegment([S1])
    Line2 = line.combine_1([value[a[0][0]],Line1])
    value[a[0][1]] =point.onLine([Line2])
    value[a[0][1]].name = a[0][1]
    value[a[0][1]].draw()
    value[a[0]] = segment.Segment([value[a[0][0]],value[a[0][1]]])
    value[a[0]].name = a[0]
    value[a[0]].draw()
#vd Daycung(["AC","C1"'
def DayCung(a):
    Var = V()
    if a[1] not  in Var: return
    if a[0][0]  in Var: return
    if a[0][1] in Var: return
    C1 = value[a[1]]
    value[a[0][0]] = point.onCircle([C1])
    value[a[0][1]] = point.onCircle([C1])
    while(value[a[0][0]] == value[a[0][1]]):
        value[a[0][1]] = point.onCircle([C1])
    value[a[0][0]].name = a[0][0]
    value[a[0][0]].draw()
    value[a[0][1]].name = a[0][1]
    value[a[0][1]].draw()
    S1 = segment.Segment([value[a[0][0]],value[a[0][1]]])
    value[a[0]] = S1
    value[a[0]].name = a[0]
    value[a[0]].draw()
# DuongKinh((["AC","C1")
def DuongKinh(a):
    Var = V()
    if a[1] not in Var: return
    if a[0][0]  in Var: return
    if a[0][1] in Var: return
    C1 = value[a[1]]
    value[a[0][0]] = point.onCircle([C1])
    value[a[0][0]].name = a[0][0]
    value[a[0][0]].draw()
    value[a[0][1]] = point.pos_point([value[a[0][0]],C1.O])
    value[a[0][1]].name = a[0][1]
    value[a[0][1]].draw()
    S1 = segment.Segment([value[a[0][0]],value[a[0][1]]])
    value[a[0]] = S1
    value[a[0]].name = a[0]
    value[a[0]].draw()
#vd GiaoDiemDuongTron_Doan("M","EF","C1")
def GiaoDiemDuongTron_Doan(a):
    Var = V()
    if a[2] not in Var: return
    if a[1][0] in Var: return
    if a[1][1] in Var: return
    if a[0] in Var: return
    C1 = value[a[2]]
    value[a[0]] = point.onCircle([C1])
    value[a[0]].name = a[0]
    value[a[0]].draw()
    S1 = segment.Segment([C1.O,value[a[0]]])
    Line1 = line.convertSegment([S1])
    Line2 = line.combine_1([value[a[0]],Line1])
    value[a[1][0]] =point.onLine([Line2])
    value[a[1][0]].name = a[1][0]
    value[a[1][0]].draw()
    value[a[1][1]] = point.pos_point([value[a[1][0]],value[a[0][0]]])
    value[a[1][1]].name = a[1][1]
    value[a[1][1]].draw()
    value[a[1]]= segment.Segment([value[a[1][0]],value[a[1][1]]])
    value[a[1]].name= a[1]
    value[a[1]].draw()

############################################################
############################################################
########################## Trang ###########################
############################################################
############################################################

def DiemNamGiuaHaiDiem(MNP):
    Var = V()
    if MNP in Var: return
    M = MNP[0]
    N = MNP[1]
    P = MNP[2]
    if N not in Var:
        value[N] = point.rand()
        value[N].name = N
        value[N].draw()
    if P not in Var:
        value[P] = point.rand()
        value[P].name = P
        value[P].draw()
    seg = segment.Segment([value[N], value[P]])
    value[M] = point.onSegment([seg])
    value[M].name = M
    value[M].draw()

def BaDiemThangHang(SRA):
    Var = V()
    if SRA in Var: return
    S = SRA[0]
    R = SRA[1]
    A = SRA[2]
    if S not in Var:
        value[S] = point.rand()
        value[S].name = S
        value[S].draw()
    if R not in Var:
        value[R] = point.rand()
        value[R].name = R
        value[R].draw()
    seg = segment.Segment([value[S], value[R]])
    ln = line.convertSegment([seg])
    value[A] = point.onLine([ln])
    value[A].name = A
    value[A].draw()

def BaDiemKhongThangHang(SRA):
    Var = V()
    if SRA in Var: return
    S = SRA[0]
    R = SRA[1]
    A = SRA[2]
    if S not in Var:
        value[S] = point.rand()
        value[S].name = S
        value[S].draw()
    if R not in Var:
        value[R] = point.rand()
        value[R].name = R
        value[R].draw()
    value[A] = point.combine_triangle([value[S], value[R]])
    value[A].name = A
    value[A].draw()

def DiemThuocDuongThang(M,d):
    Var = V()
    if (M in Var) and (d in Var): return
    if d not in Var:
        value[d] = line.rand()
        value[d].name = d
        value[d].draw()
    value[M] = point.onLine([value[d]])
    value[M].name = M
    value[M].draw()

def DiemKhongThuocDuongThang(M, d):
    Var = V()
    if M in  Var and d in Var: return
    if d not in Var:
        value[d] = line.rand()
        value[d].name = d
        value[d].draw()
    Temp = point.onLine([value[d]])
    Temp1 = point.onLine([value[d]])
    value[M] = point.combine_triangle([Temp, Temp1])
    value[M].name = M
    value[M].draw()

def DuongCaoTuGiac(H, ABCD):
    Var = V()

    if H in Var: return
    if ABCD not in Var: return
    
    (A, B, C, D) = map(str, list(ABCD))
    
    dCD = line.convertSegment([segment.Segment([value[C], value[D]])])
                              
    d = line.combine_1([value[A], dCD])
                              
    value[H] = point.intersection([dCD, d])
    value[H].name = H
                              
    AH = segment.Segment([value[A], value[H]])
    AH.name = A + H

    value[AH.name] = AH

    CH = segment.Segment([value[C], value[H]])
    CH.name = C + H
    DH = segment.Segment([value[D], value[H]])
    DH.name = D + H

    Goc(A + H + C)

    CH.draw()
    DH.draw()
    AH.draw()

def DiemThuocTia(M, Ox):
    Var = V()
    if M in Var: return
                              
    O = Ox[0]
    x = Ox[1]

    if O not in Var:
        value[O] = point.rand()
        value[O].name = O
    if x not in Var:
        value[x] = vector.rand()
        value[x].name = x

    rayOx = ray.Ray([value[O], value[x]])
    segOx = segment.convertRay([rayOx])
                              
    value[M] = point.onSegment([segOx])
    value[M].name = M
    value[M].draw()
    rayOx.draw()

def GiaoDiemHaiTia(M, Ox, Ty):
    Var = V()
    if M in Var: return
    O = Ox[0]
    x = Ox[1]
    T = Ty[0]
    y = Ty[1]
    # neu O chua co, thi tao 
    if O not in Var:
        value[O] = point.rand()
        value[O].name = O
    if x not in Var:
        value[x] = vector.rand()
        value[x].name = x
    if T not in Var:
        value[T] = point.rand()
        value[T].name = T
    if y not in Var:
        value[y] = vector.rand()
        value[y].name = y

    if Ox not in Var:
        rayOx = ray.Ray([value[O], value[x]])
    else:
        rayOx = value[Ox]
    if Ty not in Var:
        rayTy = ray.Ray([value[T], value[y]])
    else:
        rayTy = value[Ty]

    lnOx = line.convertRay([rayOx])
    lnTy = line.convertRay([rayTy])

    pM = point.intersection([lnOx, lnTy])    

    if mathfunctions.checkInRay(pM, rayOx) and \
       mathfunctions.checkInRay(pM, rayTy):    
        value[M] = pM
        value[M].name = M
        value[M].draw()
        rayOx.inscreaseSize(pM)
        rayTy.inscreaseSize(pM)

    rayOx.draw()
    rayTy.draw()
    
def GiaoDiemTiaDoan(M, Ox, AB):
    Var = V()
    if Ox in Var and AB in Var: return
    (O, x) = map(str, list(Ox))
    (A, B) = map(str, list(AB))
    if O not in Var:
        value[O] = point.rand()
        value[O].name = O
    if x not in Var:
        value[x] = vector.rand()
        value[x].name = x
    if A not in Var:
        value[A] = point.rand()
        value[A].name = A
    if B not in Var:
        value[B] = point.rand()
        value[B].name = B
    ray_Ox = ray.Ray([value[O], value[x]])
    seg_AB = segment.Segment([value[A], value[B]])
    ln_Ox = line.convertRay([ray_Ox])
    ln_AB = line.convertSegment([seg_AB])
    value[M] = point.intersection([ln_Ox, ln_AB])
    value[M].name = M
    seg_Ox = segment.convertRay([ray_Ox])
    if mathfunctions.intersect(value[M], [seg_Ox , seg_AB]) == True:
        value[M].draw()
    ray_Ox.draw()
    seg_AB.draw()

def HaiDoanThangSongSong(AB, CD):
    Var = V()
    if AB in Var and CD in Var: return
    (A, B) = map(str, list(AB))
    (C, D) = map(str, list(CD))
    if A not in Var:
        value[A] = point.rand()
        value[A].name = A
    if B not in Var:
        value[B] = point.rand()
        value[B].name = B
    if C not in Var:
        value[C] = point.rand()
        value[C].name = C
    seg_AB = segment.Segment([value[A], value[B]])
    value[AB] = seg_AB
    ln_AB = line.convertSegment([seg_AB])
    ln_CD = line.combine_2([value[C], ln_AB])
    value[D] = point.onLine([ln_CD])
    value[D].name = D
    seg_CD = segment.Segment([value[C], value[D]])
    value[CD] = seg_CD
    seg_AB.draw()
    seg_CD.draw()

def HaiDoanThangVuongGoc(AB, CD):
    Var = V()
    if AB in Var and CD in Var: return
    (A, B) = map(str, list(AB))
    (C, D) = map(str, list(CD))
    if A not in Var:
        value[A] = point.rand()
        value[A].name = A
    if B not in Var:
        value[B] = point.rand()
        value[B].name = B
    seg_AB = segment.Segment([value[A], value[B]])
    value[AB] = seg_AB
    lnAB = line.convertSegment([seg_AB])
    value[C] = point.combine_triangle([value[A], value[B]])
    value[C].name = C
    lnCD = line.combine_1([value[C], lnAB])
    value[D] = point.onLine([lnCD])
    value[D].name = D
    seg_CD = segment.Segment([value[C], value[D]])
    value[CD] = seg_CD
    seg_AB.draw()
    seg_CD.draw()
        
def HaiDoanThangBangNhau(AB, CD):
    Var = V()
    if AB in Var and CD in Var: return
    (A, B) = map(str, list(AB))
    (C, D) = map(str, list(CD))
    if A not in Var:
        value[A] = point.rand()
        value[A].name = A
    if B not in Var:
        value[B] = point.rand()
        value[B].name = B
    if C not in Var:
        value[C] = point.rand()
        value[C].name = C
    kc_AB = mathfunctions.distance([value[A], value[B]])
    value[D] = point.combine_3([value[C], kc_AB])
    value[D].name = D
    seg_AB = segment.Segment([value[A], value[B]])
    value[AB] = seg_AB
    seg_CD = segment.Segment([value[C], value[D]])
    value[CD] = seg_CD
    seg_AB.draw()
    seg_CD.draw()

def GiaoDiemHaiDoan(E, AB, CD):
    Var = V()
    if AB in Var and CD in Var: return
    (A, B) = map(str, list(AB))
    (C, D) = map(str, list(CD))
    if A not in Var:
        value[A] = point.rand()
        value[A].name = A
    if B not in Var:
        value[B] = point.rand()
        value[B].name = B
    if C not in Var:
        value[C] = point.rand()
        value[C].name = C
    if D not in Var:
        value[D] = point.rand()
        value[D].name = D
    seg_AB = segment.Segment([value[A], value[B]])
    value[AB] = seg_AB
    seg_CD = segment.Segment([value[C], value[D]])
    value[CD] = seg_CD
    ln_AB = line.convertSegment([seg_AB])
    ln_CD = line.convertSegment([seg_CD])
    value[E] = point.intersection([ln_AB, ln_CD])
    value[E].name = E
    if mathfunctions.intersect(value[E], [seg_AB , seg_CD]) == True:
        value[E].draw()
    seg_AB.draw()
    seg_CD.draw()
        
def TiaNamGiuaHaiTia(Oxzy):
    Var = V()
    if Ox in Var and Oy in Var: return
    (O, x, z, y) = map(str, list(Oxzy))
    if O not in Var:
        value[O] = point.rand()
        value[O].name = O
    if x not in Var:
        value[x] = vector.rand()
        value[x].name = x
    if y not in Var:
        value[y] = vector.rand()
        value[y].name = y
    ray_Ox = ray.Ray([value[O], value[x]])
    value[Ox] = ray_Ox
    ray_Oy = ray.Ray([value[O], value[y]])
    value[Oy] = ray_Oy
    angle_Oxy = angle.Angle([ray_Ox, ray_Oy])
    pn = point.insideAngle([angle_Oxy])
    value[z] = vector.make_from_two_points(value[O], pn)
    value[z].name = z
    ray_Oz = ray.Ray([value[O], value[z]])

    ray_Ox.draw()
    ray_Oy.draw()
    ray_Oz.draw()

def HaiTiaDoiNhau(Oxy):
    Var = V()
    if Ox in Var and Oy in Var: return
    (O, x, y) = map(str, list(Oxy))
    if O not in Var:
        value[O] = point.rand()
        value[O].name = O
    if x not in Var:
        value[x] = vector.rand()
        value[x].name = x
    ray_Ox = ray.Ray([value[O], value[x]])
    value[Ox] = ray_Ox
    seg_Ox = segment.convertRay([ray_Ox])
    pn_Ox = point.onSegment([seg_Ox])
    pn_Oy = point.pos_point([value[O], pn_Ox])
    value[y] = vector.make_from_two_points(pn_Oy, value[O])
    value[y].name = y
    ray_Oy = ray.Ray([value[O], value[y]])
    value[Oy] = ray_Oy
    ray_Ox.draw()
    ray_Oy.draw()








