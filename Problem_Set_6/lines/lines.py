import sys

def main():
    try:
        fileName = sys.argv[1]
    except IndexError:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if fileName[-3:] != ".py":
        sys.exit("Not a Python file")

    try:
        with open(fileName, "r") as file:
            codeLines = 0
            for line in file:
                if not line.lstrip().startswith("#") and line.lstrip():
                    codeLines +=1
    except FileNotFoundError:
        sys.exit("File does not exist")

    print (codeLines)

if __name__ == "__main__":
    main()