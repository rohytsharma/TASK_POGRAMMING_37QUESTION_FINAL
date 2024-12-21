"""
Create a Python program that greets the user with the message "Welcome to
the Haunted House". Then, ask the user whether they want to go "upstairs" or
"downstairs". If they choose "downstairs", print "Game Over". If they choose
"upstairs", ask if they want to "enter the room" or "stay outside". If they choose
"enter the room", print "Game Over". If they choose "stay outside", ask them
to choose between "ghost", "vampire", or "werewolf". If they choose "ghost" or
"vampire", print "Game Over". If they choose "werewolf", print "You Win".
"""
print("Welcome to the Haunted House")

data_1= input("Do you want to go 'upstairs' or 'downstairs'? ").lower()

if data_1 == "downstairs":
    print("Game Over")
elif data_1 == "upstairs":
    choice1_data = input("Do you want to \n'enter the room'\n 'stay outside'\n? ").lower()
    if choice1_data == "enter the room":
        print("Game Over")
    elif choice1_data == "stay outside":
        choice2_data = input("Choose between \n'ghost'\n 'vampire'\n  'werewolf': \n").lower()
        if choice2_data == "ghost" or choice2_data == "vampire":
            print("Game Over")
        elif choice2_data == "werewolf":
            print("You Win")
        else:
            print("Invalid choice. Game Over")
    else:
        print("Invalid choice. Game Over")
else:
    print("Invalid choice. Game Over")