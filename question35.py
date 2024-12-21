'''
Create a Python program that greets the user with the message "Welcome to
the Magic Forest". Then, ask the user whether they want to go "north" or
"south". If they choose "south", print "Game Over". If they choose "north", ask
if they want to "cross the river" or "follow the path". If they choose "cross the
river", print "Game Over". If they choose "follow the path", ask them to choose
between "fairy", "ogre", or "elf". If they choose "ogre" or "fairy", print "Game
Over". If they choose "elf", print "You Win"
'''
print("Welcome to the Magic Forest!")


a = input("Do you want to go 'north' or 'south'? ").lower()

if a == "south":
    print("Game Over")
elif a== "north":

    b = input("Do you want to 'cross the \nriver'\n 'follow the path'? \n").lower()
    if b == "cross the river":
        print("Game Over")
    elif b == "follow the path":
        c= input("Choose between '\n fairy' \n, 'ogre' \n 'elf': \n").lower()
        if c == "fairy" or c == "ogre":
            print("Game Over")
        elif c == "elf":
            print("You Win")
        else:
            print("Invalid choice. Game Over")
    else:
        print("Invalid choice. Game Over")
else:
    print("Invalid choice. Game Over")