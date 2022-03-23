from abc import ABCMeta,abstractmethod


class Filter(metaclass = ABCMeta):
    
    @abstractmethod
    def filter(self,items,specification):
        pass

class SingleSpecificationFilter(Filter):
    
    def filter(self,items,specification):
        for item in items:
            if specification.is_satisfied(item):
                yield item

