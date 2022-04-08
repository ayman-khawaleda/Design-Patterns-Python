import random
from re import S
from .Singleton import Singleton

class DB(metaclass=Singleton):
    def __init__(self,*args,**kwargs):
        print(args)
        print('id: ',random.randint(1,101))