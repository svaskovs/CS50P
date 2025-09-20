import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"^(\d?\d):?([0-5]?\d?) ([A|P]M) to (\d?\d):?([0-5]?\d?) ([A|P]M)", s, re.IGNORECASE):
        hh_a, mm_a, ap_a, hh_b, mm_b, ap_b = match.groups()
    else: raise ValueError

    time_a_validated = validate(hh_a, mm_a, ap_a.lower())
    time_b_validated = validate(hh_b, mm_b, ap_b.lower())
    return f"{time_a_validated} to {time_b_validated}" 


def validate(h, m, ap):
    if h and m:
        h, m = int(h), int(m)
    else: h, m = int(h), 0
    
    if (h not in range(1,13)) or (m not in range(0,60)):
        raise ValueError

    if ap == "am":
        if h == 12:
            h = 0
    else:
        if h != 12:
            h +=12   
    time_validated = f"{h:02}:{m:02}"
    return time_validated
    

if __name__ == "__main__":
    main()