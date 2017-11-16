
import random

class Line(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def  __init__(self):
        self.a = random.randint(0, 10)
        self.b = random.randint(0, 10)
        while (self.a == 0 and self.b == 0):
            self.a = random.randint(0, 10)
            self.b = random.randint(0, 10)
        
