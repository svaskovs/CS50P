while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x must be an integer, you dumb ass!!!")
    else:
        break

print (f"x is {x}")