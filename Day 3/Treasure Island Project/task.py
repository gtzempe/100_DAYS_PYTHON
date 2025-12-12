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
print("Good luck")


step = input("\nYou are at a cross road. Where do you want to go?\n"
             "     Type 'left' or 'right': ")


if step == "left":

    swim_or_wait = input("\nYou've come to a lake. As you see around there is an island in the middle of the lake.\n"
          "You have two options. Do you want to wait for a boat or swim across?\n"
                         "     Type 'wait' or 'swim': ")
    if swim_or_wait == "wait":

        color_door = input("\nYou arrive at the island unharmed. Nice.\n"
                           "You are going straight and you find a house with 3 doors.\n "
                           "One red, one yellow and one blue. Which color door do you choose to open?\n"
                           "     Type 'red', 'yellow' and 'blue': ")

        if color_door == "red":
            print("\nBurned by fire. Game Over.")
        elif color_door == "blue":
            print("\nEaten by beasts. Game Over.")
        elif color_door == "yellow":
            print("\nYOU FOUND THE TREASURE. YOU WIN!!!")
        else:
            print("\nGame Over. Wrong choice.")
    else:
        print("\nAttacked by trout. Game Over.")
else:
    print("\nYou fall into a hole. Game Over.")