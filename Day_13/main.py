import data as d
import random as r

def person():
    p = r.choice(d.data)
    return p

def followers(person):
    return person["follower_count"]

def comp(guess, followers_a, followers_b):
    if followers_a > followers_b:
        return guess == "A"  
    else:
        return guess == "B"  

def data(person):
    name = person["name"]
    description = person["description"]
    country = person["country"]
    return f"{name}, a {description}, from {country}"

def game():
    score = 0

    while True:
        a = person()
        b = person()
        
        while a == b:
            b = person()
        
        print(data(a))
        print(data(b))

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        af = followers(a)
        bf = followers(b)

        if comp(guess, af, bf):
            print("\nCorrect!\n")
            print(f'{a["name"]} has {af} followers\n{b["name"]} has {bf} followers')  
            score += 1
        else:
            print(f'\nWrong!\n{a["name"]} has {af} followers\n{b["name"]} has {bf} followers')   
            print(f"Your score was: {score}")
            break
        print("\nYour score:", score)

    if comp(guess, af, bf):
        game()

game()
