# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 15:14:25 2017

@author: yenhoang
"""
# Diem - Tia
def DiemThuocTia(a):
    L = []
    L.append(str(a[0]) + " = ray rand")
    L.append("d = line convertRay " + str(a[0]))
    L.append(str(a[1]) + " = point onLine d")
    return L

def DiemLaGiaoDiemHaiTia(a):
    L = []
    L.append(str(a[0]) + " = ray rand")
    L.append(str(a[1]) + " = ray rand")
    L.append("d = line convertRay " + str(a[0]))
    L.append("p = line convertRay " + str(a[1]))
    L.append(str(a[2]) + " = point intersection dp")
    return L

def DiemLaGiaoDiemTiaVaDoan(a):
    L = []
    L.append(str(a[0]) + " = ray rand")
    L.append(str(a[1]) + " = segment rand")
    L.append("d = line convertRay " + str(a[0]))
    L.append("p = line convertSegment " + str(a[1]))
    L.append(str(a[2]) + " = point intersection dp")
    return L

# Doan - Doan
def HaiDoanThangSongSong(a):
    L = []
    L.append(str(a[0]) + " = segment rand")
    L.append("d = line convertSegment " + str(a[0]))
    L.append(str(a[1]) + " = point rand")
    L.append("p = line combine_2 " + str(a[1]) + "d")
    L.append(str(a[2]) + " = point onLine p")
    L.append(str(a[3]) + " = segment Segment " + str(a[1]) + " " + str(a[2]))
    return L

def HaiDoanThangVuongGoc(a):
    L = []
    L.append(str(a[0]) + " = segment rand")
    L.append("d = line convertSegment " + str(a[0]))
    L.append(str(a[1]) + " = point onLine d")
    L.append("p = line combine_2 " + str(a[1]) + "d")
    L.append(str(a[2]) + " = point onLine p")
    L.append(str(a[3]) + " = segment Segment " + str(a[1]) + " " + str(a[2]))
    return L

def HaiDoanThangBangNhau(a):
    L = []
    L.append(str(a[0]) + " = point rand")
    L.append(str(a[1]) + " = point rand")
    L.append("d = mathfunction distance " + str(a[0]) + str(a[1]))
    L.append(str(a[2]) + " = point rand")
    L.append(str(a[3]) + " = point combine_3 " + str(a[2]) + "d")
    L.append(str(a[4]) + " = segment Segment " + str(a[0]) + " " + str(a[1]))
    L.append(str(a[5]) + " = segment Segment " + str(a[2]) + " " + str(a[3]))
    return L

def GiaoDiemHaiDoanThang(a):
    L = []
    L.append(str(a[0]) + " = segment rand")
    L.append(str(a[1]) + " = onSegment")
    L.append(str(a[2]) + " = point rand")
    L.append(str(a[3]) + " = segment Segment " + str(a[1]) + " " + str(a[2]))
    return L
    
# Tia - Tia
def TiaNamGiuaHaiTia(a):
    L = []
    L.append(str(a[0]) + " ray rand")
    L.append(str(a[1]) + " = ray combine_angle " + str(a[0]) + 30)
    L.append(str(a[1]) + " = ray combine_angle " + str(a[0]) + 75)
    return L

def HaiTiaDoiNhau(a):
    L = []
    L.append(str(a[0]) + " = ray rand")
    L.append(str(a[1]) + " = ray combine_angle " + str(a[0]) + 180)
    return L

# Doan - Tia
def DiemLaGiaoDiemDoanTia(a):
    L = []
    L.append(str[0] + " = ray rand")
    L.append("d = line convertSegment " + str(a[0]))
    L.append(str(a[1]) + " = point onLine d")
    L.append("p = line throughPoint " + str(a[1]))
    L.append(str(a[2]) + " = point onLine p")
    L.append(str(a[3]) + " = point onLine p")
    L.append(str(a[4]) + " = segment Segment " + str(a[2]) + " " + str(a[3]))
    return L
    
# Diem - Tia - Doan
def DiemLaGiaoDoanTia(a):
    L = []
    L.append(str[0] + " = ray rand")
    L.append("d = line convertSegment " + str(a[0]))
    L.append(str(a[1]) + " = point onLine d")
    L.append("p = line throughPoint " + str(a[1]))
    L.append(str(a[2]) + " = point onLine p")
    L.append(str(a[3]) + " = point onLine p")
    L.append(str(a[4]) + " = segment Segment " + str(a[2]) + " " + str(a[3]))
    return L

# Goc - Goc
def HaiGocBangNhau(a):
    L = []
    L.append(str(a[0]) + " = angle rand")
    L.append(str(a[1]) + " = angle Angle " + str(a[0]))
    return L

def GocVuong(a):
    L = []
    L.append(str(a[1]) + " = point rand")
    L.append(str(a[2]) + " = point rand")
    L.append("d = line convertSegment " + str(a[1])+ str(a[2]))
    L.append("p = line combine_1 " + a[1] + "d")
    L.append(str(a[0]) +" = point onLine p")
    return L

# Goc - Doan
def DoanPhanGiac(a):
    L = []
    L.append(str(a[0]) + " = point rand")
    L.append(str(a[1]) + " = point rand")
    L.append(str(a[2]) + " = point rand")
    L.append("d = line convertSegment " + str(a[0])+ str(a[1]))
    L.append("p = line convertSegment " + str(a[0])+ str(a[2]))
    L.append("x = circle Circle " + str(a[0]))
    L.append("e = point intersect_line_circle dx")
    L.append("f = point intersect_line_circle px")
    L.append("g = circle Circle e")
    L.append("h = circle Circle f")
    L.append(str(a[3]) + " = point intersect_two_circles gh")
    L.append(str(a[4]) + " = segment Segment " + str(a[0]) + " " + str(a[3]))
    return L

# Goc - Tia
def TiaPhanGiac(a):
    L = []
    L.append(str(a[0]) + " = point rand")
    L.append(str(a[1]) + " = point rand")
    L.append(str(a[2]) + " = point rand")
    L.append("d = line convertSegment " + str(a[0])+ str(a[1]))
    L.append("p = line convertSegment " + str(a[0])+ str(a[2]))
    L.append("x = circle Circle " + str(a[0]))
    L.append("e = point intersect_line_circle dx")
    L.append("f = point intersect_line_circle px")
    L.append("g = circle Circle e")
    L.append("h = circle Circle f")
    L.append(str(a[3]) + " = point intersect_two_circles gh")
    L.append("f = segment Segment " + str(a[0]) + " " + str(a[3]))
    L.append("x = vector directVector_2 f")
    L.append(str(a[4]) + " = vector Vector " + str(a[0]) + "x")
    return L

# TamGiac - TamGiac
def HaiTamGiacBangNhau(a):
    L = []
    L.append(str(a[0]) + " = point rand")
    L.append(str(a[1]) + " = point rand")
    L.append(str(a[2]) + " = point rand")
    L.append("x = mathfunction distance " + str(a[0]) + str(a[1]))
    L.append("y = mathfunction distance " + str(a[0]) + str(a[2]))
    L.append("z = mathfunction distance " + str(a[1]) + str(a[2]))
    L.append(str(a[3]) + " = point rand")
    L.append(str(a[4]) + " = point combine_3 " + str(a[3]) + "x")
    L.append("u = circle Circle " + str(a[3]) + "y")
    L.append("v = circle Circle " + str(a[4]) + "z")
    L.append(a[5] + " = point intersect_two_circles uv")
    return L

def HaiTamGiacDongDang(a):
    L = []
    L.append(str(a[0]) + " = point rand")
    L.append(str(a[1]) + " = point rand")
    L.append(str(a[2]) + " = point rand")
    L.append("x = mathfunction distance " + str(a[0]) + str(a[1]))
    L.append("y = mathfunction distance " + str(a[0]) + str(a[2]))
    L.append("z = mathfunction distance " + str(a[1]) + str(a[2]))
    L.append(str(a[3]) + " = point rand")
    L.append(str(a[4]) + " = point combine_3 " + str(a[3]) + "x")
    L.append("u = circle Circle " + str(a[3]) + "y")
    L.append("v = circle Circle " + str(a[4]) + "z")
    L.append(a[5] + " = point intersect_two_circles uv")
    return L

    
    
    