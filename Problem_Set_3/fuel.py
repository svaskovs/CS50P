def main():
    print (tank_status("Fraction: "))

def tank_status(prompt):  
     while True:
        try:
            fraction = input(prompt).split("/")
            result = round(100*int(fraction[0])/int(fraction[1]))
            if 0 <= result <= 100:
                return str(result)+"%"
            elif result < 0 or result > 100:
                raise ValueError
            elif result >= 99:
                return "F"
            elif 0 < result <= 1:
                return "E"

        except (ValueError, ZeroDivisionError, IndexError):
            pass

main()