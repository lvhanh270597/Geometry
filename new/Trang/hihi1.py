
import random

def Tia(a):
    temp = []
    temp.append(str(a) + " = ray Ray " + str(a[0]) + " " + str(a[1]))
    temp.append(str(a[0]) + " = point rand")
    temp.append(str(a[1]) + " = vector rand")
    return temp

def DuongThang(a):
    temp = []
    temp.append(str(a) + " = line rand")
    return temp

def TamGiac(a):
    temp = []
    temp.append(str(a) + " = triangle Triangle " + str(a[0]) + " " + str(a[1]) + " " + str(a[2]))
    temp.append(str(a[0]) + " = point rand")
    temp.append(str(a[1]) + " = point rand")
    temp.append(str(a[2]) + " = point rand")
    return temp

def TamGiacCan(a):
    temp = []
    temp.append(str(a) + " = triangle Triangle " + str(a[0]) + " " + str(a[1]) + " " + str(a[2]))
    temp.append(str(a[1]) + " = point rand")
    temp.append(str(a[2]) + " = point rand")
    R = random.randint(1,10)
    temp.append("duongTron = circle Circle "+ str(a[1]) + " " + str(R))
    temp.append("duongTron1 = circle Circle "+ str(a[2]) + " " + str(R))
    temp.append(str(a[0]) + " = point intersect_two_circles duongTron duongTron1")
    return temp

def TamGiacVuongCan(a):
    temp = []
    temp.append(str(a) + " = triangle Triangle " + str(a[0]) + " " + str(a[1]) + " " + str(a[2]))
    temp.append(str(a[1]) + " = point rand")
    temp.append(str(a[2]) + " = point rand")
    temp.append("diem = point center " + str(a[1])+ " " + str(a[2]))
    temp.append("R = mathfunctions distance " + str(a[1]) + " " +str(a[2]))
    temp.append("R1 = R / 2")
    temp.append("duongtron = circle Circle diem R1")
    temp.append("doan = segment Segment " + str(a[1]) + " " +str(a[2]))
    temp.append("duongthang = line convertSegment doan")
    temp.append("duongthang1 = line combine_1 diem duongthang")
    temp.append("List = list intersect_line_circle duongthang1 duongtron")
    temp.append(str(a[0]) + " = List[0]")
    return temp

def TuGiac(a):
    temp = []
    temp.append(str(a) + " = fourangle Fourangle " + str(a[0]) + " " + str(a[1]) + " " + str(a[2]) + " " + str(a[3]))
    temp.append(str(a[0]) + " = point rand")
    temp.append(str(a[1]) + " = point rand")
    temp.append(str(a[2]) + " = point rand")
    temp.append(str(a[3]) + " = point ranxd")
    return temp

def HinhThang(a):
    temp = []
    temp.append(str(a) + " = fourangle Fourangle " + str(a[0]) + " " + str(a[1])+ " " + str(a[2]) + " " + str(a[3]))
    temp.append(str(a[2]) + " = point rand")
    temp.append(str(a[3]) + " = point rand")
    temp.append("doan = segment Segment " + str(a[2]) + " " + str(a[3]))
    temp.append("diem = point distanceRatio doan 0.4")
    temp.append("duongthang = line combine_ 1 diem doan")
    temp.append(str(a[0])+ " = point onLine duongthang")
    temp.append("duongthang2 = line combine_2 "+ str(a[0]) + " doan")
    temp.append("diem2 = point distanceRatio doan 0.8")
    temp.append("duongthang3 = line combine_1 diem2 doan")
    temp.append(str(a[1]) + " = point intersection duongthang2 duongthang3")
    return temp

def HinhThangCan(a):
    temp = []
    temp.append(str(a) + " = fourangle Fourangle " + str(a[0]) + " " + str(a[1])+ " " + str(a[2]) + " " + str(a[3]))
    temp.append(str(a[2]) + " = point rand")
    temp.append(str(a[3]) + " = point rand")
    temp.append("doan = segment Segment " + str(a[2]) + " " + str(a[3]))
    temp.append("diem = point distanceRatio doan 0.4")
    temp.append("duongthang = line combine_ 1 diem doan")
    temp.append(str(a[0])+ " = point onLine duongthang")
    temp.append("duongthang2 = line combine_2 "+ str(a[0]) + " doan")
    temp.append("diem2 = point distanceRatio doan 0.6")
    temp.append("duongthang3 = line combine_1 diem2 doan")
    temp.append(str(a[1]) + " = point intersection duongthang2 duongthang3")
    return temp

def HinhThangVuong(a):
    temp = []
    temp.append(str(a) + " = fourangle Fourangle " + str(a[0]) + " " + str(a[1])+ " " + str(a[2]) + " " + str(a[3]))
    temp.append(str(a[2]) + " = point rand")
    temp.append(str(a[3]) + " = point rand")
    temp.append("doan = segment Segment " + str(a[2]) + " " + str(a[3]))
    temp.append("duongthang = line convertSegment doan")
    temp.append(str(a[0]) + " = point combine_1 " +str(a[3])+ " duongthang")
    temp.append(str(a[1]) + " = point combine_recrangle " + str(a[2]) + " " + str(a[3]) + " " +str(a[0]))
    return temp

def HinhBinhHanh(a):
    temp = []
    temp.append(str(a) + " = fourangle rand_hinhBinhHanh")
    return temp

def HinhThoi(a):
    temp = []
    temp.append(str(a[0]) + " = point rand")
    temp.append(str(a[1]) + " = point rand")
    temp.append("duongthang = line throughPoint " + str(a[1]))
    temp.append(str(a[2]) + " = point pos_line " + str(a[0]) + " duongthang")
    temp.append("doan = segment Segment " + str(a[0]) + " "+ str(a[2]))
    temp.append("duongthang1 = line convertSegment doan")
    temp.append(str(a[3]) + " = point pos_line " + str(a[1]) + " duongthang1")
    return temp

def HinhVuong(a):
    temp = []
    temp.append(str(a) + " = fourangle Fourangle " + str(a[0]) + " " + str(a[1])+ " " + str(a[2]) + " " + str(a[3]))
    R = random.randint(1,10)
    temp.append(str(a[0]) + " = point rand")
    temp.append(str(a[1]) + " = point combine_3 " + str(a[0]) + " " + str(R))
    temp.append("doan = segment Segment " + str(a[0]) + " " + str(a[1]))
    temp.append("duongthang = line convertSegment doan")
    temp.append(str(a[2]) + " = point combine_1 " + str(a[1])+ " duongthang")
    temp.append(str(a[3]) + " = point combine_rectangle " + str(a[0]) + " " + str(a[1]) + " " + str(a[2]))
    return temp

def HinhChuNhat(a):
    temp = []
    temp.append(str(a) + " = fourangle rand_rectangle")
    return temp

def DuongTron(a):
    temp = []
    temp.append(str(a) + " = circle Cirle " + str(a[0]) + " " + str(a[1]))
    temp.append(str(a[0]) + " = point rand")
    return temp

def NamGiua(a):
    temp = []
    temp.append(str(a[1]) + " = point rand")
    temp.append(str(a[2]) + " = point rand")
    temp.append("doan = segment Segment " + str(a[1]) + " " + str(a[2]))
    temp.append(str(a[0]) + " = point onSegment doan")
    return temp

def KhongThangHang(a):
    temp = []
    temp.append(str(a[0]) + " = point rand")
    temp.append(str(a[1]) + " = point rand")
    temp.append(str(a[2]) + " = point combine_triangle " + str(a[0]) + " " + str(a[1]))
    return temp

def ThangHang(a):
    temp = []
    temp.append(str(a[0]) + " = point rand")
    temp.append(str(a[1]) + " = point rand")
    temp.append("doan = segment Segment " + str(a[0]) + " " + str(a[1]))
    temp.append("dt = line convertSegment doan")
    temp.append(str(a[2]) + " = point onLine dt")
    return temp

def Thuoc(a):
    temp = []
    temp.append(str(a[1]) + " = line rand")
    temp.append(str(a[0]) + " = point onLine " + str(a[1]))
    return temp

def KhongThuoc(a):
    temp = []
    temp.append(str(a[1]) + " = line rand")
    temp.append("diem  = point onLine " + str(a[1]))
    temp.append("diem1 = point onLine " + str(a[1]))
    temp.append(str(a[0]) + " = point combine_triangle diem diem1")
    return temp

def DuongCao(a):
    temp = []
    seg = a[0]
    four = a[1]
    temp.append(str(four[0]) + " = point rand")
    temp.append(str(four[1]) + " = point rand")
    temp.append(str(four[2]) + " = point rand")
    temp.append(str(four[3]) + " = point rand")
    temp.append(str(four) + " = fourangle Fourangle " + str(four[0]) + " " + str(four[1]) + " " + str(four[2]) + " " + str(four[3]))
    temp.append("doan = segment Segment " + str(four[2]) + " " + str(four[3]))
    temp.append("dt = line convertSegment doan")
    temp.append("duongthang = line combine_1 " + str(four[0]) + " dt")
    temp.append(str(seg[1]) + " = point intersection dt duongthang")
    temp.append(str(a[0]) + " = segment Segment " + str(four[0]) + " " +str(seg[1]))
    return temp
    
