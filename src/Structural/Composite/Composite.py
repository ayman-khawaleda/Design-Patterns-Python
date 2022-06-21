

class GraphicObject:
    def __init__(self,Color=None):
        self.Color = Color
        self.Children = []
        self._name = 'Group'

    @property
    def name(self):
        return self._name

    def _print(self,items,depth):
        items.append('*' * depth)
        if self.Color:
            items.append(self.Color)
        items.append(f'{self.name}\n')
        for child in self.Children:
            child._print(items,depth+1)
    
    def __str__(self):
        items = []
        self._print(items,0)
        return ' '.join(items)
    
class Circle(GraphicObject):
    
    @property
    def name(self):
        return 'Circle'

class Square(GraphicObject):
    
    @property
    def name(self):
        return 'Square'
        