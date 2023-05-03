from neural_net import NeuralNet
from trainer import Trainer
import numpy as np

"""
nn = NeuralNet(shape=[2, 3, 1])
print(nn.layers)
print(nn.evolve().layers)

"""
i = 0
nns = []
while i < 10:
    nns.append(NeuralNet(shape=[2, 3, 1]))
    i += 1


inputs = [np.array([0,0]), np.array([0,1]), np.array([1,0]), np.array([1,1])]
outputs = [np.array([0]), np.array([1]), np.array([1]), np.array([0])]

trainer = Trainer(nns, inputs, outputs)

i = 0
while i < 10:
    print()

    """
    for net in trainer.networks:
        print(net.layers)
    """

    trainer.propogate()
    trainer.scores()
    trainer.evolve()

    i += 1

trainer.test()
