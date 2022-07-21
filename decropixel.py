if not __name__ == "__main__":
    exit("Don't run Decropixel as a library!")

import sys
import typing

ARGV_LENGTH: typing.Sized = len(sys.argv)

if ARGV_LENGTH == 1:
    exit("Use the \'help\' option for help!")
elif ARGV_LENGTH > 2:
    exit("Too many options!")

del ARGV_LENGTH

from decropixellib import AI, utils

artificial_intelligence = AI.AI(8, 8, "data.json")

match sys.argv[1]:
    case "help":
        print("help:")
        print("\tShow commands.")

        print("train:")
        print("\tTrain AI.")

        print("teach:")
        print("\tShow the AI an image to learn.")

        print("reset:")
        print("\tReset all knowledge data.")

        print("license:")
        print("\tShow license information (if available).")

    case "train":
        utils.train_AI(artificial_intelligence)
    
    case "teach":
        utils.teach_AI(artificial_intelligence)
    
    case "reset":
        utils.reset_AI_data(artificial_intelligence)
    
    case "license":
        utils.print_license_information()

    case default:
        print("Unknown option! Use \'help\' for help!")

exit()
