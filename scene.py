class Scene:
    """
    a scene that contains prose, a list of choices and a dict of next scenes.

    Created by: Mark
    Claim: composition of two custom classes. Scene stores other scenes inside self.next_scenes.
    """
    def __init__(self, prose, choices):
        ## initializes with prose and choices
        self.prose = prose
        self.choices = choices
        self.next_scenes = {}

    def add_next(self, choice_number, scene):
        ## goes to the next scene based on the choice number
        self.next_scenes[choice_number] = scene

    def display(self):
        ## displays the prose and choices to the user
        print(self.prose)
        print()
        count = 1
        for choice in self.choices:
            print(str(count) + ") " + choice)
            count = count + 1

    def get_choice(self):
        ## gets the user's input and returns the next scene
        pick = input("\n> ")
        pick = int(pick)
        if pick == 1:
            return self.next_scenes[1]
        elif pick == 2:
            return self.next_scenes[2]
        elif pick == 3:
            return self.next_scenes[3]
        elif pick == 4:
            return self.next_scenes[4]
        else:
            print("Invalid choice.")


def run_game(starting_scene):
    ## runs the game
    current = starting_scene
    while current is not None:
        current.display()
        current = current.get_choice()

## the scenes below:
opening = Scene(
    "You stand at the entrance to a collapsed rail tunnel. Water drips somewhere ahead. A faded sign reads MAINTENANCE ONLY.",
    [
        "Go inside",
        "Check the sign more closely",
        "Walk around the hill",
        "Wait and listen"
    ]
)

inside = Scene(
    "The tunnel smells like wet concrete and rust. Your flashlight catches rail ties half-buried in gravel.",
    [
        "Keep going deeper",
        "Search the walls",
        "Turn back"
    ]
)

sign = Scene(
    "The sign is aluminum, bolted to rebar. Under MAINTENANCE ONLY someone scratched: NOT WORTH IT.",
    [
        "Go inside anyway",
        "Walk around the hill"
    ]
)

## the connections between the scenes:
opening.add_next(1, inside)
opening.add_next(2, sign)

sign.add_next(1, inside)

run_game(opening)