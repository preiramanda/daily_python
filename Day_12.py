logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

import random as r

def start(c):
    global attempts 
    while True:
        if c == 'easy':
            attempts = 10
            return attempts
        elif c == 'hard':
            attempts = 5
            return attempts
        else:
            play_again = input("You have to type 'easy' or 'hard'.\nType any other key to exit\n").lower()
            if play_again not in ['easy', 'hard']:
                print("Exiting, please start over")
                break
            else:
                c = play_again


def game(attempts):
    number = r.randint(0, 100)
    out_of_attempts = False
    
    while attempts != 0:
        guess = int(input(f"You have {attempts} attempts. Guess a number from 0 to 100:\n"))

        if guess == number:
            print(f"You guessed correctly, the number was {number}")
            return
        
        if guess < number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        
        attempts -= 1

    out_of_attempts = True

    if out_of_attempts:
        print(f"Sorry, you ran out of attempts. The correct number was {number}.")

        
print(logo)

c = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()

attempts = start(c)

if attempts is not None:
    game(attempts)
 


