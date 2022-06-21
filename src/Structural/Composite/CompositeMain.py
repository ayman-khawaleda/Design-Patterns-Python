from Structural.Composite.CompositeNN import Neuron, NeuronLayer

def main():
    n1 = Neuron('n1')
    n2 = Neuron('n2')
    nlayer1 = NeuronLayer('L1',3)
    nlayer2 = NeuronLayer('L2',4)

    n1.connect_to(n2)
    n1.connect_to(nlayer1)
    nlayer1.connect_to(n2)
    nlayer1.connect_to(nlayer2)

    print(n1)
    print(n2)
    print(nlayer1)
    print(nlayer2)
