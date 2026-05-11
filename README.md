Text Adventure Game

Siva Gotike, Miabonita Tebo, Devin Akyen, Mark Kuo

Game Description - This project is a text adventure game that lets the player advance through a narrative by responding to different events via selection. Each time the player is put into an event they get to choose what action they will take, changing the current game state and bringing them to the next event until they complete the game (by winning). As you progress through the story you need to make wise decisions, some simple problems and manage restricted amounts of resources (Examples- health, inventory).

main.py: Contains the primary game loop and runs the actual game
player.py: The player's data (like health/inventory) is defined by the class Player
scenes.py: Where you will find each of the story scenarios and how they branch out
game_state.py: Keeps track of where you are in the game and what you have chosen along your journey
input_handler.py: Processes and validates any user input

Annotated Bibliography
Python Documentation (https://docs.python.org)
	Used to understand Python syntax, classes, and functions while building the game.
Class Notes and Lecture Slides(In the lectures)
	Used to guide the structure of the program and apply concepts learned in class.
General Programming Resources
	Used for help with logic, debugging, and organizing code into modules.

Atribution Table

| Name | Claim | Location |

| Mark Kuo | magic methods | def_len and def_str |

| Mark Kuo | function storing objects | self.next_scene |