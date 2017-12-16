import random
def Doan(a):
    L=[]
    L.append(str(a[0]) + " = point rand")
    L.append(str(a[1]) + " = point rand")
    L.append( str(a) + " = segment Segment " + str(a[0]) +" " + str(a[1]))
    return L
def Goc(a):
    L = []
    L.append(str(a[0]) + " = point rand")
    L.append(str(a[1]) + " = point rand")
    L.append(str(a[2]) + " = point rand")
    return L
#vd Tamgiacvuong("ABC")
def TamGiacVuong(a):
    L = []
    L.append(str(a[0]) +" = point rand" )
    L.append(str(a[2]) +" = point rand")
    L.append("S = segment Segment S")
    L.append("d = line convertSegment " + str(a[0])+ str(a[2]))
    L.append("p = line combine_1 " + a[0] + " d")
    L.append(str(a[1]) +" = point onLine p")
    L.append(str(a) + " = triangle Triangle " + str(a[0]) + " " + str(a[1]) + " " + str(a[2]))
    return L
def TamGiacDeu(a):
    L = []
    L.append(str(a[0]) + " = point rand")
    L.append(str(a[1]) + " = point rand")
    L.append ("temp = mathfunctions distance " +a[0] +" " + a[1])
    L.append("X = circle Circle " +a[0]+ " " +"temp")
    L.append("Y = circle Circle " +a[1]+ " " + "temp")
    L.append(a[2] + " = point intersect_two_circles X Y")
    L.append(str(a) + " = triangle Triangle " + str(a[0]) + " " + str(a[1]) + " " + str(a[2]))
    return L
# tham so dau la ten diem de lay trung diem, tham so con lai la 2 diem cua doan
# VD MAB nghia la M la trung diem AB 
def TrungDiem(a):
    L=[]
    L.append(str(a[1]) + " = point rand")
    L.append(str(a[2]) + " = point rand")
    L.append(str(a[0]) + " = point center " + a[1] + " " + a[0])
    return L 
def NamGiua(a):
    L = []
    L.append(str(a[1]) + " = point rand")
    L.append(str(a[2]) + " = point rand")
    k=1/random.randint(0,10)
    L.append(str(a[0]) + " = point distanceRatio " + str(a[1])+ str(a[2])+ " " +str(k))
    return L
# VD thuocMAB M thuoc AB 
def Thuoc(a):
    L = []
    L.append(str(a[1]) + " = point rand")
    L.append(str(a[2]) + " = point rand")
    k=1/random.randint(0,10)
    L.append(str(a[0]) + " = point distanceRatio " + str(a[1])+ str(a[2])+ " " +str(k))
    return L

def KhongNamGiua(a):
    L = []
    L.append(str(a[1]) + " = point rand")
    L.append(str(a[2]) + " = point rand")
    k = random.choice([1.25,1.5,1.75,2,2.25,2.5,2.75,3])
    L.append(str(a[0]) + " = point distanceRatio " + str(a[1])+ str(a[2]) + " " + str(k))
    return L

# vd Giaodiem(ABCDE) nghia la A la giao diem BC DE 
def GiaoDiemDoan(a):
    L = []
    L.append (str(a[1]) + str(a[2]) + " = segment rand ")
    L.append("j1 = line convertSegment "+ str(a[1])+str(a[2]))
    L.append (str(a[3]) + str(a[4]) + " = segment rand")
    L.append("j2 = line convertSegment "+str(a[3])+str(a[4]))
    L.append (a[0] + " = point intersection j1 j2")
    return L

#vd Thuocduongtron(M(O;R)) nghi ma thuoc dc tron tam O bk R 
def ThuocDuongTron(a):
    L = []
    L.append ("Circle1 = circle Circle " + str(a[2]) +" "+ str(a[4]))
    L.append(a[0]+" = point onCircle Circle1")
    return L
def NgoaiDuongTron(a):
    L = []
    L.append ("C1 = circle Circle " + str(a[2]) +" "+ str(a[4]))
    L.append("temp = point onCircle C1")
    L.append ( str(a[0]) + " = point pos_point" + a[2] + " " + "temp")
    return L
# Vd Tieptuyen("AB(O;R))
def TiepTuyen(a):
    L = []
    L.append ("C1 = circle Circle " + str(a[3]) +" "+ str(a[5]))
    L.append(a[0]+" = point onCircle C1")
    L.append(a[3] + a[0] + " = segment Segment " + a[3] + a[0])
    L.append("Line1 = line convertSegment " + a[3] + a[0])
    L.append(" Line2 = line combine_1 " + a[0] + " " + a[3] + a[0])
    L.append(a[1] + " = point onLine Line2")
    return L
#vd Daycung("AC{O;R)")
def DayCung(a):
    L = []
    L.append("Circle1 = circle Circle " + a[3] + " " + a[5])
    L.append( a[1]+ " = point onCircle Circle1")
    L.append( a[0]+ " = point onCircle Circle1")
    return L 
def DuongKinh(a):
    L = []
    L.append("Circle1 = circle Circle " + a[3] + " " + a[5])
    L.append( a[1] + " = point onCicle Circle1")
    L.append( a[0] + " = point pos_point " + a[1]+ " " + a[3])
    return L
#vd Giaodiemduongtron_doan("MAB(O;R)")
def GiaoDiemDuongTron_Doan(a):
    L = []
    L.append("Circle1 = circle Circle " + a[4] + " " + a[6])
    L.append(a[0] + " = point onCicle Circle1")
    L.append(a[4] + a[0] + " = segment Segment " + a[4] + a[0])
    L.append("Line1 = line convertSegment " + a[4] + a[0])
    L.append(" Line2 = line combine_1 " + a[0] + " " + a[4] + a[0])
    L.append(a[1] + " = point onLine Line2")
    L.append(a[2] + " = point pos_point " + a[1] + " " +a[0])
    return L
#vd Duongcao(AHABC)
def DuongCao_TG(a):
    L = []
    L.append(a[2]+ " = point rand")
    L.append(a[3]+ " = point rand")
    L.append(a[4]+ " = point rand")
    L.append( str(a[2])+str(a[3])+str(a[4]) + " = triangle Triangle " + str(a[2]) + " " + str(a[3]) + " " + str(a[4]))
    L.append ( "segment1 = segment Segment " + a[3] +" "+ a[4])
    L.append ( "Line1  = line convertSegment segment1")
    L.append ("Line2 = line combine_1 " + a[0] + " " + "Line1")
    L.append(a[1] +" = point intersection Line1 Line2")
    return L
# Duongcao_TGV("AHABC")
def DuongCao_TGV(a):
    L = []
    L.append(str(a[2]) +" = point rand" )
    L.append(str(a[4]) +" = point rand")
    L.append("S = segment Segment " + a[2] +" " +a[4])
    L.append("d = line convertSegment S")
    L.append("p = line combine_1 " + a[2] + " d")
    L.append(str(a[3]) +" = point onLine p")
    L.append( str(a[2]) +  str(a[3]) +str(a[4]) + " = triangle Triangle " + str(a[2]) + " " + str(a[3]) + " " + str(a[4]))
    L.append ( "segment1 = segment Segment " + a[3] +" "+ a[4])
    L.append ( "Line1  = line convertSegment segment1")
    L.append ("Line2 = line combine_1 " + a[0] + " " + "Line1")
    L.append(a[1] +" = point intersection Line1 Line2")
    return L 
def DuongCao_TGC(a):
    temp = []
    temp.append(str(a[3]) + " = point rand")
    temp.append(str(a[4]) + " = point rand")
    R = random.randint(1,10)
    temp.append("duongTron = circle Circle "+ str(a[3]) + " " + str(R))
    temp.append("duongTron1 = circle Circle "+ str(a[4]) + " " + str(R))
    temp.append(str(a[2]) + " = point intersect_two_circles duongTron duongTron1")
    L.append( str(a[2]) +  str(a[3]) +str(a[4]) + " = triangle Triangle " + str(a[2]) + " " + str(a[3]) + " " + str(a[4]))
    temp.append ( "segment1 = segment Segment " + a[3] +" "+ a[4])
    temp.append ( "Line1  = line convertSegment segment1")
    temp.append ("Line2 = line combine_1 " + a[0] + " " + "Line1")
    temp.append(a[1] +" = point intersection Line1 Line2")
    L.append( str(a[2]) + str(a[3]) + str(a[4]) + " = triangle Triangle " + str(a[2]) + " " + str(a[3]) + " " + str(a[4]))
    L.append ( "segment1 = segment Segment " + a[3] +" "+ a[4])
    L.append ( "Line1  = line convertSegment segment1")
    L.append ("Line2 = line combine_1 " + a[0] + " " + "Line1")
    L.append(a[1] +" = point intersection Line1 Line2")
    return temp
def DuongCao_TGVC(a):
    temp.append(str(a[3]) + " = point rand")
    temp.append(str(a[4]) + " = point rand")
    temp.append("diem = point center " + str(a[3])+ " " + str(a[4]))
    temp.append("R = mathfunctions distance " + str(a[3]) + " " +str(a[4]))
    temp.append("R1 = R / 2")
    temp.append("duongtron = circle Circle diem R1")
    temp.append("doan = segment Segment " + str(a[3]) + " " +str(a[4]))
    temp.append("duongthang = line convertSegment doan")
    temp.append("duongthang1 = line combine_1 diem duongthang")
    temp.append("List = list intersect_line_circle duongthang1 duongtron")
    temp.append(str(a[2]) + " = List[0]")
    temp.append( str(a[2]) + str(a[3]) + str(a[4]) + " = triangle Triangle " + str(a[2]) + " " + str(a[3]) + " " + str(a[4])
    temp.append ( "segment1 = segment Segment " + a[3] +" "+ a[4])
    temp.append ( "Line1  = line convertSegment segment1")
    temp.append ("Line2 = line combine_1 " + a[0] + " " + "Line1")
    temp.append(a[1] +" = point intersection Line1 Line2")
    return temp
def DuongCao_TGD(a):
    L = []
    L.append(str(a[2]) + " = point rand")
    L.append(str(a[3]) + " = point rand")
    L.append ("temp = mathfunctions distance " +a[2] +" " + a[3])
    L.append("X = circle Circle " +a[2]+ " " +"temp")
    L.append("Y = circle Circle " +a[3]+ " " + "temp")
    L.append(a[4] + " = point intersect_two_circles X Y")
    L.append( str(a[2]) + str(a[3]) + str(a[4]) + " = triangle Triangle " + str(a[2]) + " " + str(a[3]) + " " + str(a[4]))
    L.append ( "segment1 = segment Segment " + a[3] +" "+ a[4])
    L.append ( "Line1  = line convertSegment segment1")
    L.append ("Line2 = line combine_1 " + a[0] + " " + "Line1")
    L.append(a[1] +" = point intersection Line1 Line2")
    return L
