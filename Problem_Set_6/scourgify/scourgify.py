import sys
import csv

def main():

    try:
        fileName_in = sys.argv[1]
        fileName_out = sys.argv[2]
    except IndexError:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    try:
        with open(fileName_in, "r") as input, open(fileName_out, "w") as output:
            reader = csv.DictReader(input)
            writer = csv.DictWriter(output, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                first, last = row['name'].split(",")
                writer.writerow({"first": first.strip(), "last": last.strip(), "house": row['house']})

    except FileNotFoundError:
        sys.exit(f"Could not read {fileName_in}")

if __name__ == "__main__":
    main()