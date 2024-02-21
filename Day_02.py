print("Welcome to the Tip Calculator!") 

# First question: 
total = float(input("What is the total of your bill?"))

#Second question:
percentage = int(input("What percentage of tip you'd like to give? (10, 12 or 15)"))

# Third question:
split  = float(input("How many people to split the bill?"))

#Calculations:
ntotal = ((percentage * total)/100) + total
ntotal /= split

#Printing result:
print(f"Each person will pay {round(ntotal,2)}")