from neural_net import NeuralNet
import math, random

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
                net.score += self.gen_score(net.output, output)
        
        for net in self.nets:
            net.score = net.score / len(inputs)
        
    def gen_score(self, a, b):
        c = 0
        for (num_a, num_b) in zip(a, b):
            #print(f"num_a {num_a}, num_b {num_b}")
            c += abs(num_a - num_b)
        
        return math.pow(5, -c)

    def get_score(self):
        self.nets.sort(key = lambda l: l.score, reverse = True)
        max_score = self.nets[1].score
        min_score = self.nets[-1].score
        avg_score = 0

        for net in self.nets:
            avg_score += net.score

        avg_score = avg_score / len(self.nets)

        return f"Max Score: {max_score}, Avg_Score: {avg_score}, Min_Score: {min_score}"
        

    def next_generation(self):
        self.nets.sort(key = lambda l: l.score, reverse = True)
        self.nets = self.nets[:len(self.nets)//4]

        new_nets = []
        for net_1 in self.nets:
            net_2 = random.choice(self.nets)
            new_nets.append(net_1.merge(net_2))
        
        len_self_nets = len(self.nets)
        for i in range(len_self_nets):
            self.nets.append(self.nets[i].evolve())
        
        for net in new_nets:
            self.nets.append(net.evolve())
        
        self.nets.extend(new_nets)
