if not __name__ == "__main__":
    exit("Don't run Decropixel as a library!")

import sys

ARGV_LENGTH = len(sys.argv)

if ARGV_LENGTH == 1:
    exit("Use the \'help\' option for help!")
elif ARGV_LENGTH > 2:
    exit("Too many options!")

del ARGV_LENGTH

DATA_FILE_NAME = "data.txt"
LICENSE_FILE_NAME = "LICENSE"

def reset_AI_data() -> None:
    print("This command will reset all the AI training data!")
    confirmation = input("Are you sure you wish to continue? [y]es/[n]o: ")

    if not confirmation == "y":
        return

    print("Resetting all the data...")

    try:
        with open(DATA_FILE_NAME, "w") as data_file:
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
        print("Train AI")
    
    case "reset":
        reset_AI_data()
    
    case "license":
        print_license_information()

    case default:
        print("Unknown option! Use \'help\' for help!")

exit()
