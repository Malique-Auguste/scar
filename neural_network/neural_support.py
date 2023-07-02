from math import tanh
import datetime

class Link:
    def __init__(self, start, end, weight, start_layer):
        self.start = start
        self.end = end
        self.weight = weight
        self.start_layer = start_layer
    
    def __str__(self) -> str:
        return f"{self.start} --({self.weight})-> {self.end} (layer: {self.start_layer})"

class Node:
    def __init__(self, id, **kwargs):
        self.id = id
        self.input = 0.0
        self.output = 0.0

        if kwargs.get("layer") != None:
            self.layer = kwargs.get("layer")
        elif kwargs.get("neighbour_layers") != None:
            (a, b) = kwargs.get("neighbour_layers")
            self.layer = (a + b) / 2

    def update_input(self, input, weight):
        self.input += input * weight

    def propogate(self):
        self.output = tanh(self.input)

    def __str__(self) -> str:
        return f"Id: {self.id}, Input: {self.input}, Output: {self.output} (layer: {self.layer})"
