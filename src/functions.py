
import random
import point
import line
import segment
import circle
import graphics

win = graphics.GraphWin("My windows", 500, 500)

for i in range(1):
    c1 = circle.rand()
    print(c1)
    c1.draw(win)
    c2 = circle.rand()
    print(c2)
    c2.draw(win)
    p = point.intersect_two_circles(c1, c2)
    print(p)
    

'''colors = ['red', 'blue']

for i in range(2):
    p = point.rand()
    print(p)
    p2 = point.rand()
    L1 = line.throughPoint_1(p)
    L2 = line.combine_2(p2, L1)
    print(L1)
    print(L2)
    p.draw(win)
    color = random.choice(colors)
    print(color)
    L1.draw(win, color)
    L2.draw(win, color)'''
