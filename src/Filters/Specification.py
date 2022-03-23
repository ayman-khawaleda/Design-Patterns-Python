from abc import ABCMeta,abstractmethod

class Specification(metaclass=ABCMeta):
    @abstractmethod
    def is_satisfied(self,item):
        pass

class ColorSpecification(Specification):

    def __init__(self,color):
        self.color = color

    def is_satisfied(self,item):
        return self.color == item.color

class SizeSpecification(Specification):

    def __init__(self,size):
        self.size = size

    def is_satisfied(self,item):
        return self.size == item.size

class AndSpecification(Specification):
    def __init__(self,*args,**kwargs):
        self.args = args

    def is_satisfied(self,item):
        return all([spec.is_satisfied(item) for spec in self.args])

class OrSpecification(Specification):
    def __init__(self,*args,**kwargs):
        self.args = args
    
    def is_satisfied(self,item):
        return any([spec.is_satisfied(item) for spec in self.args])