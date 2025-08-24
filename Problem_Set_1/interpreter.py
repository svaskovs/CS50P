def main():
    expression_raw = input("Expression: ").lower()
    print (calculate(expression_raw))
           
def calculate(ex):
    x, y, z = ex.split(" ")
    x, z = float(x), float(z)

    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z if z != 0 else "Division by zero error"
    
main()