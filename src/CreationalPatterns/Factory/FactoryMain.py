from CreationalPatterns.Factory.AbstractFactory import *

def main():
    hdm = HotDrinkMaker(Tea=TeaFactory,Moka=MokaFactory)
    hdm.add_beverage('Coffee',CoffeeFactory)
    beverage = hdm.make_drink()

    beverage.consume()