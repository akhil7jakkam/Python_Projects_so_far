import random

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

word_list = ["aardvark", "baboon", "camel"]
lives = 6


display = []
chosen_word = []
for i in random.choice(word_list):
    chosen_word.append(i)

for _ in chosen_word:
    display += "_"

print(chosen_word)

game_on = True

while game_on:

    guess = input("Guess a letter : ").lower()

    index = 0

    for letter in chosen_word:
        if guess == letter:
            display[index] = letter
        index += 1

    word = ""
    for w in display:
        word += w + " "
    print(word)

    if guess not in display:
        lives -= 1

    print(f"lives : {lives}")
    print(stages[lives])

    if display == chosen_word:
        print("You won.")
        game_on = False
    elif lives < 1:
        print("You lose.")
        game_on = False
