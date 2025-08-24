
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
order = []

while True:
    try:
        item = input("Item: ").title().strip()
        item_price = menu.get(item)
        if item_price == None:
            raise ValueError()
        order.append(item_price)
        print (f"Total: ${sum(order)}")
    except EOFError:
            print ()
            break
    except (ValueError, TypeError):
        pass