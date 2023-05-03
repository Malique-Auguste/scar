from neural_net import NeuralNet
import numpy as np

class Trainer:
    def __init__(self, networks, inputs, outputs):
        self.networks = networks
        self.inputs = inputs
        self.outputs = outputs
    
    def propogate(self):
        for network in self.networks:
            network.score = 0.0

        data = (self.inputs, self.outputs)
        for network in self.networks:
            i = 0
            while i < len(self.inputs):
                score = np.absolute(np.sum(self.outputs[i] - network.propogate(self.inputs[i])))
                network.score += score
                i += 1

            network.score = network.score / (len(self.inputs) + 1)
        
    
    def scores(self, max = False):
        self.networks.sort()
        if max:
            print(f"Max Score: {self.networks[0].score}")
        else:
            print("Scores:")
            for network in self.networks:
                print(network.score)

    def evolve(self):
        self.networks.sort()
        max_size = len(self.networks)
        self.networks = self.networks[: int(len(self.networks) / 2)]

        i = 0
        while len(self.networks) < max_size:
            self.networks.append(self.networks[i].evolve())
            i += 1

    def test(self):
        self.networks.sort()
        print(f"Input: {self.inputs}")
        print(f"Outputs: {self.outputs}")

        print("Layers:")
        for layer in self.networks[0].layers:
            print(layer)

        print(f"Score: {self.networks[0].score}")

        i = 0
        while i < len(self.inputs):
            print(i)
            print(self.networks[0].propogate(self.inputs[i]))
            i += 1
