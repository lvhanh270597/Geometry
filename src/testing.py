
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
from template import *

functions = {
    'point.rand'                    : point.rand,    
    'point.onCircle'                : point.onCircle,
    'point.center'                  : point.center,
    'point.onLine'                  : point.onLine,
    'point.onSegment'               : point.onSegment,
    'point.insideTriangle'          : point.insideTriangle,
    'point.insideAngle'             : point.insideAngle,
    'point.pos_line'                : point.pos_line,
    'point.distanceRatio'           : point.distanceRatio,
    'point.combine_1'               : point.combine_1,
    'point.combine_2'               : point.combine_2,
    'point.combine_3'               : point.combine_3,
    'point.intersection'            : point.intersection,
    'point.combine_triangle'        : point.combine_triangle,
    'point.combine_square'          : point.combine_square,
    'point.combine_rectangle'       : point.combine_rectangle,
    'point.intersect_line_circle'   : point.intersect_line_circle,
    'point.intersect_two_circles'   : point.intersect_two_circles,
    'point.pos_point'               : point.pos_point,
    'line.Line'                     : line.Line,
    'line.rand'                     : line.rand,
    'line.throughPoint_1'           : line.throughPoint_1,
    'line.combine_angle'            : line.combine_angle,
    'line.combine_1'                : line.combine_1,
    'line.combine_2'                : line.combine_2,
    'line.convertSegment'           : line.convertSegment,
    'line.convertRay'               : line.convertRay,
    'circle.Circle'                 : circle.Circle,
    'circle.rand'                   : circle.rand,
    'circle.through_three'          : circle.through_three,
    'mathfunctions.distance'        : mathfunctions.distance,
    'segment.Segment'               : segment.Segment,
    'segment.rand'                  : segment.rand,
    'triangle.Triangle'             : triangle.Triangle,
    'triangle.rand'                 : triangle.rand,
    'fourangle.rand'                : fourangle.rand,
    'fourangle.Fourangle'           : fourangle.Fourangle,
    'fourangle.rand_rectangle'      : fourangle.rand_rectangle,
    'fourangle.rand_hinhBinhHanh'   : fourangle.rand_hinhBinhHanh,
    'angle.Angle'                   : angle.Angle,
    'angle.rand'                    : angle.rand,
    'vector.rand'                   : vector.rand,
    'ray.Ray'                       : ray.Ray
}

def main():
    #template.TamGiacVuong('ABC')
    #template.DoanPhanGiac('E', 'ABC')
    '''TamGiac('ABC')
    DoanPhanGiac('H', 'ABC')
    DoanPhanGiac('K', 'BCA')
    GiaoDiemDoan(['I', 'BH', 'CK'])
    QuaMotDiemVaSongSongVoiDoan('d', 'I', 'BC')
    GiaoDiemDuongDoan('D', 'd', 'AB')
    GiaoDiemDuongDoan('E', 'd', 'AC')'''
    '''HinhThang('ABCD')
    DuongCaoTuGiac('H', 'ABCD')
    DuongCaoTuGiac('K', 'BADC')    '''
    '''TamGiacCan('ABC')
    DoanPhanGiac('E', 'ABC')
    DoanPhanGiac('F', 'ACB')
    TuGiac('BFEC')'''
    '''HinhThang('ABCD')
    TrungDiem('M', 'A', 'D')
    TrungDiem('N', 'B', 'C')
    GiaoDiemHaiDoan('I', 'MN', 'BD')
    GiaoDiemHaiDoan('K', 'MN', 'AC')'''
    '''TamGiac('ABC')
    TrungTuyen('D', 'ABC')
    TrungTuyen('E', 'CBA')
    GiaoDiemHaiDoan('G', 'AD', 'CE')
    TrungDiem('I', 'GB')
    TrungDiem('K', 'GC')'''
    '''TamGiac('ABC')
    TrungTuyen('M', 'ABC')
    TrungDiem('D', 'AM')
    Duong('dBD')
    Duong('dAC')
    GiaoDiemHaiDuong('E', 'dBD', 'dAC')'''
    TamGiac('ABC')
    TrungTuyen('D', 'BCA')
    TrungTuyen('E', 'CAB')
    TrungDiem('M', 'BE')
    TrungDiem('N', 'CD')
    Duong('dMN')
    Duong('dBD')
    Duong('dCE')
    GiaoDiemHaiDuong('I', 'dMN', 'dCE')
    GiaoDiemHaiDuong('K', 'dBD', 'dCE')
    
main()
s = input()










