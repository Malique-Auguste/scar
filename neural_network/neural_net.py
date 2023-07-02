from neural_support import *
import sys
import random
import copy

MINIMUM = sys.float_info.min * 2
MAXIMUM = sys.float_info.max / 2

class NeuralNet:
    def __init__(self, input_num, output_num) -> None:

        self.links = []
        self.nodes = []

        self.hidden_num = 0

        for i in range(input_num):
            self.nodes.append(Node("i" + str(i), layer = MINIMUM))
        for i in range(input_num):
            self.nodes.append(Node("o" + str(i), layer = MAXIMUM))

        self.score = 0.0

    def evolve(self):
        clone = copy.deepcopy(self)
        action = random.random()

        links_present = len(self.links) > 0
        
        'Evolve link'
        if action < 0.2 or not links_present:
            print("evolving link")
            node_1 = random.choice(clone.nodes)
            node_2 = random.choice(list(filter(lambda n: n.layer != node_1.layer, clone.nodes)))
            print(f"Check link err: {node_1}, {node_2}")


            if node_1.layer < node_2.layer:
                clone.links.append(Link(node_1.id, node_2.id, random.uniform(-2, 2), node_1.layer))

            elif node_1.layer > node_2.layer:
                clone.links.append(Link(node_2.id, node_1.id, random.uniform(-2, 2), node_2.layer))
       
        #Evolve node
        elif action < 0.4:
            print("evolving node")
            old_link = random.choice(clone.links)
            old_link_index = clone.links.index(old_link)
            clone.links.remove(old_link)

            old_end_node = next(filter(lambda n: n.id == old_link.end, clone.nodes))

            new_node = Node("h" + str(clone.hidden_num), neighbour_layers = (old_link.start_layer, old_end_node.layer))
            clone.nodes.append(new_node)
            clone.hidden_num += 1

            print(f"Check node err: {old_link.start}, {new_node.id}")
            new_link_1 = Link(old_link.start, new_node.id, old_link.weight, old_link.start_layer)
            new_link_2 = Link(new_node.id, old_link.end, old_link.weight, new_node.layer)

            clone.links.insert(old_link_index, new_link_1)
            clone.links.insert(old_link_index + 1, new_link_2)

        #Evolve weight
        else:
            print("evolving weight")
            link = random.choice(clone.links)
            link.weight += random.uniform(-1, 1)
            if link.weight > 2:
                link.weight = 2
            elif link.weight < -2:
                link.weight = -2

        return clone
        
    def propogate(self, input):
        self.links.sort(key = lambda l: l.layer)
        layer = MINIMUM

        for (input_node, value) in zip(filter(lambda i_n: i_n.id.contains("i"), self.nodes), input):
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

        for output_node in filter(lambda o_n: o_n.id.contains("o"), self.nodes):
            output_node.propogate()
            self.output.append(output_node.output)

    def __str__(self) -> str:
        string = ""
        for link in self.links:
            string = string + link.__str__()  + '\n'
        for node in self.nodes:
            string = string + node.__str__() + "\n"

        return string