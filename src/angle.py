
import random
import point
import vector
import segment
import ray

from RULE import *

class Angle(object):
	"""docstring for Angle"""
	def __init__(self, L):		
		self.v1 = L[0]
		self.v2 = L[1]		
	def draw(self, name, color='black', arrow='none'):                
                self.v1.draw(color)
                self.v2.draw(color)
                
	def __str__(self):
		return "(" + str(self.v1) + ", " + str(self.v2) + ")"
def rand(L=None):
	O = point.rand()
	v1 = ray.rand()
	v2 = ray.rand()
	v2.start = O
	v1.start = O
	return Angle([v1, v2])

		
