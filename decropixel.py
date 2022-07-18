if not __name__ == "__main__":
    exit("Don't run Decropixel as a library!")

import sys

argv_length = len(sys.argv)

if argv_length == 1:
    print("Use the \'help\' option for help!")
    exit()
elif argv_length > 2:
    print("Too many options!")
    exit()

del argv_length

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
        print("Reset AI")
    
    case "license":
        print("License information")
    
    case default:
        print("Unknown option! Use \'help\' for help!")
