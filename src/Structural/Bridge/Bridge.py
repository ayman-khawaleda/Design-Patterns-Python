from abc import ABC, abstractmethod
class color(ABC):
    @abstractmethod
    def coloring(self):pass

class Red(color):
    def coloring(self):
        return 'Red'
    
class Blue(color):
    def coloring(self):
        return 'Blue'
    
class Green(color):
    def coloring(self):
        return 'Green'

class Shape(ABC):
    def __init__(self,color):
        self.color = color
    
    @abstractmethod
    def draw(self):pass
    @abstractmethod
    def resize(self,factor):pass

class Circle(Shape):
    def __init__(self,radius,color):
        super(Circle,self).__init__(color)
        self.radius = radius
    
    def draw(self):
        print(f'Drawing Circle With Color ' + self.color.coloring())
    
    def resize(self,factor):
        self.radius *= factor
    
class Rectangle(Shape):
    def __init__(self,w,h,color):
        super(Rectangle,self).__init__(color)
        self.w = w
        self.h = h

    def draw(self):
        print(f'Drawing Rectangle With Color ' + self.color.coloring())
    
    def resize(self,factor):
        self.w *= factor
        self.h *= factor 

