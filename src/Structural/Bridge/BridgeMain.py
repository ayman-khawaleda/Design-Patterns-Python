from Structural.Bridge.Bridge import *

def main():
    red = Red()
    green = Green()
    blue = Blue()

    circle = Circle(9,red)
    rectangle = Rectangle(5,10,green)
    rectangle1 = Rectangle(5,10,blue)

    circle.draw()
    rectangle.draw()
    rectangle1.draw()