# Land the Plane

## Description

This is a simple text-based adventure game where you are the unexpected pilot of a plane flying over the ocean. The original pilots have fainted, and it's up to you to make critical decisions to try and land the plane safely before the fuel runs out. Your mission is to navigate and choose the right actions to reach a potential landing spot.

## How to Play

1.  **Run the script:** Execute the Python script. You will be greeted with an ASCII art of a plane and a welcome message setting the scene.
2.  **Make choices:** The game will present you with scenarios and ask for your decisions by typing in specific keywords (e.g., 'left', 'right', 'y', 'n', 'land', 'contact the control tower', 'pray'). Type your choice in lowercase and press Enter.
3.  **Manage fuel:** Your fuel level is a critical resource. Different choices will consume varying amounts of fuel. Pay attention to the fuel updates after each decision.
4.  **Try to land:** Your goal is to make the right sequence of choices to successfully land the plane. Incorrect decisions or running out of fuel will lead to a "GAME OVER".
5.  **Explore endings:** The game has different outcomes based on your choices, including a secret ending!

## Functionality

* **Text-based Adventure:** The game progresses through text prompts and user input.
* **Decision-Making:** The story branches based on the choices you make at each step.
* **Fuel Management:** A `fuel` variable tracks your remaining fuel, and certain actions deplete it. Running out of fuel results in a game over.
* **Multiple Endings:** The game has at least two distinct "GAME OVER" scenarios and a successful landing scenario, along with a secret ending for a specific choice.
* **ASCII Art:** Displays an ASCII art representation of a plane at the beginning.

## Requirements

* Python 3.x (No external libraries are required as it uses only built-in Python functions.)

## Installation

No specific installation is needed. Save the provided code as a `.py` file (e.g., `emergency_landing.py`) and run it using a Python interpreter.

## Code Explanation

* **ASCII Art:** The `print(r'''...''')` statement displays a multi-line raw string containing an ASCII art representation of a plane. The `r''` denotes a raw string, which treats backslashes as literal characters.
* **Welcome Messages:** Prints introductory messages to set the game's context and your mission.
* **`fuel = 80`:** Initializes the starting fuel level to 80 units.
* **`choice1 = ...`:** Presents the first choice to the player: go 'Left' or 'Right' upon seeing an island. The input is taken, stripped of leading/trailing whitespace, and converted to lowercase for case-insensitive comparison.
* **`if choice1 == "right":`:** If the player chooses 'right':
    * `fuel -= 40`: 40 units of fuel are consumed.
    * `choice2 = ...`: A second choice is presented: continue towards the distant island ('y') or not ('n').
    * **Nested `if choice2 == "y":`:** If the player chooses to continue:
        * `fuel -= 20`: Another 20 units of fuel are consumed.
        * `choice3 = ...`: A third choice is presented upon seeing an airport: 'Land', 'Contact the Control Tower', or 'Pray'.
        * **Nested `if/elif/else` for `choice3`:** Different outcomes are printed based on the player's final choice, including a successful landing, a secret ending for 'pray', and a game over for 'contact the control tower' (due to insufficient fuel) or any other input (ignoring the island and running out of fuel).
    * **`else:` for `choice2 == "n"`:** If the player chooses not to continue towards the island, fuel is lost, and a game over scenario is triggered.
* **`else:` for `choice1 == "left"`:** If the player chooses 'left' at the first decision, a significant amount of fuel is lost, and a game over scenario is triggered due to not finding a landing spot.
* **`.strip().lower()`:** This method is used on the `input()` to remove any leading or trailing whitespace from the user's input and convert it to lowercase, ensuring that the comparison with the expected strings ('right', 'y', 'land', etc.) is case-insensitive.
