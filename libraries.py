import random
import sys

coin = random.choice(["heads", "tails"])
number = random.randint(1, 10)
a = random.randrange(1,10)
cards = ["jack", "queen", "king"]
random.shuffle(cards)
print (coin)
print (number)
print (a)
for card in cards:
    print (card)

print (f"Hello, my name is {sys.argv}")