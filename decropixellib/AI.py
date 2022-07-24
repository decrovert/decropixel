import typing
import random; random.seed()
import json

class Neuron:
    def __init__(self, stimulation: float, bias: float):
        self.stimulation = stimulation
        self.bias = bias

class NeuralNetwork:
    def __init__(self, IMAGE_WIDTH: typing.Sized, IMAGE_HEIGHT: typing.Sized, NETWORK_SIZE: typing.Sized, DATA_FILE_NAME: str):
        self.IMAGE_WIDTH = IMAGE_WIDTH
        self.IMAGE_HEIGHT = IMAGE_HEIGHT
        self.NETWORK_SIZE = NETWORK_SIZE
        self.DATA_FILE_NAME = DATA_FILE_NAME
        del IMAGE_WIDTH, IMAGE_HEIGHT, NETWORK_SIZE, DATA_FILE_NAME

        self.IMAGE_SIZE = self.IMAGE_WIDTH * self.IMAGE_HEIGHT

        self.layers = []
        self.connections = []

        try:
            with open(self.DATA_FILE_NAME, "r") as data_file:
                data_file_json = data_file.read()
                data_structure = json.loads(data_file_json)
                del data_file_json

                bias_index: typing.Sized = 0

                for i in range(self.NETWORK_SIZE):
                    self.layers.append([])
                
                    for _ in range(self.IMAGE_SIZE):
                        self.layers[i].append(Neuron(0.0, data_structure[0][bias_index]))
                        bias_index += 1
                
                del bias_index

                for i in range((len(self.layers) - 1) * (self.IMAGE_SIZE ** 2)):
                    self.connections.append(data_structure[1][i])
        except:
            self.layers = []
            self.connections = []

            for i in range(self.NETWORK_SIZE):
                self.layers.append([])
                
                for _ in range(self.IMAGE_SIZE):
                    self.layers[i].append(Neuron(0.0, random.random() * 2 - 1))

            for i in range((len(self.layers) - 1) * (self.IMAGE_SIZE ** 2)):
                self.connections.append(random.random() * 2 - 1)
    
    def populate_input_neurons(self) -> None:
        for i in range(self.IMAGE_SIZE):
            self.layers[0][i].stimulation = random.random() * 2 - 1
    
    def produce_output_image(self) -> None:
        layer: typing.Sized = 1
        connection_index: typing.Sized = 0

        while layer < len(self.layers):
            for neuron in range(len(self.layers[layer])):
                neuron_stimulation: float = self.layers[layer - 1][neuron].stimulation

                for _ in range(self.IMAGE_SIZE):
                    neuron_stimulation += self.connections[connection_index] / 100
                    connection_index += 1
                
                neuron_stimulation += self.layers[layer][neuron].bias / 10
                self.layers[layer][neuron].stimulation = neuron_stimulation

            layer += 1
    
    def get_output_image(self) -> list[bool]:
        output_image: list[bool] = []

        for neuron in self.layers[len(self.layers) - 1]:
            output_image.append(neuron.stimulation > 0)
        
        return output_image
    
    def apply_feedback(self, feedback: float) -> None:
        feedback_adapted = feedback / 10 - 0.5
        print(feedback_adapted)

        for layer in self.layers:
            for neuron in layer:
                if neuron.bias < 0:
                    neuron.bias += -feedback_adapted
                elif neuron.bias > 0:
                    neuron.bias += feedback_adapted
        
        for connection in self.connections:
            if connection < 0:
                connection += -feedback_adapted
            elif connection > 0:
                connection += feedback_adapted
    
    def learn_image(self, image: list[bool]) -> None:
        for i in range(self.IMAGE_SIZE):
            self.layers[self.NETWORK_SIZE - 1][i].stimulation = float(image[i]) - 0.5

        layer: typing.Sized = self.NETWORK_SIZE - 2
        connection_index: typing.Sized = len(self.connections) - 1

        while layer > 0:
            for neuron in range(self.IMAGE_SIZE):
                neuron_stimulation: float = self.layers[layer + 1][neuron].stimulation

                for _ in reversed(range(self.IMAGE_SIZE)):
                    neuron_stimulation += self.connections[connection_index]
                    connection_index -= 1
                
                neuron_stimulation += self.layers[layer][neuron].bias
                self.layers[layer][neuron].stimulation = neuron_stimulation

            layer -= 1

class AI:
    def __init__(self, IMAGE_WIDTH: typing.Sized, IMAGE_HEIGHT: typing.Sized, DATA_FILE_NAME: str):
        self.neural_network = NeuralNetwork(IMAGE_WIDTH, IMAGE_HEIGHT, 18, DATA_FILE_NAME)

    def draw_image(self) -> list[bool]:
        self.neural_network.populate_input_neurons()
        self.neural_network.produce_output_image()
        return self.neural_network.get_output_image()
    
    def get_training_data(self) -> str:
        training_data: tuple[list[float], list[float]] = ([], [])

        for layer in self.neural_network.layers:
            for neuron in layer:
                training_data[0].append(neuron.bias)
        
        for connection in self.neural_network.connections:
            training_data[1].append(connection)

        return json.dumps(training_data, indent = 4)
