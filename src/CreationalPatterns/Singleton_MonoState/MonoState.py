class MonoState:
    __shared_data = {}

    def __new__(cls,*args,**kwargs):
        obj = super(MonoState, cls).__new__(cls,*args,**kwargs)
        obj.__dict__ = cls.__shared_data
        return obj
    
class CFO(MonoState):
    def __init__(self):
        self.name = ''
        self.money_managed = 0

    def __str__(self):
        return f'Name: {self.name}, Money Managed: {self.money_managed}'

