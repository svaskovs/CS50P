def main():
    time_raw = input("What time is it? ")
    
    if 7 <= convert(time_raw) <= 8:
        print ("breakfast time")
    elif 12 <= convert(time_raw) <= 13:
        print ("lunch time")
    elif 18 <= convert(time_raw) <= 19:
        print ("dinner time")


def convert(time):
    h, m = time.split(":")
    time_flt = float(h)+(float(m)/60)
    return time_flt


if __name__ == "__main__":
    main()