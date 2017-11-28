
import random
import point
import vector

class Ray(object):
    def __init__(self, S, v):
        self.start = S
        self.v = v
    def __str__(self):
    	return "(" + str(self.start) + ", " + str(v) + ')'    	
    
# return a random ray    
def rand():
	start = point.rand()
	v = vector.rand()
	return Ray(start, v)

# trả về 1 ray, cái ray đó nó tạo với ray khác một góc cho trước
def combine_angle(ray, angle):

# trả về 1 ray, mà ray đó song song với một ray khác
def combine_1_ray(ray):

# trả về 1 ray, mà ray đó song song với một line
def combine_1_line(line):

# trả về 1 ray, mà ray đó song song với một segment
def combine_1_segment(segment):
