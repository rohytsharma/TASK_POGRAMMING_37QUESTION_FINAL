"""
Create a Python program that greets the user with the message "Welcome to
the Jungle Adventure". Then, ask the user whether they want to go "left" or
"right". If they choose "right", print "Game Over". If they choose "left", ask if
they want to "climb a tree" or "explore the cave". If they choose "climb a tree",
print "Game Over". If they choose "explore the cave", ask them to choose
between "bear", "tiger", or "snake". If they choose "bear" or "tiger", print
"Game Over". If they choose "snake", print "You Win".
"""
print("Welcome to the Jungle Adventure!")

choice1_data = input("Do you want to go 'left' or 'right'? ").lower()

if choice1_data == "right":
    print("Game Over")
elif choice1_data == "left":
    choice2_data = input("Do you want to \n 'climb a tree' \n  'explore the cave'?\n ").lower()
    if choice2_data == "climb a tree":
        print("Game Over")
    elif choice2_data== "explore the cave":
        choice3_data = input("Choose between \n' bear' \n 'tiger' \n 'snake' \n: ").lower()
        if choice3_data == "bear" or choice3_data == "tiger":
            print("Game Over")
        elif choice3_data == "snake":
            print("You Win")
        else:
            print("Invalid choice. Game Over")
    else:
        print("Invalid choice. Game Over")
else:
    print("Invalid choice. Game Over")