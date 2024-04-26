
print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
print('Entering other inputs aside from the provided will result in an error of this game.')
print("Choosing an unexpected choice MAY result in a surprise.. Who knows..")

#first scenario: forked crossroads
choice1 = input('You\'re at a crossroad where the road is split into 2. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
    # second scenario: cave and a lake
    choice2 = input('At the end of the road, there is a cave on your left and a road that leads to the lake on your right. Type "cave" to go to the cave or "lake" to go to the lake \n').lower()
    if choice2 == "cave":
        print("There is a grizzly brown bear sleeping on the cave. He wakes up and eats you. Game Over.")
    elif choice2 == "lake":
        # third scenario: boat or a bridge
        choice3 = input('You chose to go to the end of the path to reach the lake. There is a near-collapsing bridge and a boat. Type "boat" to ride the boat to the other side or "bridge" to cross the bridge instead. \n').lower()
        if choice3 == "bridge":
            # FINALE
            print("Somehow you crossed the bridge just fine because it still holds your body weight for long.")
            choiceFinal = input('There is a tombstone and 13 feet far from it is a huge "X" on the ground. Think carefully because you know the treasure is in one of these 2. Type "tombstone" to dig the tombstone or type "X" to dig the X on the ground. \n').lower()
            if choiceFinal == "tombstone":
                print("Somehow the treasure was the inside to coffin all along provided by a letter of the one who buried the treasure saying :The real treasure is not found always on what you will expect for. You win!")
            else:
                print("Say Goodbye because the 'X' was a hole full of snakes and dangerous predators. Game Over.")
        elif choice3 == "boat":
            print("You have been attacked by piranhas and crocodiles. Game Over.")
        else:
            print("You chose to do nothing and starve to death. You are a lazy ass person. Game Over.")

    else:
        print("You chose to do nothing. Game Over.")
else:
    print("It is a Dead End. Game Over.")





# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
#
# #Write your code below this line 👇
#
# choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
# if choice1 == "left":
#   choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
#   if choice2 == "wait":
#     choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
#     if choice3 == "red":
#       print("It's a room full of fire. Game Over.")
#     elif choice3 == "yellow":
#       print("You found the treasure! You Win!")
#     elif choice3 == "blue":
#       print("You enter a room of beasts. Game Over.")
#     else:
#       print("You chose a door that doesn't exist. Game Over.")
#   else:
#     print("You get attacked by an angry trout. Game Over.")
# else:
#   print("You fell into a hole. Game Over.")

