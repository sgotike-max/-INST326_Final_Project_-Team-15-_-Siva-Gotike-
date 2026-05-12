class Scene:
    """The engine of the game."""

    def __init__(self, prose, choices):
        self.prose = prose
        self.choices = choices
        self.next_scenes = {}  # composition: Scene stores Scene objects (claimed by mark kuo)

    def add_next(self, choice_number, scene):
        self.next_scenes[choice_number] = scene

    def __str__(self):  # magic method: string representation of Scene (claimed by mark kuo)
        result = self.prose + "\n"
        count = 1
        for choice in self.choices:
            result = result + "\n" + str(count) + ") " + choice
            count = count + 1
        return result

    def __len__(self):  # magic method: returns number of choices (claimed by mark kuo)
        return len(self.choices)

    def get_choice(self,player):
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
    name = input("Enter your name:")
    player = Player(name)
    current = starting_scene
    while current is not None:
        print()
        player.show_status()
        print(current)
        if not player:
            print("\n--- GAME OVER ---")
            break
        current = current.get_choice(player)
