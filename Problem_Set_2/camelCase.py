def main():
    camel_case = input("Name? ")
    snake_case(camel_case)
    print()

def snake_case(name):
    for l in name:        
        if l.isupper():
            print ("_" + l.lower(), end='')
        else: print (l, end='')


main()