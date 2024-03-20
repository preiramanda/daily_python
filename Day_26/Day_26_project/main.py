#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

#Transforming the columns letter and code into rows (in the for loop) to later transform them in key,value to the dict.
data_dict = {r.letter: r.code for i,r in data.iterrows()}

name =  input("What is the name?\n").upper()

nato_list = [data_dict.get(i) for i in name if i in data_dict.keys()]

print(name)
print(nato_list)

 