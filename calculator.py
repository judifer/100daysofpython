from replit import clear

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
operators = "Available operators:\n+\n-\n*\n/"

def new_num():
    print(logo)
    print()
    num_1 = float(input("Type in your first number:\n"))
    return ex_num(num_1)
    
def ex_num(a):
    print(operators)
    op = input("Pick an operator:\n")
    b = float(input("Type in your second number:\n"))
    print(f"{a} {op} {b} =", calc(a, op, b))
    c = input("Type 'yes' if you want to continue with this number or 'no' if you want to choose a new number.\n")
    if c == "yes":
        return ex_num(a)
    elif c == "no":
        clear()
        return new_num()
    else:
        exit()
    
def calc(x, o, y):
    if o == "+":
        result = x + y
    elif o == "-":
        result = x - y
    elif o == "*":
        result = x * y
    elif o == "/":
        result = x / y
    else:
        print("Invalid operator. Restarting.")
        return new_num()
    return result
    
new_num()