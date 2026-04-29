class Scene:
    def __init__(self, prose, choices):
        self.prose = prose
        self.choices = choices
        self.next_scenes = {}

    def add_next(self, choice_number, scene):
        self.next_scenes[choice_number] = scene  
        # composition: Scene stores Scene objects | Claimed by: mark_kuo

    def __str__(self):  
        # magic method: string representation of Scene | claimed by: mark_kuo
        result = self.prose + "\n"
        count = 1
        for choice in self.choices:
            result = result + "\n" + str(count) + ") " + choice
            count = count + 1
        return result

    def __len__(self):  
        # magic method: returns number of choices | claimed by: mark_kuo
        return len(self.choices)

    def get_choice(self):
        while True:
            pick = input("\n> ")
            try:
                pick = int(pick)
            except ValueError:
                print("Enter a number.")
                continue
            if pick < 1 or pick > len(self):
                print("Pick between 1 and " + str(len(self)) + ".")
                continue
            if pick not in self.next_scenes:
                print("That path isn't available yet.")
                continue
            return self.next_scenes[pick]


def run_game(starting_scene):
    current = starting_scene
    while current is not None:
        print(current)
        current = current.get_choice()
    print("\nEnd of the road.")


# --- example setup ---

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

opening.add_next(1, inside)
opening.add_next(2, sign)


sign.add_next(1, inside)


run_game(opening)