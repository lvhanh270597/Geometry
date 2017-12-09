
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

class rule(object):
    def __init__(self, S):
        v = S.split()
        self.Name = v[0]
        self.Type = v[2]
        self.Func = v[3]
        for i in range(4, len(v)):
            if v[i].isdigit():
                v[i] = float(v[i])
        self.Depend = v[4:]
        self.docs = S
    def __str__(self):
        return self.docs

def draw(value, display):
    line.Line([1, 0, 0]).draw()
    line.Line([0, 1, 0]).draw()

    for key in value.keys():
        obj = value[key]
        print(key)
        #print(obj)
        # draw text in point
        '''if len(key) == 1 and display[key] == '1':
            p = graphics.Point(obj.dx , obj.dy - 10)
            '''
        #######################################
        if display[key] == '1':
            obj.draw(key)
    
def readKnowledge(fileKnowledge):
    f = open(fileKnowledge, 'r')
    V = f.readline().split()
    V = V[2 : ]

    mtp = f.readline().split()
    mtp = mtp[2 : ]
    display = {}
    for i in range(len(mtp)):
        display[V[i]] = mtp[i]
    
    rules = []
    for line in f:
        rules += [rule(line)]
    return (V, rules, display)

def init(V):
    active = {}
    value = {}
    for v in V:
        active[v] = False
        value[v] = None
    return (active, value)

def isNumber(x):
    return str(x).count('.') > 0

def canSolve(r, active):
    for depend in r.Depend:
        # check for a number
        if isNumber(depend): continue
        if not active[depend]:
            return False
    return True

def solve(value, r):
    L = []
    for depend in r.Depend:
        # check for a number
        if isNumber(depend):
            L += [depend]
        else:
            L += [value[depend]]
    return functions[r.Type + '.' + r.Func](L)
        

def main():    
    (V, rules, display) = readKnowledge('../data/bai7.txt')
    (active, value) = init(V)
    
    stop = False
    while not stop:
        stop = True        
        for r in rules:
            if not active[r.Name]:
                if canSolve(r, active):                    
                    active[r.Name] = True
                    value[r.Name] = solve(value, r)
                    stop = False

    draw(value, display)
    
main()

















