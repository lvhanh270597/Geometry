
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

    AH.draw()

def DiemThuocTia(M, Ox):
    Var = V()
    if M in Var: return
    if Ox not in Var: return
                              
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
    if Ox not in Var: return
    if Ty not in Var: return
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
                              
    rayOx = ray.Ray([value[O], value[x]])
    rayTy = ray.Ray([value[T], value[y]])
    lnOx = line.convertRay([rayOx])
    lnTy = line.convertRay([rayTy])
    value[M] = point.intersection([lnOx, lnTy])
    value[M].name = M
    value[M].draw()
    rayOx.draw()
    rayTy.draw()
    
def main():
    #DiemNamGiuaHaiDiem('LNP')
    #BaDiemThangHang('NRA')
    #BaDiemKhongThangHang('ABC')
    #DiemThuocDuongThang('N','AB')
    #DiemKhongThuocDuongThang('M','d1')
    #DuongCaoTuGiac('HABCD')
    DiemThuocTia('TOx')
    GiaoDiemHaiTia('N','Ox','Ty')
    

main()
