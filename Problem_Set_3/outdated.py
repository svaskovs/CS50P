months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        input_date = input("Date: ")
        if "/" in input_date:       
            mm, dd, yyyy = input_date.split('/')
            mm, dd = int(mm), int(dd)
        else:
            mm, dd, yyyy = input_date.split(' ')
            mm, dd = months.index(mm)+1, int(dd[:-1]) 
        if mm < 13 and dd < 32: 
            print(f"{yyyy}-{mm:02}-{dd:02}")
            break
    except ValueError:
        pass

