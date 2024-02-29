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

import random as r

print("Let's play Hangman!\n")
print("The word can be a color, fruit or animal.\n")

word_list = ["apple", "banana", "orange", "grape", "strawberry", 
             "watermelon", "red", "blue", "green", "yellow", "orange", 
             "purple", "pink", "brown", "black", "white","dog", "cat", 
             "horse", "elephant", "lion", "tiger", "bear", "penguin", 
             "koala", "dolphin", "monkey", "bee", "shark", "giraffe"]

lives = 6

word = r.choice(word_list)

blanks = ["_"] * len(word)

print(" ".join(blanks)) 

while "_" in blanks and lives != 0:
    l = input("\nGuess a letter:").lower()
    
    if l in word:
        for i in range(len(word)):
            if word[i] == l:
                blanks[i] = l
        print(" ".join(blanks))
        print("\n")
    else:
        print("\nIncorrect word, try again!\n")
        lives -= 1
        print(stages[lives])

if lives == 0:
    print("You lose!")
else:
    print("\nCongratulations, you win. The word was:", ''.join(blanks))
