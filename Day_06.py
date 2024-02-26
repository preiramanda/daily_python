import random as r

c = r.randint(0, 101)

while True:
    u = int(input("Guess the number!\nTry to guess a number from 1 to 100: "))

    if u < c:
        print("The number is a little higher than that!\n")
    elif u > c:
        print("The number is a little lower than that!\n")
    else:
        print("Congratulations! You guessed the number!")
        break
