
import random

class Vector(object):
	"""docstring for Vector"""
	def __init__(self, a, b):		
		self.a = a
		self.b = b
	def __str__(self):
		return "(" + str(a) + ", " + str(b) + ")"

def rand(s = 1, t = 10):
	a = random.randint(s, t)
	b = random.randint(s, t)
	while a == 0 and b == 0:
		a = random.randint(s, t)
		b = random.randint(s, t)
	return Vector(a, b)
	
# trả về vector chỉ phương của đường thẳng
def directVector_1(line):
    	return Vector(b, -a)

# trả về vector chỉ phương của đoạn thẳng
def directVector_2(segment)
	return Vector(end.x-begin.x, (end.y-begin.y))
