import numpy as np

class NeuralNet:
    def __init__(self, input_nodes_num, hidden_layer_num, hidden_nodes_num, output_nodes_num) -> None:
        #creates an array that will hold input data and bias node from the sensors
        self.input = np.ones(input_nodes_num + 1)

        #creates an array that will hold the weights for each hidden layer
        #each layer is of size (previous layer, numver of hidden layer nodes)
        self.hidden_weights = []

        #populates array with random weights for the hidden layer
        #additionall row created for bias weight
        for i in range(hidden_layer_num):
            if i == 0:
                self.hidden_weights.append(np.random.uniform(-2, 2, (input_nodes_num + 1, hidden_nodes_num)))
            else:
                self.hidden_weights.append(np.random.uniform(-2, 2, (hidden_nodes_num + 1, hidden_nodes_num)))

        #populates array with random weights for the output layer
        self.output_weights = np.random.uniform(-2, 2, (hidden_nodes_num + 1, output_nodes_num))

        #creates an array that will hold output data for the motors
        self.output = np.ones(output_nodes_num)

    def propogate(self, input):
        #adds on 1 bias node to the input
        input = np.hstack((input, np.ones(1)))

        #saves a copy of the input in the neural net
        self.input = input.copy()

        #a temporary vairable to hold the output of layer propogation
        temp = input
        for layer in self.hidden_weights:
            #multiplies previous output with weights of the current layer
            temp = temp.dot(layer)

            #adds on 1 bias node to the output
            temp = np.hstack((temp, np.ones(1)))
        
        self.output = temp.dot(self.output_weights)




    def __str__(self) -> str:
        string = f"Input: \n{self.input}\n\nHidden Weights:\n{self.hidden_weights}\n\nOutput Weights:\n{self.output_weights}\n\nOutput:{self.output}"
        return string