
import random
import point

class Segment(object):

    def __init__(self, A, B):
        self.A = A
        self.B = B

    def __str__(self):
        return self.A.__str__() + '--' + self.B.__str__()
        
