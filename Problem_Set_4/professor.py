import random

def main():
    n = get_level()
    score = 0
    for _ in range(0,10):
        x, y = generate_integer(n)[0], generate_integer(n)[1]
        error = 0
        while True:
            try: 
                ans = input(f"{x} + {y} = ")
                if int(ans) != x+y and error <3:
                    raise ValueError
                score += 1
                break
            except ValueError:
                print("EEE")
                error += 1
                if error == 3:
                    print (f"{x} + {y} = {x+y}")
                    break
                pass
    print ("Score: ", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                raise ValueError
            return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        x, y = random.randint(1, 9), random.randint(1, 9)
    elif level == 2:
        x, y = random.randint(10, 99), random.randint(10, 99)
    elif level == 3:
        x, y = random.randint(100, 999), random.randint(100, 999)
    return x, y

if __name__ == "__main__":
    main()