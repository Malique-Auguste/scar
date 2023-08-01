from neural_support import *
import sys
import random
import copy

MINIMUM = sys.float_info.min * 2
MAXIMUM = sys.float_info.max / 2


def average_list(l):
        avg = 0
        for item in l:
            avg += item
        
        avg = avg / len(l)

        return avg

class NeuralNet:
    def __init__(self, input_num, output_num) -> None:

        self.links = []
        self.nodes = []
        self.output = []
        self.error = 0
        self.diff = 0

        self.hidden_num = 0

        for i in range(input_num):
            self.nodes.append(Node("i" + str(i), layer = MINIMUM))
        for i in range(output_num):
            self.nodes.append(Node("o" + str(i), layer = MAXIMUM))
        
        bias_node = Node("b", layer = MINIMUM)
        bias_node.output = 1
        self.nodes.append(bias_node)

    def evolve(self):
        clone = copy.deepcopy(self)
        action = random.random()

        links_present = len(self.links) > 0
        
        'Evolve link'
        if action < 0.3 or not links_present:
            #print("evolving link")
            node_1 = random.choice(clone.nodes)
            node_2 = random.choice(list(filter(lambda n: n.layer != node_1.layer, clone.nodes)))
            #print(f"Check link err: {node_1}, {node_2}")


            if node_1.layer < node_2.layer:
                clone.links.append(Link(node_1.id, node_2.id, random.uniform(-2, 2), node_1.layer))

            elif node_1.layer > node_2.layer:
                clone.links.append(Link(node_2.id, node_1.id, random.uniform(-2, 2), node_2.layer))
       
        #Evolve node
        elif action < 0.5:
            #print("evolving node")
            old_link = random.choice(clone.links)
            old_link_index = clone.links.index(old_link)
            clone.links.remove(old_link)

            old_end_node = next(filter(lambda n: n.id == old_link.end, clone.nodes))

            new_node = Node("h" + str(clone.hidden_num), neighbour_layers = (old_link.start_layer, old_end_node.layer))
            clone.nodes.append(new_node)
            clone.hidden_num += 1

            #print(f"Check node err: {old_link.start}, {new_node.id}")
            new_link_1 = Link(old_link.start, new_node.id, old_link.weight, old_link.start_layer)
            new_link_2 = Link(new_node.id, old_link.end, old_link.weight, new_node.layer)

            clone.links.insert(old_link_index, new_link_1)
            clone.links.insert(old_link_index + 1, new_link_2)

        #Evolve weight
        else:
            #print("evolving weight")
            link = random.choice(clone.links)
            link.weight += random.uniform(-1, 1)
            if link.weight > 2:
                link.weight = 2
            elif link.weight < -2:
                link.weight = -2

        return clone
    
    def remove_duplicates(self):
        i = 0
        #iterates through entire list of links and finds links with sme start and end. if found the weight is averaged and the duplicate link is removed
        while i < len(self.links):
            weights = [self.links[i].weight]

            j = 0
            while j < len(self.links):
                if i == j:
                    j += 1
                elif self.links[i].is_equivalent(self.links[j]):
                    weights.append(self.links[j].weight)
                    self.links.pop(j)
                else:
                    j += 1
            
            self.links[i].weight = average_list(weights)

            i += 1

    def merge(self, other):
        self.remove_duplicates()
        other.remove_duplicates()

        self_links_copy = self.links.copy()
        other_links_copy = other.links.copy()
  
        for o_link in other_links_copy:
            weights = [o_link.weight]
            i = 0
            while i < len(self_links_copy):
                if o_link.is_equivalent(self_links_copy[i]):
                    weights.append(self_links_copy[i].weight)
                    self_links_copy.pop(i)
                else:
                    i += 1
            
            o_link.weight = average_list(weights)
        
        other_links_copy.extend(self_links_copy)


        other_nodes_copy = other.nodes.copy()
        self_nodes_copy = self.nodes.copy()

        for o_node in other_nodes_copy:
            i = 0
            while i < len(self_nodes_copy):
                if o_node.is_equivalent(self_nodes_copy[i]):
                    self_nodes_copy.pop(i)
                else:
                    i += 1
        
        other_nodes_copy.extend(self_nodes_copy)

        nn = NeuralNet(0,0)
        nn.links = other_links_copy
        nn.nodes = other_nodes_copy

        return nn

    def get_difference_score(self, other):
        missing_nodes = 0
        
        #Creates lists of the nde ids in self and other
        s_node_ids = [node.id for node in self.nodes]
        o_node_ids = [node.id for node in other.nodes]

        #uses sets to find the unique ids (where botth sets do not overlap)
        unique_node_ids = set(s_node_ids) ^ set(o_node_ids)
        missing_nodes = len(unique_node_ids)


        missing_links = 0
        #Creates lists of the node ids in self and other
        s_link_data = [(link.start, link.end) for link in self.links]
        o_link_data = [(link.start, link.end) for link in other.links]


        #uses sets to find the unique ids (where botth sets do not overlap)
        unique_link_data = set(s_link_data) ^ set(o_link_data)
        missing_links = len(unique_link_data)
        
        return missing_links + missing_nodes


    def propogate(self, input):
        self.links.sort(key = lambda l: l.start_layer)
        layer = MINIMUM

        for node in self.nodes:
            node.input = 0

        for (input_node, value) in zip(filter(lambda i_n: 'i' in i_n.id, self.nodes), input):
            input_node.output = value 

        end_nodes = []
        for link in self.links:
            if layer != link.start_layer:
                for node in end_nodes:
                    node.propogate()
                
                end_nodes = []

            start_node = next(filter(lambda n: n.id == link.start, self.nodes))
            end_node = next(filter(lambda n: n.id == link.end, self.nodes))
            end_node.update_input(start_node.output, link.weight)
            end_nodes.append(end_node)

        for output_node in filter(lambda o_n: 'o' in o_n.id, self.nodes):
            self.output = []
            output_node.propogate()
            self.output.append(output_node.output)

    def __str__(self) -> str:
        string = ""
        for link in self.links:
            string = string + link.__str__()  + '\n'
        for node in self.nodes:
            string = string + node.__str__() + "\n"

        string = string + f"Outputs: {self.output}" + "\n"
        string = string + f"Error: {self.error}" + "\n"
        string = string + f"Diff: {self.diff}" + "\n"


        return string