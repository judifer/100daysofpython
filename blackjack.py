import random
from time import sleep

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print("Welcome to...\n", logo)

def draw():
    a = random.choice(cards)
    return a

def player():
    score = list()
    while True:
        b = draw()
        if b == 11:
            if (sum(score) + b) > 21:
                b = 1
        score.append(b)
        print(f"The value of your card is {b}.")
        if len(score) > 1:
            print(f"{' + '.join(str(x) for x in score)} = {sum(score)}")
        if sum(score) > 21:
            n = input("Oh no, you lost. Type 'yes' to start a new game.\n").lower()
            if n == "yes":
                return player()
            else:
                exit()
        elif sum(score) == 21:
            print("Yay! You won!")
            x = input("Type 'yes' if you want to play another game.\n").lower()
            if x == "yes":
                return player()
        else:
            c = input("Type 'yes' if you want to draw another card.\n").lower()
            if c != "yes":
                break
            else:
                continue
    sum_score = sum(score)
    print(f"The score the computer has to beat is {sum(score)}")
    return computer(sum_score)

def computer(p):
    score = list()
    while sum(score) <= 19:
        print("Computer is drawing a card...")
        sleep(3)
        a = draw()
        if a == 11:
            if (sum(score) + a) > 21:
                a = 1
        score.append(a)
        if len(score) < 2:
            print(f"Computer's current score: {a}")
        else:
            print(f"Computer's current score: {' + '.join(str(x) for x in score)} = {sum(score)}")
    if sum(score) > 21:
        print("You have won!")
    elif sum(score) > p:
        print("The computer has won!")
    elif sum(score) == p:
        print("It's a tie!")
    x = input("Type 'yes' if you want to play another game.\n").lower()
    if x == "yes":
        return player()
    else:
        exit()


player()