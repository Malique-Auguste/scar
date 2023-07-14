from neural_net import NeuralNet, average_list
from neural_support import *
from trainer import Trainer
import sys, copy

MINIMUM = sys.float_info.min * 2
MAXIMUM = sys.float_info.max / 2

if False:
    print("\n---\n")

    nn = NeuralNet(2,2)
    for i in range(13):
        nn = nn.evolve() 
        if i%3 == 0:
            sys.stdout.flush()
            print(nn)
            sys.stdout.flush()

if False:
    print("\n---\n")

    nn = NeuralNet(2, 2)
    nn.nodes.append(Node("h0", neighbour_layers = (MINIMUM, MAXIMUM)))
    print(nn)

    links = []
    links.append(Link("i0", "o0", 1, MINIMUM))
    links.append(Link("h0", "o1", 1, (MINIMUM + MAXIMUM) / 2))
    links.append(Link("i0", "h0", 1, MINIMUM))
    links.append(Link("i1", "h0", 1, MINIMUM))
    nn.links = links

    nn.propogate([1, 1])
    if nn.output == [0.7615941559557649, 0.7460679984455996]:
        print("propogation successful")
    else:
        print(f"propogation failure: {nn.output}")

if False:
    trainer = Trainer(5, 2, 1)
    trainer.propogate([[1, 1], [1, 0], [0, 1], [0, 0]], [[1], [1], [0], [0]])
    for net in trainer.nets:
        print(f"Score: {net.score}")

if False:
    nn1 = NeuralNet(2, 2)
    nn2 = NeuralNet(2, 2)

    nn1.links.append(Link("i0", "o0", 1, MINIMUM))
    nn1.links.append(Link("i1", "o1", -1.7, MINIMUM))

    nn2.nodes.append(Node("h0", neighbour_layers = (MINIMUM, MAXIMUM)))
    nn2.links.append(Link("h0", "o1", 1, (MINIMUM + MAXIMUM) / 2))
    nn2.links.append(Link("i0", "o0", 2, MINIMUM))
    nn2.links.append(Link("i0", "h0", 1, MINIMUM))

    nn3 = nn1.merge(nn2)

    print(nn3)

if False:
    l = [1, 2, 3, 4]
    print(average_list(l))

if False:
    nn2 = NeuralNet(1, 1)
    nn2 = nn2.evolve()
    nn2 = nn2.evolve()
    nn2 = nn2.evolve()
    nn2 = nn2.evolve()

    nn2_link = copy.deepcopy(nn2.links[0])
    nn2.links.append(nn2_link)

    print(f"\nNN2: \n{nn2}")
    sys.stdout.flush()

    nn2.remove_duplicates()
    print(f"\nNN2: \n{nn2}")
    sys.stdout.flush()




if True:
    nn1 = NeuralNet(2, 1)
    nn1 = nn1.evolve()
    nn1 = nn1.evolve()
    nn1 = nn1.evolve()
    nn1_link = copy.deepcopy(nn1.links[0])
    nn1.links.append(nn1_link)

    nn2 = NeuralNet(2, 1)
    nn2 = nn2.evolve()
    nn2 = nn2.evolve()
    nn2 = nn2.evolve()
    nn2_link = copy.deepcopy(nn2.links[0])
    nn2.links.append(nn2_link)
  

    print(f"NN1: \n{nn1}")
    print(f"\nNN2: \n{nn2}")

    nn3 = nn1.merge(nn2)
    print(f"\nNN3: \n{nn3}")


