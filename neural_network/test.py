from neural_net import NeuralNet
import numpy as np

nn = NeuralNet(seed=0, shape=[2, 3, 2])
print(nn.layers)

print()
print(nn.propogate(np.array([1,0])))