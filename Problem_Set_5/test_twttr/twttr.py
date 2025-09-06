def main():
    input_txt = input("Input: ")
    print ("Output: ", shorten(input_txt))


def shorten(word):
    output = ""
    for s in word:
        if s.upper() not in ["A", "E", "I", "O", "U"]:
            output = output + s
    return output


if __name__ == "__main__":
    main()
