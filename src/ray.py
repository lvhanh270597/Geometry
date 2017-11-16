
import random
import point

class Ray(object):

    def __init__(self, A, a, b, c):
        self.A = A
        self.a = a
        self.b = b
        self.c = c
    def  __init__(self, A):
        self.a = random.randint(1, 10)
        self.b = random.randint(1, 10)
        self.c = random.randint(1, 10)
        if (A.x == 0 and A.y == 0):
            self.c = 0
        else:
            if (A.x == 0):
                self.b = -c / A.y
            else:
                self.a = -c / A.x
        
        
