
import random
import point
import line
import segment
import ray
import circle


def getRandPoint():
    T = point.Point(1, 2)
    T.x = random.randint(100, 500)
    T.y = random.randint(100, 500)
    return T

def getRandSegment():
    A = getRandPoint()
    B = getRandPoint()
    T = segment.Segment(A, B)    
    return T

def getMiddlePoint(A, B):
    M = point.Point((A.x + B.x) / 2, (A.y + B.y) / 2)
    return M

def getMiddleSeg(S):
    return getMiddlePoint(S.A, S.B)

