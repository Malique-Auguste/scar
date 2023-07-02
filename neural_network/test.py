from neural_net import NeuralNet
from neural_support import *
from trainer import Trainer
import sys

nn = NeuralNet(2,2)

for i in range(22):
    nn = nn.evolve() 
    if i%3 == 0:
        sys.stdout.flush()
        print(nn)
        sys.stdout.flush()