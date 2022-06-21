class Item:
    def __init__(self,name,color,size):
        self.name = name
        self.color = color
        self.size = size
    
    def __str__(self):
        return f'{self.name}:{self.color}-{self.size}'