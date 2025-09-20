from datetime import date
import sys
import inflect

def main():
    try:
        dob = date.fromisoformat(input("Date of Birth: "))
    except:
        return sys.exit ("Invalid date")
    diff = (date.today() - dob).days*24*60
    print(scribe(diff), "minutes")


def scribe(minutes):
    p = inflect.engine()
    return p.number_to_words(minutes, andword="").capitalize()


if __name__ == "__main__":
    main()