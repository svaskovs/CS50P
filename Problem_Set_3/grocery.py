grocery_list = {}
while True:
    try:
        item = input().lower().strip()
        if item != "":
            if item not in grocery_list:
                grocery_list.update({item : 1})
            else:
                grocery_list[item] +=1
    
    except EOFError:
        print()
        for item in sorted(grocery_list.keys()):
            print (grocery_list[item], item.upper())
        break