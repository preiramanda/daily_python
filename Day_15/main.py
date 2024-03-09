import data 

def initial():
    while True:  
        choice = input("\nWhat would you like? (espresso/latte/cappuccino):\n")

        if choice in data.MENU:   
            ingredients = data.MENU[choice]['ingredients']
            coffee_price = data.MENU[choice]['cost']
            return choice, ingredients, coffee_price
        elif choice == "report":
            return choice, None, None
        elif choice == "off":
            print("Turning off")
            return choice, None, None
        else:
            print("Invalid choice! Please choose from the available options.")

def resources(ingredients):

    
    if len(ingredients) == 2:
        if ingredients['water'] <= data.resources['water'] and ingredients['coffee'] <= data.resources['coffee']:
            data.resources['water'] -= ingredients['water']
            data.resources['coffee'] -= ingredients['coffee']
            print("Available!")
            return True
        else:
            print("Not enought ingredients")
    else:
        if ingredients['water'] <= data.resources['water'] and ingredients['coffee'] <= data.resources['coffee'] and  ingredients['milk'] <= data.resources['milk']:
            data.resources['water'] -= ingredients['water']
            data.resources['milk'] -= ingredients['milk']
            data.resources['coffee'] -= ingredients['coffee']
            print("Available!")
            return True
        else:
            print("Not enought ingredients")

def coins(money=0):
    while True: 
        c = input("\nInsert the type of coin: 'Q' for quarter, 'D' for dime, or 'N' for nickles:\n").lower()
        coin = {'q': 0.25, 'd': 0.10, 'n': 0.05}   

        if c in coin:
            while True:
                ncoins = int(input("How many coins?\n"))
                if ncoins < 150:
                    money += coin[c] * ncoins 
                    return money
                else:
                    print("\nThe max amout of coins is 150\n")
        else: 
            print("You have to chose between 'Q' for quarter, 'D' foridme, or 'N' for nickles:\n")

def checkmoney(coffee_price):    
    money = coins() 
    while coffee_price > money:
        if money < coffee_price:
            missing = coffee_price - money
            print(f"Is missing: {missing} for your coffee")
            money += coins()  

    if money > coffee_price:
        change = money - coffee_price
        print("Enjoy your coffee ☕️ !")
        print(f"Your change: {change}")
        data.resources['money'] += coffee_price
        return coffee_price  
    else:
        print("Enjoy your coffee ☕️ !")
        data.resources['money'] += coffee_price
        return coffee_price

def report():
    water = data.resources['water']
    milk = data.resources['milk']
    coffee = data.resources['coffee']
    pay = data.resources['money']
    print(f"This machine has\nCoffe: {coffee}ml\nMilk: {milk}ml\nWater: {water}ml\nTotal cash in machine: {pay}")


choice, ingredients, coffee_price = initial()

if choice not in ["off","report"]:
    resources_ok = resources(ingredients)
    if resources_ok == True:
        checkmoney(coffee_price)
    
if choice == "report":
    report()



