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
direction_choice =input("To begin, you are in the middle of the island with the choice of going right or left, do you go right or left?").lower()

if direction_choice == "right":
   choice2 = input('You have now entered a cave with minimal light '
        'and you do not know what lies ahead.'
        ' Do you continue or leave the cave? Type "continue" or "leave"').lower()
   if choice2 == "continue":
    Weapon_choice = input('Would you like to pick an axe, flashlight or a rock? Type "axe", "flashlight", "rock" ').lower()
    if Weapon_choice == "flashlight":
        print("You can now see the cave and have progressed safely to the end of the tunnel! Congratulations You have reached the treasure ")
    elif Weapon_choice == "rock":
        print("You can't see in the cave, game over!")
    elif Weapon_choice == "axe":
        print("You can't see in the cave, game over!")
    else:
       print("You left the cave, game over")
elif direction_choice == "left":
     choice3 = input('You fell into the river, do you swim or wait for a boat? '
          'Type "swim" or "wait"').lower()
     if choice3 == "wait":
         box_choice =input('A boat has arrived and has taken you across the river and you are now at the final stage.'
                           '\n You are now faced with a tiger and have to make a quick decision. '
               'There is are three boxes near you. Do you pick the left, middle or right box?').lower()
         if box_choice == "left":
             print("There is a pack of gum in the box. Game over, the tiger has eaten you!")
         if box_choice == "middle":
             print("There is a small rock in the box. Game Over, the tiger has eaten you!")
         if box_choice == "left":
            print("You have found a sleeping potion and put the tiger to sleep. You have won the game! "
            )
     else:
         print("You have been eaten by crocodiles. Game over")
else:
    print("Please select provided options")





