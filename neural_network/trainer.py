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
            net.error = 0

            for (input, output) in zip(inputs, outputs):
                net.propogate(input)
                net.error += self.gen_error(net.output, output)
        
        for net in self.nets:
            net.error = net.error / len(inputs)
        
    def gen_error(self, a, b):
        c = 0
        for (num_a, num_b) in zip(a, b):
            #print(f"num_a {num_a}, num_b {num_b}")
            c += abs(num_a - num_b)
        
        #return math.pow(5, -c)
        return c

    def get_error(self):
        self.nets.sort(key = lambda l: l.error)
        max_error = self.nets[1].error
        min_error = self.nets[-1].error
        avg_error = 0

        for net in self.nets:
            avg_error += net.error

        avg_error = avg_error / len(self.nets)

        return f"Max Error: {max_error}, Avg_error: {avg_error}, Min_Error: {min_error}"
        

    def next_generation(self):
        self.nets.sort(key = lambda l: l.error)
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
