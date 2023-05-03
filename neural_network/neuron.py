from math import tanh

class neuron:
    def __init__(self, id, weight) -> None:
        self.id = id
        self.weight = weight
        self.output = 0.0
        pass

    def propogate(self, input):
        self.output = tanh(self.input)
