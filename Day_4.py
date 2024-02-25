
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

images = [rock, paper, scissors]


print("\nWhat do you choose?\n")
i = int(input("Press:\nRock -- 1\nPaper -- 2\nScissors -- 3 \n\n" )) -1

import random as r

rn = r.randint(0,2)

if i == 0 and rn == 2:
    print("Your choice\n", images[i])
    print("Computer choice\n", images[rn])
    print("you win")
elif rn == 0 and i == 2:
    print("Your choice\n", images[i])
    print("Computer choice\n", images[rn])
    print("you loose" )
elif i > rn:
    print("Your choice\n", images[i])
    print("Computer choice\n", images[rn])
    print("you win" )
elif i < rn:
    print("Your choice\n", images[i])
    print("Computer choice\n", images[rn])
    print("you loose" )
elif i == rn:
    print("Your choice\n", images[i])
    print("Computer choice\n", images[rn])
    print("it's a draw")
else:
    print("Invalid choice!")


