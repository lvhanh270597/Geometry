
import random
import point
import line
import segment
import ray
import circle
from graphics import *

win = GraphWin("My windows", 500, 500)

for i in range(10):
    a = point.rand()
    b = point.rand()
    print(a)
    print(b)
    line = Line(Point(a.x, a.y), Point(b.x, b.y))
    line.draw(win)
