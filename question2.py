print("Welcome to Treasure Land")
direction_data = input("Choose a direction: \n Right \n Left: \n")
if direction_data=="Right":
    print("Game over")
elif direction_data=="left" or direction_data=='Left':
    action_data=input("Do you want to Swim or wait? ")

    if action_data == "Swim":
        print("game over")
    elif action_data=="Wait" or action_data=="wait":
      color_data=input("Please Select a color: \n Red \n Blue \n yellow: \n")
      if color_data=="Red" or color_data=="red" or color_data=="blue" or color_data=="blue":
         print("Game over")
      elif color_data=="Yellow" or color_data=="yellow":
         print("you won")
else:
    print("Choose correct direction")