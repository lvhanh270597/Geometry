import random
import segment
import math

class Vector(object):
	"""docstring for Vector"""
	def __init__(self, L):
		self.a = L[0]
		self.b = L[1]	
	def __str__(self):
		return "(" + str(a) + ", " + str(b) + ")"

def rand(L = None):
        s = 0
        t = 100
        a = random.randint(s, t)
        b = random.randint(s, t)
        while a == 0 and b == 0:
                a = random.randint(s, t)
                b = random.randint(s, t)
        return Vector([a, b])

def make_from_two_points(A, B):
        seg = segment.Segment([A, B])
        return directVector_2([seg])

def size(v):
        return math.sqrt(v.a ** 2 + v.b ** 2)
# trả về vector chỉ phương của đường thẳng
def directVector_1(L):
        line = L[0]
        return Vector([line.b, -line.a])

# trả về vector chỉ phương của đoạn thẳng
def directVector_2(L):
        segment = L[0]
        return Vector([segment.end.x-segment.begin.x,
                       segment.end.y-segment.begin.y])
