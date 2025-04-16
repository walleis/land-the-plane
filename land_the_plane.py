print(r'''
            ______
            _\ _~-\___
    =  = ==(____AA____D
                \_____\___________________,-~~~~~~~`-.._
                /     o O o o o o O O o o o o o o O o  |\_
                `~-.__        ___..----..                  )
                      `---~~\___________/------------`````
                      =  ===(_________D
        ''')

print("Welcome aboard!")
print("Your mission is to land the plane and you are in the middle of the ocean. "
      "Somehow the pilots faint down, good luck!")
fuel = 80

choice1 = (input(f"Fuel: {fuel} - You see an island far away at your right, where would you go?"
                 f" 'Left' or 'Right'? ")).strip().lower()
if choice1 == "right":
    fuel -= 40
    choice2 = input(f"Fuel: {fuel} - You choose right. The island is too far away, would you continue? 'Y' or 'N': ").strip().lower()
    if choice2 == "y":
        fuel -= 20
        choice3 = input(f"Fuel: {fuel} - After coming close, you see there is an airport! "
                            "What would you do? 'Land', 'Contact the Control Tower or 'Pray'? ").strip().lower()
        if choice3 == "land":
            print("After taking some risks, you were able to land! "
                            "Now you are an hero and everyone loves you! Thanks for playing.").strip().lower()
        elif choice3 == "pray":
            print("After some divine intervention, you were able to save everyone. Now you are in heaven amongst the other passengers. SECRET ENDING!")
        elif choice3 == "contact the control tower":
            fuel -= 20
            print(f"Fuel: {fuel} - You did not have enough time to contact the control tower and follow the instructions,"
                    f" the fuel goes to zero and the plane crashes. GAME OVER!")
        else:
            fuel -= 20
            print(
                f"Fuel: {fuel} - You ignore the island, continues flying and the fuel goes to zero, falling straight into ocean. GAME OVER!")
    else:
        fuel -= 40
        print(f"Fuel: {fuel} - You ignored the only chance of landing. At the middle of the ocean, the fuel goes to zero and"
              f" you go straight to ocean. GAME OVER!")

else:
    fuel -= 80
    print(f"Fuel: {fuel} - After that decision, you spent countless hours without seeing an place to land and the fuel goes to zero."
          " GAME OVER!")


