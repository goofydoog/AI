import numpy as np

class Neuron:
    def __init__(self, n_inputs, bias=0., weights=None):
        self.b = bias
        if weights:
            self.ws = np.array(weights)
        else:
            self.ws = np.random.rand(n_inputs)
        self.input = None
        self.output = None
        self.gradient = None

    def _f(self, x):
        return max(0.1 * x, x) 

    def _df(self, x):
        return 0.1 if x < 0 else 1.0  

    def forward(self, xs):
        self.input = xs
        self.output = self._f(xs @ self.ws + self.b)
        return self.output

    def backward(self, output_gradient):
        local_gradient = self._df(self.input @ self.ws + self.b)
        self.gradient = output_gradient * local_gradient
        return self.gradient

    def update(self, lr):
        self.ws -= lr * self.input * self.gradient
        self.b -= lr * self.gradient

class NeuralNetwork:
    def __init__(self):
        self.input_layer = [Neuron(3) for _ in range(3)]
        self.hidden_layer1 = [Neuron(3) for _ in range(4)]
        self.hidden_layer2 = [Neuron(4) for _ in range(4)]
        self.output_layer = Neuron(4)

    def forward(self, inputs):
        h1_outputs = np.array([neuron.forward(inputs) for neuron in self.hidden_layer1])
        h2_outputs = np.array([neuron.forward(h1_outputs) for neuron in self.hidden_layer2])
        output = self.output_layer.forward(h2_outputs)
        return output

    def backward(self, y, y_pred):
        output_gradient = 2 * (y_pred - y)  # MSE derivative
        gradient = self.output_layer.backward(output_gradient)
        gradients_h2 = np.array([neuron.backward(gradient) for neuron in self.hidden_layer2])
        gradient = gradients_h2.sum(axis=0)
        gradients_h1 = np.array([neuron.backward(gradient) for neuron in self.hidden_layer1])
        gradient = gradients_h1.sum(axis=0)

    def update(self, lr):
        self.output_layer.update(lr)
        for neuron in self.hidden_layer2:
            neuron.update(lr)
        for neuron in self.hidden_layer1:
            neuron.update(lr)

    def train(self, inputs, y_true, lr):
        y_pred = self.forward(inputs)
        self.backward(y_true, y_pred)
        self.update(lr)


network = NeuralNetwork()
inputs = np.array([
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 0],
    [1, 1, 0],
    [1, 0, 1],
    [1, 1, 1],
])  
y_true = np.array([0, 1, 0, 1, 1, 0])  

# Trening sieci
for epoch in range(10000):
    for x, y in zip(inputs, y_true):
        network.train(x, y, lr=0.01)


outputs = np.array([network.forward(x) for x in inputs])
print("Inputs:\n", inputs)
print("Expected Outputs:\n", y_true)
print("Predicted Outputs:\n", outputs)
