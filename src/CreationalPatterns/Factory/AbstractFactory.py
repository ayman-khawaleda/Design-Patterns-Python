from abc import ABC, abstractmethod
from enum import Enum, auto
from operator import le, length_hint

class Beverage(ABC):
    @abstractmethod
    def consume(self):
        pass

class HotBeverage(Beverage):
    @abstractmethod
    def consume(self):
        pass

class Tea(HotBeverage):
    def consume(self):
        print('I\'m Drinking Tea')

    def __str__(self):
        return 'Tea Beverage'


class Coffee(HotBeverage):
    def consume(self):
        print('I\'m Drinking Coffe')

    def __str__(self):
        return 'Coffee Beverage'

class Moka(HotBeverage):
    def consume(self):
        print('I\'m Drinking Moka')

    def __str__(self):
        return 'Moka Beverage'

class BeverageFactory(ABC):
    @abstractmethod
    def prepare(self,amount):
        pass

class HotBeverageFactory(BeverageFactory):
    @abstractmethod
    def prepare(self,amount):
        pass

class TeaFactory(HotBeverageFactory):
    def prepare(self,amount):
        print(f'Tea is ordered with amount: {amount}')
        return Tea()
    

class CoffeeFactory(HotBeverageFactory):
    def prepare(self,amount):
        print(f'Coffee is ordered with amount: {amount}')
        return Coffee()

class MokaFactory(HotBeverageFactory):
    def prepare(self,amount):
        print(f'Moka is ordered with amount: {amount}')
        return Moka()

class HotDrinkMaker:

    factories = []

    def __init__(self,*args,**kwargs):
        for name,factory in kwargs.items():
            self.factories.append((name,factory))

    def add_beverage(self,name,factory_inestance):
        self.factories.append((name,factory_inestance))

    def make_drink(self):
        print('What would you like to drinke?\n')
        for f_num,factory in enumerate(self.factories):
            print(f'{f_num+1}.{factory[0]}')
        inp = input('Enter Your Choice: ')
        choice = int(inp)-1
        if choice<len(self.factories):
            amount = input('Enter Amount: ')
            factory_instance = self.factories[choice][1]
            beverage = factory_instance().prepare(int(amount))
            return beverage
        else:
            raise Exception('Not in list')



