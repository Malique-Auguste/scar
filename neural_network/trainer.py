from neural_net import NeuralNet
import math

class Trainer:
    def __init__(self, net_num, input_num, output_num):
        self.nets = []
        net = NeuralNet(input_num, output_num)
        for i in range(net_num):
            self.nets.append(net.evolve())
    
    def propogate(self, inputs, outputs):
        for net in self.nets:
            net.score = 0
            for node in net.nodes:
                node.input = 0
        
        for (input, output) in zip(inputs, outputs):
            for net in self.nets:
                net.propogate(input)
                net.score += self.get_score(net.output, output)
        
        for net in self.nets:
            net.score = net.score / len(inputs)

        self.nets.sort(key = lambda l: l.score, reverse = True)
        
    def get_score(self, a, b):
        c = 0
        for (num_a, num_b) in zip(a, b):
            #print(f"num_a {num_a}, num_b {num_b}")
            c += abs(num_a - num_b)
        
        return math.pow(5, -c)
