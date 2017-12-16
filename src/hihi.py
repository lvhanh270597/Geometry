
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
    (M, N, P) = map(str, list(MNP))
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
    (S, R, A) = map(str, list(SRA))
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
    (S, R, A) = map(str, list(SRA))
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
    if M in Var and d in Var: return
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

def DuongCaoTuGiac(HABCD):
    Var = V()
    if HABCD in Var: return
    (H, A, B, C, D) = map(str, list(HABCD))
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
    tg_ABCD = fourangle.Fourangle([value[A], value[B], value[C], value[D]])
    seg = segment.Segment([value[C], value[D]])
    ln = line.convertSegment([seg])
    ln_1 = line.combine_1([value[A], ln])
    value[H] = point.intersection([ln,ln_1])
    value[H].name = H
    seg_1 = segment.Segment([value[A], value[H]])
    value[seg_1] = seg_1
    tg_ABCD.draw()
    seg_1.draw()

def DiemThuocTia(MOx):
    Var = V()
    if MOx in Var: return
    (M, O, x) = map(str, list(MOx))
    if O not in Var:
        value[O] = point.rand()
        value[O].name = O
    if x not in Var:
        value[x] = vector.rand()
        value[x].name = x
    ray_Ox = ray.Ray([value[O],value[x]])
    seg_Ox = segment.convertRay([ray_Ox])
    value[M] = point.onSegment([seg_Ox])
    value[M].name = M
    value[M].draw()
    ray_Ox.draw()

def GiaoDiemHaiTia(M, Ox,Ty):
    Var = V()
    if Ox in Var and Ty in Var: return
    (O, x) = map(str, list(Ox))
    (T, y) = map(str, list(Ty))
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
    ray_Ox = ray.Ray([value[O], value[x]])
    ray_Ty = ray.Ray([value[T], value[y]])
    ln_Ox = line.convertRay([ray_Ox])
    ln_Ty = line.convertRay([ray_Ty])
    value[M] = point.intersection([ln_Ox, ln_Ty])
    value[M].name = M
    seg_Ox = segment.convertRay([ray_Ox])
    seg_Ty = segment.convertRay([ray_Ty])
    if mathfunctions.intersect(value[M], [seg_Ox , seg_Ty]) == True:
        value[M].draw()
    ray_Ox.draw()
    ray_Ty.draw()
    
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
    
        
def main():
    #DiemNamGiuaHaiDiem('LNP')
    #BaDiemThangHang('NRA')
    #BaDiemKhongThangHang('ABC')
    #DiemThuocDuongThang('N','AB')
    #DiemKhongThuocDuongThang('M','d1')
    #DuongCaoTuGiac('HABCD')
    #DiemThuocTia('MOx')
    #GiaoDiemHaiTia('N','Ox','Ty')
    #GiaoDiemTiaDoan('K', 'Ox', 'AB')
    #HaiDoanThangSongSong('AB', 'CD')
    #HaiDoanThangVuongGoc('AB', 'CD')
    #HaiDoanThangBangNhau('AB', 'CD')
    #GiaoDiemHaiDoan('E','AB', 'CD')
    #TiaNamGiuaHaiTia('Oxzy')
    HaiTiaDoiNhau('Oxy')
    

main()
