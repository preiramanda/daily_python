import random as r

country = input("Add a country name\n") 
visits = int(input("\nHow many times did you visit?\n")) 
list_of_cities = input("\nInsert the list of visited cities, separated by a comma (,)\n").split(",") 

travel_log = [
  { "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"] },
  { "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"] },]
 
def add_country(country, visits, cities):
    new_country = {
        "country": country,
        "visits": visits,
        "cities": cities
    }
    travel_log.append(new_country)

random_country = r.choice(travel_log) 
random_city = r.choice(random_country["cities"])

print(f"The next place you should visit again is {random_country['country']}.\nWhy dont you try to visit {random_city} again?\n")

