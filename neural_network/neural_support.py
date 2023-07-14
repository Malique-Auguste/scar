from math import tanh
import datetime

#This class represents connections between nodes
class Link:
    def __init__(self, start, end, weight, start_layer):
        self.start = start
        self.end = end
        self.weight = weight
        self.start_layer = start_layer
    
    def is_equivalent(self, other):
        return self.start == other.start and self.end == other.end 
    
    def __str__(self) -> str:
        return f"{self.start} --({self.weight})-> {self.end} (layer: {self.start_layer})"

#This represents a point in the neural net at which computations take place
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
        else:
            raise "layer not provided for node"

    def update_input(self, input, weight):
        self.input += input * weight

    def propogate(self):
        self.output = tanh(self.input)

    def is_equivalent(self, other):
        return self.id == other.id

    def __str__(self) -> str:
        return f"Id: {self.id}, Input: {self.input}, Output: {self.output} (layer: {self.layer})"
