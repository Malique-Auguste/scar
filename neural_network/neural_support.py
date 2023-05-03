from math import tanh

class Link:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        return self

class Neuron:
    def __init__(self, id, weight, links) -> None:
        self.id = id
        self.weight = weight
        self.links = links
        self.output = 0.0
        pass

    def propogate(self, input):
        self.output = tanh(self.input)
