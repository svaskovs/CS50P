def main():
    fruit = input("Item: ").lower()
    if calories(fruit) != None:
        print ("Calories: ", calories(fruit))
    
def calories(f):
    nutr = {
        "apple":130,
        "banana":110,
        "grapes":90,
        "lemon":15
        }
    if f in nutr: return nutr[f]

main()