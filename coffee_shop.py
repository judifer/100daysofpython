from time import sleep

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickle": 0.05,
    "penny": 0.01,
}

def main_menu():
    paid = 0
    print("You're in the main menu. Please choose one of the following options.")
    print("Espresso\nLatte\nCappucino\nReport\nOff")
    a = input().lower()
    if a != "espresso" and a != "latte" and a != "cappucino" and a != "report" and a != "off":
        print("I'm sorry, I don't understand you. Please choose a valid option.")
        return main_menu()
    if a == "off":
        exit()
    elif a == "report":
        print(f"\nWater: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\n")
        input("Press any button to return to the main menu.\n")
        return main_menu()
    else:
        return res_check(a, paid)

def res_check(a, p):
    if a == "espresso":
        if menu[a]["ingredients"]["water"] < resources["water"] and menu[a]["ingredients"]["coffee"] < resources["coffee"]:
            print("\nProcessing order.\n")
            return payment(a, p)
        else:
            print("\nOrder currently not available. Please choose a different option.\n")
            return main_menu()
    else:
        if menu[a]["ingredients"]["water"] < resources["water"] and menu[a]["ingredients"]["milk"] < resources["milk"] and menu[a]["ingredients"]["coffee"] < resources["coffee"]:
            print("\nProcessing order.\n")
            return payment(a, p)
        else:
            print("\nOrder currently not available. Please choose a different option.\n")
            return main_menu()

def payment(a, p):
    print(f"The cost for your order is $ {'{:.2f}'.format(menu[a]['cost'])}")
    x = input("We accept the following coins:\nQuarter\nDime\nNickle\nPenny\nPlease insert one coin at a time. Type 'finish' when you're done.\n").lower()
    if x == "finish":
        print(f"You have paid $ {'{:.2f}'.format(p)}")
        if p < menu[a]["cost"]:
            print("Payment not sufficient. Coins will be returned to you.")
            return main_menu()
        elif p > menu[a]["cost"]:
            change = p - menu[a]["cost"]
            print(f"Your change of $ {'{:.2f}'.format(change)} will be returned to you now.")
            return brewing(a)
        else:
            return brewing(a)
    else:
        p += coins[x]
        print(f"Current amount: $ {'{:.2f}'.format(p)}")
        return payment(a, p)

def brewing(a):
    print("\nPlease wait while your drink is brewing...\n")
    sleep(3)
    resources["coffee"] -= menu[a]["ingredients"]["coffee"]
    resources["water"] -= menu[a]["ingredients"]["water"]
    if a != "espresso":
        resources["milk"] -= menu[a]["ingredients"]["milk"]
    if len(resources) == 3:
        resources["cost"] = menu[a]["cost"]
    else:
        resources["cost"] += menu[a]["cost"]
    print(f"Here's your {a}, enjoy!")
    print("Returning to main menu...\n")
    sleep(1)
    return main_menu()

main_menu()