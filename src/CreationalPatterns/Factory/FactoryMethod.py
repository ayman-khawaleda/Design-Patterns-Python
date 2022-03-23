from math import cos, sin

class Point:
    def __init__(self,a,b):
        self.x = a
        self.y = b

    def __str__(self):
        return f'X:{self.x}, Y:{self.y}'

class PointFactory:
    @staticmethod
    def new_cartesian_point(x,y):
        return Point(x,y)
    
    @staticmethod
    def new_polar_point(rho,theta):
        return Point(rho * cos(theta),rho * sin(theta))
