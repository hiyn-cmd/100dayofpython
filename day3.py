print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
road = input("You encoutered a crossroad. Where do you want to go \nType \"left\" or \"right\"  ")
if road == "left":
    river = input("You're at a river. Do you swim across or wait? \nType \"swim\" or \"wait\" ")
    if river == "wait":
        door = input(
            "You see a boat nearby and used it to cross the river.\nYou see a castle with a red door, a blue door and a yellow door. Which will you go through? \nType\"red\",\"blue\" or \"yellow\" ")
        if door == "yellow":
            print("You found the treasure!")
        elif door == "red":
            print("You got burned by fire. Game Over")
        elif door == "blue":
            print("You got mauled by beasts. Game Over")
        else:
            print("That's not a door. Game Over")
    else:
        print("You got attacked by trout. Game Over")
else:
    print("You fell into a hole. Game Over")
