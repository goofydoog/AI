import numpy as np
import matplotlib.pyplot as plt


class Neuron:
    def __init__(self, n_inputs, bias=0., weights=None):
        self.b = bias
        if weights:
            self.ws = np.array(weights)
        else:
            self.ws = np.random.rand(n_inputs)

    def _f(self, x): 
        return max(x * .1, x)

    def __call__(self, xs):  
        return self._f(xs @ self.ws + self.b)


class NeuralNetwork:
    def __init__(self):
        self.input_layer = [Neuron(3) for _ in range(3)]
        self.hidden_layer1 = [Neuron(3) for _ in range(4)]
        self.hidden_layer2 = [Neuron(4) for _ in range(4)]
        self.output_layer = Neuron(4)

    def __call__(self, inputs):
        h1_outputs = np.array([neuron(inputs) for neuron in self.hidden_layer1])
        h2_outputs = np.array([neuron(h1_outputs) for neuron in self.hidden_layer2])
        output = self.output_layer(h2_outputs)
        return output


network = NeuralNetwork()

def visualize_network():
    fig, ax = plt.subplots(figsize=(10, 6))

    input_layer_x = 1
    input_layer_y = [0.5, 1.5, 2.5]  
    for i in range(3):
        ax.plot([input_layer_x], [input_layer_y[i]], 'ro', markersize=20)
        ax.text(input_layer_x - 0.5, input_layer_y[i], f'Input {i + 1}', ha='right', va='center', fontsize=12)

    hidden_layer1_x = 2
    for i in range(4):
        ax.plot([hidden_layer1_x], [i], 'bo', markersize=20)

    hidden_layer2_x = 3
    for i in range(4):
        ax.plot([hidden_layer2_x], [i], 'bo', markersize=20)

    output_layer_x = 4
    ax.plot([output_layer_x], [1.5], 'go', markersize=20)
    ax.text(output_layer_x + 0.5, 1.5, 'Output', ha='left', va='center', fontsize=12, color='green')

    for i in range(3):
        for j in range(4):
            ax.arrow(input_layer_x, input_layer_y[i], hidden_layer1_x - input_layer_x - 0.1, j - input_layer_y[i],
                     head_width=0.1, head_length=0.1, fc='k', ec='k')
    for i in range(4):
        for j in range(4):
            ax.arrow(hidden_layer1_x, i, hidden_layer2_x - hidden_layer1_x - 0.1, j - i, head_width=0.1,
                     head_length=0.1, fc='k', ec='k')
            ax.arrow(hidden_layer2_x, i, output_layer_x - hidden_layer2_x - 0.1, 1.5 - i, head_width=0.1,
                     head_length=0.1, fc='k', ec='k')

    ax.text(hidden_layer1_x, -0.5, 'Hidden Layer 1', ha='center', va='center', fontsize=12, color='blue')
    ax.text(hidden_layer2_x, -0.5, 'Hidden Layer 2', ha='center', va='center', fontsize=12, color='blue')

    ax.set_xlim(0, 5)
    ax.set_ylim(-1, 4)
    ax.axis('off')
    plt.show()


visualize_network()
