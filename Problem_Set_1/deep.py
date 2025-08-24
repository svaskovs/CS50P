the_answer = input("What is the Answer to the Great Question of Life, the Universe and Everything: ")

match the_answer.lower():
    case "42" | "fourty two" | "fourty-two" :
        print ("Yes")
    case _:
        print ("No")