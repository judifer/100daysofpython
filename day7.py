import random

word_list = ["hund", "leni", "bauhaus", "couch", "fernseher", "papa", "mama", "tisch", "bohrmaschine", "apfel"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

a = random.randrange(0, len(word_list))
chosen_word = word_list[a]
display = list()
for i in chosen_word:
    display.append("_")
print(f"Your word has {len(display)} letters.")
lives = 6

def guessing(x, display, l):
    guess = input("Choose a letter!\n").lower()
    if guess in x:
        for ind, a in enumerate(x):
            if a == guess:
                display[ind] = guess
        if "_" in display:
            print(f"You've guessed the following letters correctly: {' '.join(display)}")
            return guessing(x, display, l)
        else:
            return f"Congratulations! Your word is {''.join(display)}"
    else:
        print("The word does not contain your letter. You've lost a life")
        print(stages[l])
        l -= 1
        if l < 0:
            return "Game over."
        else:
            return guessing(x, display, l)

print(guessing(chosen_word, display, lives))
input()
