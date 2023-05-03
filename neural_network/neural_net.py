from numpy.random import default_rng
import numpy as np
import copy

class NeuralNet:
    rng = default_rng(1)

    def __init__(self, shape) -> None:

        self.layers = []

        i = 0
        while i < len(shape):
            if i > 0:
                self.layers.append(self.rng.random((shape[i-1], shape[i])))
            
            i += 1

        self.score = 0.0

    def evolve(self):
        clone = copy.deepcopy(self)
        for layer in clone.layers:
            row = 0
            while row < len(layer):
                column = 0
                while column < len(layer[row]):
                    if NeuralNet.rng.choice([True, False]):
                        layer[row, column] += NeuralNet.rng.uniform(-0.5, 0.5)
                    
                    column += 1
                row += 1
        
        return clone
        
    def propogate(self, input):
        i = 0
        output = input
        while i < len(self.layers):
            output = np.dot(output, self.layers[i])
            output = np.tanh(output)
            i += 1
        
        return output
    
    def __lt__(self, other):
         return self.score < other.score



