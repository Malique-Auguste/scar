from numpy.random import default_rng
import numpy as np

class NeuralNet:

    def __init__(self, seed, shape) -> None:
        rng = default_rng(seed)

        self.layers = []

        i = 0
        while i < len(shape):
            if i == 0:
                input_size = shape[0]
            else:
                self.layers.append(rng.random((shape[i-1], shape[i])))
            
            i += 1
        
    def propogate(self, input):
        i = 0
        output = input
        while i < len(self.layers):
            output = np.dot(output, self.layers[i])
            i += 1
        
        return output



