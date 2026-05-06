class Scene:
    def __init__(self, prose, choices):
        self.prose = prose
        self.choices = choices
        self.next_scenes = {}

    def add_next(self, choice_number, scene):
        self.next_scenes[choice_number] = scene

    def __str__(self):
        result = self.prose + "\n"
        count = 1
        for choice in self.choices:
            result = result + "\n" + str(count) + ") " + choice
            count = count + 1
        return result

    def __len__(self):
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