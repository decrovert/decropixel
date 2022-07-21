from decropixellib import AI
from PIL import Image

def format_AI_image(image: list[bool], author: AI.AI) -> str:
    formatted_image: str = ""

    for _ in range(author.neural_network.IMAGE_WIDTH + 2):
        formatted_image += "- "

    formatted_image += "\n"

    for y in range(author.neural_network.IMAGE_HEIGHT):
        for x in range(author.neural_network.IMAGE_WIDTH):
            if x == 0:
                formatted_image += "| "

            match image[y * author.neural_network.IMAGE_WIDTH + x]:
                case True:
                    formatted_image += "# "
                case False:
                    formatted_image += "  "
        
        formatted_image += "|\n"
    
    for _ in range(author.neural_network.IMAGE_WIDTH + 2):
        formatted_image += "- "

    return formatted_image

def save_AI_data(artificial_intelligence: AI.AI) -> None:
    with open(artificial_intelligence.neural_network.DATA_FILE_NAME, "w") as data_file:
        data_file.write(artificial_intelligence.get_training_data())

def train_AI(trainee: AI.AI) -> None:
    print("Evaluate the AI's creations to train it.")

    draw_another = True

    while draw_another:
        print(format_AI_image(trainee.draw_image(), trainee))

        coolness = input("How cool was this? 0..10: ")
        coolness_float: float = 0.0

        try:
            coolness_float = float(coolness)
            
            if coolness_float < 0.0:
                coolness_float = 0.0
            elif coolness_float > 10.0:
                coolness_float = 10.0

            trainee.neural_network.apply_feedback(coolness_float)
        except:
            print("Error parsing a decimal number. Discarding evaluation...")
        
        del coolness, coolness_float

        if not input("Do you wish to continue training the AI? [y]es/[n]o: ") == "y":
            draw_another = False
    
    if input("Do you wish to save the training data? [y]es/[n]o: ") == "y":
        save_AI_data(trainee)

def teach_AI(student: AI.AI) -> None:
    print("Please choose an image to teach the AI.")
    print("The image must contain only fully black and fully white pixels and use the correct size!")
    image_file_path: str = input("Write the path to the image file: ")
    image_list: list[bool] = []

    try:
        image_list_raw = list(Image.open(image_file_path).convert("RGBA").tobytes())

        for i in range(int(len(image_list_raw) / 4)):
            rgb = (image_list_raw[i * 4], image_list_raw[i * 4 + 1], image_list_raw[i * 4 + 2])
            
            if not (rgb == (255, 255, 255) or rgb == (0, 0, 0)):
                print("The image contains pixels that do not satisfy the required criteria!")
                raise
            else:
                image_list.append(rgb == (0, 0, 0))
    except:
        print("Error while opening the specified image file.")
        return
    
    del image_file_path

    student.neural_network.learn_image(image_list)

    del image_list

    if input("Do you wish to save the new neural network data? [y]es/[n]o: ") == "y":
        save_AI_data(student)

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
