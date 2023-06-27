from neural_support import *
import random
import copy

class NeuralNet:
    def __init__(self, input_num, output_num) -> None:

        self.links = []
        self.nodes = []

        self.input_num = input_num
        self.output_num = output_num
        self.hidden_num = 0

        self.score = 0.0

    def evolve(self):
        clone = copy.deepcopy(self)
        action = random.random()
        
        'Evolve hidden link'
        if action < 0.1:
            nodes = random.choices(clone.nodes, k = 2)
            if nodes[0].init_time < nodes[1].init_time:
                clone.links.append(Link(nodes[0].id, nodes[1].id, random.uniform(-2, 2)))

            elif nodes[0].init_time > nodes[1].init_time:
                clone.links.append(Link(nodes[1].id, nodes[0].id, random.uniform(-2, 2)))

        #Evolve input link
        elif action < 0.2:
            node = random.choice(clone.nodes)
            input_id =  "i" + random.randrange(0, clone.input_num)
            clone.links.append(Link(input_id, node.id, random.uniform(-2, 2)))

        #Evolve output link
        elif random.random() < 0.3:
            node = random.choice(clone.nodes)
            output_id =  "o" + random.randrange(0, clone.output_num)
            clone.links.append(Link(node.id, output_id, random.uniform(-2, 2)))
        
        #Evolve node
        elif random.random() < 0.5:
            old_link = random.choice(clone.links)
            old_link_index = clone.links.index(old_link)
            clone.links.remove(old_link)

            new_node = Node(clone.output_num)
            clone.nodes.append(new_node)
            clone.output_num += 1

            new_link_1 = Link(old_link.start, new_node.id, old_link.weight)
            new_link_2 = Link(new_node.id, old_link.end, old_link.weight)

            clone.links.insert(old_link_index, new_link_1)
            clone.links.insert(old_link_index + 1, new_link_2)

        #Evolve weight
        else:
            link = random.choice(clone.links)
            link.weight += random.uniform(-1, 1)
            if link.weight > 2:
                link.weight = 2
            elif link.weigt < -2:
                link.weight = -2

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



