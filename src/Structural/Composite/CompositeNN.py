from abc import ABC
from collections.abc import Iterable

class Connectable(Iterable,ABC):
    def connect_to(self,other):
        if self == other:
            return
        for x in self:
            for y in other:
                x.outputs.append(y)
                y.inputs.append(x)

class Neuron(Connectable):
    def __init__(self,name):
        self.name = name
        self.inputs = []
        self.outputs = []

    def __str__(self):
        return f'{self.name}, Input len :{len(self.inputs)}, Output len :{len(self.outputs)}'

    def __iter__(self):
        yield self

class NeuronLayer(list,Connectable):
    def __init__(self,name,count):
        super().__init__()
        self.name = name
        for x in range(count):
            self.append(Neuron(f"{name}-{x}"))
        
    def __str__(self):
        return f'{self.name} wiht {len(self)} Neurons'
    
