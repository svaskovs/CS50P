import random

while True:
    try:
        stop = int(input ("Level: "))
        if stop <= 0:
            raise ValueError
        break
    except ValueError:
        pass
while True:
    try:
        guess = int(input ("Guess: "))
        if guess <0:
            raise ValueError
        break
    except ValueError:
        pass

goal = random.randrange(1,stop+1)
if guess < goal:
    print ("Too small!")
elif guess > goal: 
    print ("Too large!")
else:
    print ("Just right!")