# Things used today: random.choice (randint for strings) and random.shuffle

import random as r

print("Welcome to the PyPassword generator!\n")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#my list:
password = []

nl = int((input("How many letters would you like in your password?\n")))
nn = int((input("How many numbers would you like in your password?\n")))
ns = int((input("How many symbols would you like in your password?\n")))

'''
For each imput, I'll transform the imput into a range. 
For the range, I'll chose random letters, numbers or signs
'''

for i in range(0,nl):
    password.append(r.choice(letters))

for i in range(0,nn):
    password.append(r.choice(numbers))

for i in range(0,ns):
    password.append(r.choice(symbols))

r.shuffle(password) 

npassword = ""

for i in password:
    npassword += i

print(f"\n Your new password is: {npassword}")
 
