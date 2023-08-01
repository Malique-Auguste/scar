from neural_net import NeuralNet
import math, random



ORGANISMS_PER_SPECIES = 3

def print_species(species):
        for specie in species:
            print("specie:")
            for nn in specie:
                print(nn)


class Trainer:
    def __init__(self, num_species, input_num, output_num):
        self.num_species = num_species
        self.nets = []
        for i in range(self.num_species * ORGANISMS_PER_SPECIES):
            net = NeuralNet(input_num, output_num)
            self.nets.append(net.evolve().evolve())
    
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

        '''
        Creates a list of species. 
        The species are identified by their structural differences from the network with the least error.
        After determining their differences and subsequentally sorting them, ever nth net is used as the basis of that species.
        '''

        species = []
        i = 0
        while i < self.num_species and len(self.nets) > 0:
            if i == 0:
                species.append([self.nets.pop(0)])
            else:
                species.append([self.nets.pop()])

            for net in self.nets:
                net.diff = species[i][0].get_difference_score(net)
            
            self.nets.sort(key = lambda l: l.diff)

            while len(self.nets) > 0 and self.nets[0].diff == 0:
                species[i].append(self.nets.pop(0))

            i += 1
        

        while len(self.nets) > 0:
            diff = []
            net = self.nets.pop(0)
            for specie in species:
                diff.append(net.get_difference_score(specie[0]))
            
            min_diff = min(diff)

            species[diff.index(min_diff)].append(net)
        
        print_species(species)



    """
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
    """

    
