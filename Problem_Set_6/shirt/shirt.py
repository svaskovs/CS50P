import sys
import os
from PIL import Image, ImageOps


def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    valid_ext = [".jpg", ".jpeg", ".png"]
    if os.path.splitext(sys.argv[1])[1].lower() not in valid_ext or os.path.splitext(sys.argv[2])[1] not in valid_ext  :
        sys.exit("Invalid input")
    if os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
        sys.exit("Input and output have different extensions")   

    try:
        with Image.open(sys.argv[1]) as inputIMG:
            with Image.open("shirt.png") as shirt:
                outputIMG = ImageOps.fit(inputIMG, shirt.size)
                outputIMG.paste(shirt, shirt)
                outputIMG.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("File does not exist")



if __name__ == "__main__":
    main()