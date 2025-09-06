import sys
from tabulate import tabulate
import csv

def main():
    try:
        fileName = sys.argv[1]
    except IndexError:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if fileName[-4:] != ".csv":
        sys.exit("Not a CSV file")

    try:
        with open(fileName, "r") as file:
            reader = csv.DictReader(file)
            print (tabulate(reader, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()