from tokenize import group
from Structural.Composite import *
from Structural.Composite.Composite import Circle, GraphicObject, Square

def main():
    drawing = GraphicObject()
    drawing._name = 'Basic Draw'
    drawing.Children.append(Square('Red'))
    drawing.Children.append(Circle('Green'))
    
    groupObj = GraphicObject('Yellow')
    groupObj.Children.append(Circle('Pink'))
    groupObj.Children.append(Square('Purple'))
    drawing.Children.append(groupObj)

    print(drawing)
