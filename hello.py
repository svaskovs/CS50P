"""
# name = input("What's your name? ")

# Remowe leading and trailing whitespace from str
# name = name.strip()

# Capitalize str
# name = name.capitalize()

# Capitalize every word in str
# name = name.title()

# You can also chain all these methods:
name = input("What's your name? ").strip().title()

print ("Hello,", name)

# This is just another way to use the print function using the "format string:
print (f"Hello, {name}")

# Example of using the escape characters:
print ("Hello, \"friend\"")
"""
def hello(to="World"):
    print ("Hello", to)

name = input("What's your name? ")
hello (name)
