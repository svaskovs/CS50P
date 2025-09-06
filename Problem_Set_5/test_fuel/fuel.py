import sys

def main():
    fraction = (input("Fraction: "))
    print (gauge(convert(fraction)))


def convert(fraction):
    x,y = fraction.split("/")
    if int(x) > int(y):
        raise ValueError
    if int(y) == 0:
        raise ZeroDivisionError
    return round(100*int(x)/int(y))
          

def gauge(percentage):
    if 1 < percentage < 99:
        return str(percentage)+"%"
    elif percentage >= 99:
        return "F"
    elif 0 <= percentage <= 1:
        return "E"


if __name__ == "__main__":
    main()