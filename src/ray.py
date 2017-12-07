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
	l1 = convertRay(ray)
	l2 = combine_angle(l1, angle)
	v1 = directVector_1(l2)
	s1 = ray.start
	return Ray(s1, v1)

# trả về 1 ray, mà ray đó song song với một ray khác
def combine_1_ray(ray):
	start = point.rand()
	while start == ray.start:
    	start = point.rand()
	return Ray(start, v)

# trả về 1 ray, mà ray đó song song với một line
def combine_1_line(line):
	v1 = directVector_1(line)
	s1 = onLine(line)
	r1 = Ray(s1, v1)
	r2 = combine_1_ray(r1)
	return r2

# trả về 1 ray, mà ray đó song song với một segment
def combine_1_segment(segment):
	v1 = directVector_2(segment)
	s1 = center(segment)
	r1 = Ray(s1, v1)
	r2 = combine_1_ray(r1)
	return r2    	
