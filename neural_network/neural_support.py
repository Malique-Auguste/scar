from math import tanh
import datetime

class Link:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight
        return self

class Node:
    def __init__(self, id) -> None:
        self.id = id
        self.input = 0.0
        self.output = 0.0
        self.init_time = datetime.datetime.now()
        pass

    def propogate(self, input):
        self.output = tanh(self.input)
