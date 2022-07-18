if not __name__ == "__main__":
    exit("Don't run Decropixel as a library!")

import sys

argv_length = len(sys.argv)

if argv_length == 1:
    print("Use the -h option for help!")
    exit()
elif argv_length > 2:
    print("Too many options!")
    exit()

del argv_length

match sys.argv[1]:
    case "-h":
        print("Help")
    case "-t":
        print("Test")
    case default:
        print("Unknown option! Use -h for help!")
