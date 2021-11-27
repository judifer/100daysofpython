print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 

def welcome():
    print("Do you want to go 'left' or 'right'?")
    a = input()
    if a == "left":
        return first_fork()
    elif a == "right":
        return "Fall into a hole.\nGame over."
    else:
        print("That was not a valid choice.")
        return welcome()

def first_fork():
    print("You've reached a river.\nDo you want to 'wait' for a boat or 'swim'?")
    a = input()
    if a == "swim":
        return "Attacked by trout.\nGame over."
    elif a == "wait":
        return second_fork()
    else:
        print("That was not a valid choice.")
        return first_fork()

def second_fork():
    print("You cross the river in the boat and reach a house with three doors.\nWhich door do you want to open? 'Red', 'Blue' or 'Yellow'?")
    a = input()
    if a == "Red":
        return "You've been burned by fire.\nGame over."
    elif a == "Blue":
        return "You've been eaten by beasts.\nGame over."
    elif a == "Yellow":
        return "You win!\nGood job!"
    else:
        print("That was not a valid choice.")
        return second_fork()

print(welcome())