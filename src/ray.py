import random
import point
import vector
import segment
import mathfunctions
from RULE import *

class Ray(object):
    def __init__(self, L):        
        self.start = L[0]
        self.v = L[1]
        self.name = L[0].name + L[1].name
        if len(L) > 2: self.name = L[2]
        self.drawn = False
    def draw(self):

        if self.drawn: return
        # determine end point
        size = vector.size(self.v)

        dx = 10 / size
        dy = 10 / size
        
        xA = self.start.x + dx * self.v.a
        yA = self.start.y + dy * self.v.b
        A = point.Point([xA, yA, self.v.name])        
        # draw start point and end point
        self.start.draw()
        A.draw()
        # draw the line between start and end
        line = graphics.Line(graphics.Point(self.start.dx, self.start.dy),
                             graphics.Point(A.dx, A.dy))
        
        line.setArrow('last')
        line.draw(win)

        #decide drawn = False
        self.drawn = True
        
    def __str__(self):
    	return "(" + str(self.start) + ", " + str(v) + ')'    	
    
# return a random ray    
def rand(L=None):
    start = point.rand()
    v = vector.rand()
    return Ray([start, v])

# trả về 1 ray, cái ray đó nó tạo với ray khác một góc cho trước
def combine_angle(L):
    ray = L[0]
    angle = L[1]
    l1 = convertRay(ray)
    l2 = combine_angle(l1, angle)
    v1 = directVector_1(l2)
    s1 = ray.start
    return Ray([s1, v1])

# trả về 1 ray, mà ray đó song song với một ray khác
def combine_1_ray(L):
    ray = L[0]
    start = point.rand()
    while start == ray.start:
        start = point.rand()
    return Ray([start, v])

# trả về 1 ray, mà ray đó song song với một line
def combine_1_line(L):
    line = L[0]
    v1 = directVector_1(line)
    s1 = onLine(line)
    r1 = Ray(s1, v1)
    r2 = combine_1_ray(r1)
    return r2

# trả về 1 ray, mà ray đó song song với một segment
def combine_1_segment(L):
    segment = L[0]
    v1 = directVector_2(segment)
    s1 = center(segment)
    r1 = Ray(s1, v1)
    r2 = combine_1_ray(r1)
    return r2    	
