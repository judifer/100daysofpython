import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 

graphics = [rock, paper, scissors]

def game():
    chosen = input("Type '0' for rock, '1' for paper, '2' for scissors or 'exit' to stop playing.\n")
    if chosen == "exit":
        return "Thank you for playing."
    else:
        opponent = random.randint(0, 2)
        chosen = int(chosen)
        if chosen >= 3 or chosen < 0:
            print("Oops! Something went wrong!")
            return game()
        else:
            print("You chose\n", graphics[chosen])
            print("Opponent chose\n", graphics[opponent])
            if chosen == 0 and opponent == 2:
                print("You win!")
                return game()
            elif chosen == 2 and opponent == 0:
                print("You lose!")
                return game()
            elif chosen < opponent:
                print("You lose!")
                return game()
            elif chosen > opponent:
                print("You win!")
                return game()
            elif chosen == opponent:
                print("It's a tie!")
                return game()
            else:
                print("Oops! Something went wrong.")
                return game()

print("Welcome to rock, paper, scissors!")
print(game())
