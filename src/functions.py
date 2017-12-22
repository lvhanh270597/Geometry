
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
def Doan(L, show=1):
    AB = L[0]
    Var = V()
    if AB in Var:   return value[AB]
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
    if show == 1: seg.draw()
    return seg

def Duong(L, show=1):
    dAB = L[0]
    AB = dAB[1 :]
    doanAB = Doan([AB], show = 0)
    duongAB = line.convertSegment([doanAB])
    if show == 1: duongAB.draw()
    value[dAB] = duongAB
    return duongAB

def DuongTrungTruc(L):
    AB = L[0]
    Var = V()
    if AB in Var: return value[AB]
    (A, B) = list(AB)
    ln_AB = line.duongTrungTruc([value[A], value[B]])
    ln_AB.draw()
    return ln_AB

# doan trung binh MN cua tam giac ABC, tai dinh A
def DoanTrungBinh(L):
    MN = L[0]
    ABC = L[1]
    AA = L[2]

    (A, B, C) = list(ABC)
    (D, E, F) = list(ABC)

    pA = value[A]
    pB = value[B]
    pC = value[C]
    
    if AA == E:
        (pA, pB, pC) = (value[E], value[D], value[F])
    if AA == F:
        (pA, pB, pC) = (value[F], value[E], value[D])
    
    Var = V()
    if MN in Var: return
    
    (M, N) = list(MN)
    
    ln_TB = line.duongTrungBinh([value[ABC], pA])
    
    seg_AB = segment.Segment([pA, pB])
    ln_AB = line.convertSegment([seg_AB])
    seg_AC = segment.Segment([pA, pC])
    ln_AC = line.convertSegment([seg_AC])
    value[M] = point.intersection([ln_TB, ln_AB])
    value[M].name = M
    value[N] = point.intersection([ln_TB, ln_AC])
    value[N].name = N
    seg_MN = segment.Segment([value[M], value[N]])
    value[MN] = seg_MN
    seg_MN.draw()
    

def TamGiac(L, show=1):
    ABC = L[0]
    Var = V()
    if ABC in Var: return value[ABC]
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
        ganHoanVi(ABC, tgABC)
        #value[ABC] = tgABC
        if (show == 1):
            tgABC.draw()
        return tgABC
    if (A in Var) and \
       (B in Var) and \
       (C in Var):
        tgABC = triangle.Triangle([value[A], value[B], value[C], ABC])
        #value[ABC] = tgABC
        ganHoanVi(ABC, tgABC)
        if (show == 1):
            tgABC.draw()
        return tgABC
        
def TamGiacVuong(L, show=1):    
    ABC = L[0]
    A = L[1]

    (D, E, F) = list(ABC)
    if A == E: ABC = E + D + F
    if A == F: ABC = F + E + D
    
    Var = V()
    if ABC in Var: return
    (A, B, C) = map(str, list(ABC))
    if (A not in Var) and \
       (B not in Var) and \
       (C not in Var):        
        value[A] = point.Point([random.randint(-8, -3), -2, A])        
        value[B] = point.Point([value[A].x + random.randint(8, 12), -2, B])        
        
        d = line.convertSegment([segment.Segment([value[A], value[B]])])
        point_C = point.combine_1([value[A], d])
        while not triangle.isTamGiac(value[A], value[B], point_C):
            point_C = point.combine_1([value[A], d])
        
        point_C.name = C        
        value[C] = point_C        
        tgABC = triangle.Triangle([value[A], value[B], value[C], ABC])
        ganHoanVi(ABC, tgABC)
        #value[ABC] = tgABC
        if (show == 1):
            tgABC.draw()
        Goc(B + A + C)
        return tgABC
    TamGiac(ABC)

def TamGiacCan(L, show=1):    
    ABC = L[0]
    A = L[1]

    (D, E, F) = list(ABC)
    if A == E: ABC = E + D + F
    if A == F: ABC = F + E + D

    Var = V()
    
    if ABC in Var: return
    (A, B, C) = map(str, list(ABC))
    if (A not in Var) and \
       (B not in Var) and \
       (C not in Var):        
        value[B] = point.Point([random.randint(-8, -3), -2, B])        
        value[C] = point.Point([value[B].x + random.randint(8, 12), -2, C])        
        
        d = line.duongTrungTruc([value[B], value[C]])
        d2 = line.convertSegment([segment.Segment([value[B], value[C]])])
        value[A] = point.onLine([d])
        dist = mathfunctions.distance_line([value[A], d2]) 
        while (dist < 3) or (dist > 10):
            value[A] = point.onLine([d])
            dist = mathfunctions.distance_line([value[A], d2])         
        
        value[A].name = A
        
        tgABC = triangle.Triangle([value[A], value[B], value[C], ABC])
        value[ABC] = tgABC
        if show == 1:
            tgABC.draw()
        return tgABC
    TamGiac(ABC)

def TamGiacVuongCan(L, show=1):    
    ABC = L[0]
    A = L[1]

    (D, E, F) = list(ABC)
    if A == E: ABC = E + D + F
    if A == F: ABC = F + E + D

    Var = V()
    
    if ABC in Var: return
    (A, B, C) = map(str, list(ABC))
    if (A not in Var) and \
       (B not in Var) and \
       (C not in Var):        
        value[B] = point.Point([random.randint(-8, -3), -2, B])        
        value[C] = point.Point([value[B].x + random.randint(8, 12), -2, C])        
        
        '''value[B] = point.rand()
        value[B].name = B
        value[C] = point.rand()
        value[C].name = C'''
        
        d = line.duongTrungTruc([value[B], value[C]])

        M = point.center([value[B], value[C]])
        dis = mathfunctions.distance([value[B], value[C]])
        c = circle.Circle([M, dis / 2])        
        
        value[A] = point.intersect_line_circle([d, c])[random.randint(0, 1)]
        value[A].name = A
        
        tgABC = triangle.Triangle([value[A], value[B], value[C], ABC])
        ganHoanVi(ABC, tgABC)
        #value[ABC] = tgABC
        if show == 1:
            tgABC.draw()

        Goc(B + A + C)
            
        return tgABC
    TamGiac(ABC)

def TamGiacDeu(L, show = 1):
    ABC = L[0]
    Var = V()
    if ABC in Var: return
    (A, B, C) = map(str, list(ABC))
    if (A not in Var) and \
       (B not in Var) and \
       (C not in Var):        
        value[B] = point.Point([random.randint(-8, -3), -2, B])        
        value[C] = point.Point([value[B].x + 8, -2, C])        

        dis = mathfunctions.distance([value[B], value[C]])
        c1 = circle.Circle([value[B], dis])
        c2 = circle.Circle([value[C], dis])
        
        value[A] = point.intersect_two_circles([c1, c2])[random.randint(0, 1)]
        value[A].name = A
        
        tgABC = triangle.Triangle([value[A], value[B], value[C], ABC])
        ganHoanVi(ABC, tgABC)
        #value[ABC] = tgABC
        tgABC.draw()
        return
    TamGiac(ABC)

def TrungTuyen(L):
    AH = L[0]
    ABC = L[1]

    (A, H) = list(AH)
    (D, E, F) = list(ABC)
    if A == E: ABC = E + F + D
    if A == F: ABC = F + D + E
    
    (A, B, C) = list(ABC)
    (pA, pB, pC) = (value[A], value[B], value[C])
    pH = point.center([pB, pC])
    pH.name = H
    value[H] = pH
    Doan([A + H])
    pH.draw()
    return pH
    

def SmallTamGiacCan(ABC):
    Var = V()
    if ABC in Var: return
    (A, B, C) = map(str, list(ABC))
    if (A not in Var) and \
       (B not in Var) and \
       (C not in Var):        
        value[B] = point.Point([-8, -2, B])        
        value[C] = point.Point([value[B].x + 15, -2, C])        
        
        d = line.duongTrungTruc([value[B], value[C]])
        d2 = line.convertSegment([segment.Segment([value[B], value[C]])])
        value[A] = point.onLine([d])        
        dist = mathfunctions.distance_line([value[A], d2]) 
        while (dist < 3) or (dist > 6):
            value[A] = point.onLine([d])
            dist = mathfunctions.distance_line([value[A], d2])         
        
        value[A].name = A
        
        tgABC = triangle.Triangle([value[A], value[B], value[C], ABC])
        value[ABC] = tgABC
        return tgABC



# [O; R]
# R is a float of number
def DuongTron(OR):
    Var = V()
    O = OR[0]
    R = OR[1]
    print(R)
    print(O)
    pO = None
    if O not in Var:
        pO = point.rand()
        pO.name = O
        value[O] = pO
    else:
        pO = value[O]
    C = circle.Circle([pO, R])
    C.draw()

def DuongTronNgoaiTiep(L):
    Var = V()
    O = L[0]
    ABC = L[1]
    if ABC not in Var: return
    (A, B, C) = list(ABC)
    TamGiac([ABC])
    value[O] = circle.through_three([value[A], value[B], value[C]])
    value[O].name = O
    value[O].draw()
    
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
        
def DoanPhanGiac(L):    
    AH = L[0]
    ABC = L[1]

    (A, H) = list(AH)
    (D, E, F) = list(ABC)
    if A == D: ABC = E + D + F
    if A == F: ABC = E + F + D
    
    Var = V()
    (A, B, C) = map(str, list(ABC))

    if H in Var: return
    
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

    # determine duong phan giac
    pA = point.Point([value[B].x + vBA.a * r1, value[B].y + vBA.b * r1])
    pC = point.Point([value[B].x + vBC.a * r2, value[B].y + vBC.b * r2])
    pA.drawn = pC.drawn = True

    M = point.center([pA, pC])
    BM = segment.Segment([value[B], M])
    d = line.convertSegment([BM])

    AC = segment.Segment([value[A], value[C]])
    dAC = line.convertSegment([AC])
    # E = intersection
    pH = point.intersection([d, dAC])
    pH.name = H
    value[H] = pH

    BH = segment.Segment([value[B], pH, B + H])
    value[B + H] = BH
    BH.draw()
    


def QuaMotDiemVaSongSongVoiDuong(L):
    (P, L1, L2) = L
    Var = V()
    if L1 in Var: return
    if L2 not in Var: return        
    L = line.combine_2([value[P], value[L2]])
    value[L1] = L
    L.draw()

def QuaMotDiemVaSongSongVoiDoan(L):
    Var = V()
    
    (P, L1, S) = L
    
    if P not in Var: return
    if L1 in Var: return
    if S not in Var: value[S] = Doan([S])        
    
    ln = line.convertSegment([value[S]])    
    d = line.combine_2([value[P], ln])
    value[L1] = d
    d.draw()    

# L = [P, seg]
# duong thang d qua P va vuong goc voi seg

def QuaMotDiemVuongGocVoiDuong(L, show=1):
    Var = V()
    (P, L1, L2) = L
    if P not in Var: return
    if L2 not in Var: return
    d = line.combine_1([value[P], value[L2]])
    value[L1] = d
    if show == 1: d.draw()
    return d

def QuaMotDiemVuongGocVoiDoan(L, show=1):
    Var = V()
    (P, L1, S) = L
    if P not in Var: return       
    print(S)
    if S not in Var: value[S] = Doan([S])
    
    d2 = line.convertSegment([value[S]])
    d = line.combine_1([value[P], d2])
    value[L1] = d
    if show == 1: d.draw()
    return d
############################################################
############################################################
########################### Minh ###########################
############################################################
############################################################

# PHan Doan - Doan
# VD List A
# M, AB
def TrungDiem(L):
    Var = V()
    M = L[0]
    AB = L[1]
    (A, B) = list(AB)
    if A not in Var: return
    if B not in Var: return
    if AB not in Var: Doan([AB])
        
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

    if AB not in Var: value[AB] = Doan([AB])
    
    AB = value[AB]
    
    k = random.random()
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
    (A, B) = list(AB)
    (C, D) = list(CD)

    if M in Var: return
    if AB not in Var: value[AB] = Doan([AB])
    if CD not in Var: value[CD] = Doan([CD])
    
    d1 = line.convertSegment([segment.Segment([value[A], value[B]])])
    d2 = line.convertSegment([segment.Segment([value[C], value[D]])])
    pM = point.intersection([d1, d2])
    pM.name = M
    value[M]= pM
    if mathfunctions.intersect(value[M], [segment.Segment([value[A], value[B]]), \
                                          segment.Segment([value[C], value[D]])]) == False:
             seg_MA = segment.Segment([value[M], value[A]])
             seg_MC = segment.Segment([value[C], value[M]])
             seg_MB = segment.Segment([value[M], value[B]])
             seg_MD = segment.Segment([value[D], value[M]])
             seg_MA.draw()
             seg_MC.draw()
             seg_MB.draw()
             seg_MD.draw()
    pM.draw()

############################################################
############################################################
########################## Trang ###########################
############################################################
############################################################

def DiemNamGiuaHaiDiem(L):
    Var = V()
    
    M = L[0]
    NP = L[1]
    
    (N, P) = map(str, list(NP))
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

def DiemTrongTamGiac(L):
    O = L[0]
    ABC = L[1]
    Var = V()
    if O in Var: return
    value[O] = point.insideTriangle([value[ABC]])
    value[O].name = O
    value[O].draw()

def DiemNgoaiTamGiac(L):
    O = L[0]
    ABC = L[1]
    Var = V()
    if O in Var: return
    value[O] = point.outsideTriangle([value[ABC]])
    value[O].name = O
    value[O].draw()
    

def DiemThuocDuongThang(L):
    Var = V()
    M = L[0]
    d = L[1]
    if (M in Var) and (d in Var): return
    if d not in Var:
        value[d] = line.rand()
        value[d].name = d
        value[d].draw()
    value[M] = point.onLine([value[d]])
    value[M].name = M
    value[M].draw()        

def HaiDoanThangSongSong(L):
    Var = V()
    AB = L[1]
    CD = L[0]
    if AB in Var: return
    if CD in Var: return
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
    if D in Var: return
            
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

def HaiDoanThangVuongGoc(L):
    Var = V()
    CD = L[0]
    AB = L[1]
    if AB in Var: return
    if CD in Var: return
    (A, B) = map(str, list(AB))
    (C, D) = map(str, list(CD))
    if A not in Var:
        value[A] = point.rand()
        value[A].name = A
    if B not in Var:
        value[B] = point.rand()
        value[B].name = B
    if C not in Var:
        value[C] = point.combine_triangle([value[A], value[B]])
        value[C].name = C
    seg_AB = segment.Segment([value[A], value[B]])
    value[AB] = seg_AB
    lnAB = line.convertSegment([seg_AB])
    lnCD = line.combine_1([value[C], lnAB])
    value[D] = point.intersection([lnAB, lnCD])
    value[D].name = D
    seg_CD = segment.Segment([value[C], value[D]])
    value[CD] = seg_CD
    if mathfunctions.checkIntersect([value[D], seg_AB]) == False:
        seg_DA = segment.Segment([value[A], value[D]])
        seg_DA.draw()
    seg_AB.draw()
    seg_CD.draw()
        
def TrongTam(L):
    Var = V()
    E = L[0]
    ACK = L[1]
    if E in Var: return
    if ACK not in Var: return

    (A, C, K) = list(ACK)
    pn_B = point.center([value[C], value[K]])
    pn_D = point.center([value[A], value[K]])
    
    seg_AB = segment.Segment([value[A], pn_B])
    
    seg_CD = segment.Segment([value[C], pn_D])
    
    ln_AB = line.convertSegment([seg_AB])
    ln_CD = line.convertSegment([seg_CD])
    value[E] = point.intersection([ln_AB, ln_CD])
    value[E].name = E
    value[E].draw()
    ln_AB.draw()
    ln_CD.draw()

def DuongCaoTamGiac(L):
    AH = L[0]
    ABC = L[1]

    (A, H) = list(AH)
    (D, E, F) = list(ABC)
    if A == E: ABC = E + F + D
    if A == F: ABC = F + D + E
    
    Var = V()
    if H in Var: return
    (A, B, C) = list(ABC)
    if (A not in Var) or \
       (B not in Var) or \
       (C not in Var):
        return

    if ABC not in Var:
        tgABC = triangle.Triangle([value[A], value[B], value[C]])
        tgABC.draw()

    d1 = line.convertSegment([segment.Segment([value[B], value[C]])])
    d2 = line.combine_1([value[A], d1])

    pH = point.intersection([d1, d2])
    pH.name = H
    value[H] = pH

    AH = segment.Segment([value[A], pH])

    Goc(A + H + B)

    AH.draw()
    pH.draw()

    if not mathfunctions.checkInSegment(pH, \
                                         segment.Segment([value[B], value[C]])):
        BH = segment.Segment([value[B], value[H]])
        CH = segment.Segment([value[C], value[H]])
        BH.draw()
        CH.draw()
    return AH

def TrucTam(L):
    Var = V()
    H = L[0]
    ABC = L[1]
    
    if H in Var: return
    if ABC not in Var: return

    (A, B, C) = list(ABC)
    BC = B + C
    AC = A + C
    d1 = QuaMotDiemVuongGocVoiDoan([A, 'd' + str(random.random()), BC])
    d2 = QuaMotDiemVuongGocVoiDoan([B, 'd' + str(random.random()), AC])

    pH = point.intersection([d1, d2])
    pH.name = H
    value[H] = pH
    pH.draw()
    

##############################################
# I la giao diem cua duong thang d va doan AB
def GiaoDiemDuongDoan(L):
    Var = V()
    (I, d, AB) = L
    if I in Var: return
    if d not in Var: return    
    if AB not in Var:
        (A, B) = list(AB)
        if (A not in Var) or \
           (B not in Var): return
        value[AB] = Doan([AB])
        
    L = line.convertSegment([value[AB]])
    pI = point.intersection([value[d], L])
    pI.name = I
    value[I] = pI
    pI.draw()

def GiaoDiemHaiDuong(L):
    I = L[0]
    d1 = L[1]
    d2 = L[2]
    pI = point.intersection([value[d1], value[d2]])
    pI.name = I
    value[I] = pI
    pI.draw()
    
# Điểm đối xứng qua cạnh
# vẽ M đối xứng với N qua cạnh AB
def DoiXungQuaCanh(L):
    Var = V()
    (M, N, AB) = L
    if AB not in Var: value[AB] = Doan([AB])
    if N not in Var: return
    if M in Var: return
    value[M] = point.pos_line([value[N], line.convertSegment([value[AB]])])
    value[M].name = M
    value[M].draw()

def DoiXungQuaDiem(L):
    Var = V()
    (M, N, O) = L
    if N not in Var: return
    if O not in Var: return
    if M in Var: return
    value[M] = point.pos_point([value[N], value[O]])
    value[M].name = M
    value[M].draw()



###############################################
#TamGiac(['ABC'])
#QuaMotDiemVuongGocVoiDoan(['d', 'A', 'AB'])
#GiaoDiemDuongDoan(['I', 'd', 'AB'])
#TrucTam(['H', 'ABC'])
#DuongCaoTamGiac(['AH', 'BAC'])
#DoiXungQuaCanh(['K', 'A', 'BC'])
#TrongTam(['G', 'ACB'])
#QuaMotDiemVaSongSongVoiDoan(['d1', 'B', 'AC'])
#QuaMotDiemVuongGocVoiDoan(['d2', 'A', 'AB'])
#DoanTrungBinh(['MN', 'BCA', 'C'])
#TrungTuyen(['CM', 'A])
#DuongTronNgoaiTiep(['O', 'ABC'])
#DoanPhanGiac(['CK', 'ABC'])
#DiemThuocDuongThang(['N', 'd1'])
#Doan(['MN'])
    
