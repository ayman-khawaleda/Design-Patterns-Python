import random
from .Singleton import Singleton

@Singleton
class DB:
    def __init__(self,*args,**kwargs):
        print(args)
        print('id: ',random.randint(1,101))