
import random
import point
import vector

class Angle(object):
	"""docstring for Angle"""
	def __init__(self, O, v1, v2):	
		self.O = O	
		self.v1 = v1
		self.v2 = v2
	def __str__(self):
		return "(" + str(self.O) + ", " + str(self.v1) + ", " + str(self.v2) + ")"
def rand():
	O = point.rand()
	v1 = vector.rand()
	v2 = vector.rand()
	return Angle(O, v1, v2)

		