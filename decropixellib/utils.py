from decropixellib import AI

def format_AI_image(image: list[bool], author: AI.AI) -> str:
    formatted_image: str = ""

    for _ in range(author.neural_network.IMAGE_WIDTH + 2):
        formatted_image += "-"

    formatted_image += "\n"

    for y in range(author.neural_network.IMAGE_HEIGHT):
        for x in range(author.neural_network.IMAGE_WIDTH):
            if x == 0:
                formatted_image += "|"

            match image[y * author.neural_network.IMAGE_WIDTH + x]:
                case True:
                    formatted_image += "#"
                case False:
                    formatted_image += " "
        
        formatted_image += "|\n"
    
    for _ in range(author.neural_network.IMAGE_WIDTH + 2):
        formatted_image += "-"

    return formatted_image

def train_AI(trainee: AI.AI) -> None:
    print("Evaluate the AI's creations to train it.")

    draw_another = True

    while draw_another:
        print(format_AI_image(trainee.draw_image(), trainee))

        cool = input("Was this cool? [y]es/[n]o: ")

        if not input("Do you wish to continue training the AI? [y]es/[n]o: ") == "y":
            draw_another = False
    
    if input("Do you wish to save the training data? [y]es/[n]o: ") == "y":
        with open(trainee.neural_network.DATA_FILE_NAME, "w") as data_file:
            data_file.write(trainee.get_training_data())

def reset_AI_data(target: AI.AI) -> None:
    print("This command will reset all the AI training data!")

    if not input("Are you sure you wish to continue? [y]es/[n]o: ") == "y":
        return

    print("Resetting all the data...")

    try:
        with open(target.neural_network.DATA_FILE_NAME, "w"):
            pass

    except:
        exit("Unable to open the data file to reset it!")

    print("The data was reset!")

def print_license_information() -> None:
    try:
        with open("LICENSE", "r") as license_file:
            print(license_file.read())

    except:
        exit("Unable to read the license file!")
