the_answer = input("Greeting: ").lower()

if the_answer.startswith("hello"):
    print ("$0")
elif the_answer.startswith("h"):
    print ("$20")
else: print ("$100")