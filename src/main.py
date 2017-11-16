
import random

from graphics import *
from functions import *

win = GraphWin('My circle', 800, 500)


A = getRandPoint()
B = getRandPoint()

print(A)
print(B)
print(getMiddlePoint(A, B))
for i in range(10):
    S = getRandSegment()
    print(S)

    r = random.randrange(256)
    b = random.randrange(256)
    g = random.randrange(256)
    color = color_rgb(r, g, b)
    
    line = Line(Point(S.A.x, S.A.y), Point(S.B.x, S.B.y))
    line.setWidth(2)
    line.setOutline(color)
    line.draw(win)
