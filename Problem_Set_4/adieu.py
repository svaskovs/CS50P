import inflect

p = inflect.engine()

names = []
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        print (f"\nAdieu, Adieu, to {p.join(names)}")
        break