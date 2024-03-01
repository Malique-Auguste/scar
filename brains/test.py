import numpy as np
from neural_net import NeuralNet

np.random.seed = 1

nn = NeuralNet(3, 2, 2, 2)
print(nn)
print("\n---\n")

nn.propogate(np.array([0,0,0]))
print(nn)
