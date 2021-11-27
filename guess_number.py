import random

logo = """
.___  .__                         ___.                             
|   | |  |__ _____ ___  __ ____   \_ |__   ____   ____   ____      
|   | |  |  \\__  \\  \/ // __ \   | __ \_/ __ \_/ __ \ /    \     
|   | |   Y  \/ __ \\   /\  ___/   | \_\ \  ___/\  ___/|   |  \    
|___| |___|  (____  /\_/  \___  >  |___  /\___  >\___  >___|  /    
           \/     \/          \/       \/     \/     \/     \/     
  _____                              .___   __                     
_/ ____\___________   ____  ____   __| _/ _/  |_  ____             
\   __\/  _ \_  __ \_/ ___\/ __ \ / __ |  \   __\/  _ \            
 |  | (  <_> )  | \/\  \__\  ___// /_/ |   |  | (  <_> )           
 |__|  \____/|__|    \___  >___  >____ |   |__|  \____/            
                         \/    \/     \/                           
.__              .__            .___         __  .__    .__        
|__| ____   ____ |  |  __ __  __| _/____   _/  |_|  |__ |__| ______
|  |/    \_/ ___\|  | |  |  \/ __ |/ __ \  \   __\  |  \|  |/  ___/
|  |   |  \  \___|  |_|  |  / /_/ \  ___/   |  | |   Y  \  |\___ \ 
|__|___|  /\___  >____/____/\____ |\___  >  |__| |___|  /__/____  >
        \/     \/                \/    \/             \/        \/ 
                     .__.__  .__                                   
_____    ______ ____ |__|__| |  |   ____   ____   ____             
\__  \  /  ___// ___\|  |  | |  |  /  _ \ / ___\ /  _ \            
 / __ \_\___ \\  \___|  |  | |  |_(  <_> ) /_/  >  <_> )           
(____  /____  >\___  >__|__| |____/\____/\___  / \____/            
     \/     \/     \/                   /_____/                  
"""

print(logo)
print("Welcome to 'Guess the Number'!")

def mode():
    a = input("Please choose your mode by typing 'easy' or 'hard'.\n")
    if a == 'easy':
        b = 10
    elif a == 'hard':
        b = 5
    else:
        print("I'm sorry, I didn't understand what you were saying. Please try again.")
        return mode()
    return calc_number(b)

def calc_number(m):
    a = random.randint(1, 99)
    return user_number(a, m)

def user_number(x, m):
    while m > 0:
        a = int(input("Please type in a number between 0 and 100.\n"))
        if a == x:
            print("Yay! You've found the number!")
            b = input("Type 'yes' if you want to play again:\n").lower()
            if b == "yes":
                return mode()
            else:
                exit()
        elif a > x:
            print("Your number is too high.")
        else:
            print("Your number is too low.")
        m -= 1
        print(f"You have {m} guesses left.")
    print("Oh no. You didn't guess the number.")
    b = input("Type 'yes' if you want to play again:\n").lower()
    if b == "yes":
        return mode()
    else:
        exit()

mode()