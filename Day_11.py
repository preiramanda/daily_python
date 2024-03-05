#Blackjack game

import random  as r

def hand():
    hand = []
    for i in range(2):
        hand.append(r.choice(cards))
    return hand

def score(hand):
    score = sum(hand)

    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score


def displayh(hand,score):
    print("Cards:", hand)
    print("Score:", score)


cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

user = hand()
computer =  hand()

computer_score = score(computer)
user_score = score(user)

displayh(computer, computer_score)
displayh(user, user_score)

def blackjack():
    while True:
        user = hand()
        computer = hand()

        computer_score = score(computer)
        user_score = score(user)

        print("Computer's Hand:")
        displayh(computer, computer_score)
        print("\nYour Hand:")
        displayh(user, user_score)

        # Verificar se o usuário ou o computador já têm Blackjack
        if user_score == 21:
            print("You have Blackjack! You win!")
        elif computer_score == 21:
            print("Computer has Blackjack! You lose!")
        else:
            while True:
                decision = input("Do you want to hit or pass? (h/p): ").lower()
                if decision == 'h':
                    user.append(r.choice(cards))
                    user_score = score(user)
                    print("Your new hand:")
                    displayh(user, user_score)
                    if user_score > 21:
                        print("Busted! You lose!")
                        break
                elif decision == 'p':
                    break

            if user_score <= 21:
                while computer_score < 17:
                    computer.append(r.choice(cards))
                    computer_score = score(computer)

                print("\nComputer's final hand:")
                displayh(computer, computer_score)

                if computer_score > 21 or (user_score <= 21 and user_score > computer_score):
                    print("You win!")
                elif user_score == computer_score:
                    print("It's a tie!")
                else:
                    print("You lose!")

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

blackjack()

