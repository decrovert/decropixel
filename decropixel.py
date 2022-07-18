if not __name__ == "__main__":
    exit("Don't run Decropixel as a library!")

import sys
import random; random.seed()
import typing

ARGV_LENGTH: typing.Sized = len(sys.argv)

if ARGV_LENGTH == 1:
    exit("Use the \'help\' option for help!")
elif ARGV_LENGTH > 2:
    exit("Too many options!")

del ARGV_LENGTH

DATA_FILE_NAME: str = "data.txt"
LICENSE_FILE_NAME: str = "LICENSE"

IMAGE_WIDTH: int = 8
IMAGE_HEIGHT: int = 8
IMAGE_SIZE: int = IMAGE_WIDTH * IMAGE_HEIGHT

NETWORK_SIZE: typing.Sized = 5

class Neuron:
    def __init__(self, stimulation: float, bias: float):
        self.stimulation = stimulation
        self.bias = bias

class NeuralNetwork:
    def __init__(self):
        self.layers = []
        self.connections = []

        for i in range(NETWORK_SIZE):
            self.layers.append([])
            
            for _ in range(IMAGE_SIZE):
                self.layers[i].append(Neuron(0.0, random.random() * 2 - 1))

        for i in range((len(self.layers) - 1) * (IMAGE_SIZE ** 2)):
            self.connections.append(random.random() * 2 - 1)
    
    def populate_input_neurons(self) -> None:
        for i in range(len(self.layers[0])):
            self.layers[0][i].stimulation = random.random() * 2 - 1
    
    def produce_output_image(self) -> None:
        layer: typing.Sized = 1
        connection_index: typing.Sized = 0

        while layer < len(self.layers):
            for neuron in range(len(self.layers[layer])):
                neuron_stimulation: float = self.layers[layer - 1][neuron].stimulation

                for _ in range(IMAGE_SIZE):
                    neuron_stimulation += self.connections[connection_index]
                    connection_index += 1
                
                neuron_stimulation += self.layers[layer][neuron].bias
                self.layers[layer][neuron].stimulation = neuron_stimulation

            layer += 1
    
    def get_output_image(self) -> typing.List[bool]:
        output_image: typing.List[bool] = []

        for neuron in self.layers[len(self.layers) - 1]:
            output_image.append(neuron.stimulation > 0)
        
        return output_image

    def draw_image(self) -> typing.List[bool]:
        self.populate_input_neurons()
        self.produce_output_image()
        return self.get_output_image()

neural_network = NeuralNetwork()

def format_AI_image(image: typing.List[bool]) -> str:
    formatted_image: str = ""

    for _ in range(IMAGE_WIDTH + 2):
        formatted_image += "-"

    formatted_image += "\n"

    for y in range(IMAGE_HEIGHT):
        for x in range(IMAGE_WIDTH):
            if x == 0:
                formatted_image += "|"

            match image[y * IMAGE_WIDTH + x]:
                case True:
                    formatted_image += "#"
                case False:
                    formatted_image += " "
        
        formatted_image += "|\n"
    
    for _ in range(IMAGE_WIDTH + 2):
        formatted_image += "-"

    return formatted_image

def train_AI() -> None:
    print("Evaluate the AI's creations to train it.")

    draw_another = True

    while draw_another:
        print(format_AI_image(neural_network.draw_image()))

        cool = input("Was this cool? [y]es/[n]o: ")

        if not input("Do you wish to continue training the AI? [y]es/[n]o: ") == "y":
            draw_another = False

def reset_AI_data() -> None:
    print("This command will reset all the AI training data!")

    if not input("Are you sure you wish to continue? [y]es/[n]o: ") == "y":
        return

    print("Resetting all the data...")

    try:
        with open(DATA_FILE_NAME, "w"):
            pass
    except:
        exit("Unable to open the data file to reset it!")

    print("The data was reset!")

def print_license_information() -> None:
    try:
        with open(LICENSE_FILE_NAME, "r") as license_file:
            print(license_file.read())
    except:
        exit("Unable to read the license file!")

match sys.argv[1]:
    case "help":
        print("help:")
        print("\tShow commands.")

        print("train:")
        print("\tTrain AI.")

        print("reset:")
        print("\tReset all knowledge data.")

        print("license:")
        print("\tShow license information (if available).")

    case "train":
        train_AI()
    
    case "reset":
        reset_AI_data()
    
    case "license":
        print_license_information()

    case default:
        print("Unknown option! Use \'help\' for help!")

exit()
