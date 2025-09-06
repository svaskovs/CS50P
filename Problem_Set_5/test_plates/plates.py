def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if length(s) and start_2l(s) and sur_by_l(s) and leadZero(s) and unallowed_char(s):
        return True
    else: return False


def length(s):
    if 2 <= len(s) <= 6:
        return True
    else: return False

def start_2l(s):
    if s[0].isdigit() or s[1].isdigit():
        return False
    else: return True

def sur_by_l(s):
    for i in range(len(s)-1):
        if s[i].isdigit() == True and s[i+1].isdigit() is False:
            return False
    return True


def leadZero(s):
    for i in range(len(s)-1,-1,-1):
        if s[i].isdigit() == True and s[i-1] == '0':
            return False
    return True        

            
def unallowed_char(s):
    if s.isalnum() != True:
        return False
    return True

if __name__ == "__main__":
    main()