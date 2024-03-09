# from  turtle  import Turtle, Screen

# timmy = Turtle()

# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# myscreen = Screen()
# print(myscreen.canvheight)
# myscreen.exitonclick()


 
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemón Name", ["Pikachu","Squirtle", "Charmander"])
table.add_column("Type", ["Eletric","Water", "Fire"])

table.align = "c"


print(table)

 