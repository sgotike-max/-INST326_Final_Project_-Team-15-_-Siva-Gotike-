class GameState:
    """Tracks the player's choices and history throughout the game."""
    def __init__(self, player_name, max_attempts=3):
        """Sets up a fresh game state for the player.
        Technique: optional parameters and keyword arguments (#2)
        """
        self.player_name = player_name
        self.max_attempts = max_attempts
        self.attempts = 0
        self.choices_made = []
        self.scenes_visited = []
        self.outcomes = []
    def record_choice(self, scene_name, choice_number):
        """Saves the choice the player made at a scene."""
        self.choices_made.append((scene_name, choice_number))
        if scene_name not in self.scenes_visited:
            self.scenes_visited.append(scene_name)
    def record_outcome(self, outcome):
        """Saves the result of a completed run."""
        self.attempts += 1
        self.outcomes.append(outcome)
    def get_play_style(self):
        """Figures out how the player approaches the game based on their choices.
        Weights each choice by how risky the scene was, then scores the run.
        Technique: comprehensions and generator expressions (#8)
        """
        risk_weights = {
            "approach": 3,
            "wall_climb": 5,
            "vault_door": 4,
            "escape_heavy": 5,
            "escape_light": 2
        }
        if len(self.choices_made) == 0:
            return "Unknown"
        weighted_score = sum(
            risk_weights.get(scene, 1) * (1 if choice == 1 else 0)
            for scene, choice in self.choices_made
        )
        max_possible = sum(risk_weights.get(scene, 1) for scene, _ in self.choices_made)
        ratio = weighted_score / max_possible if max_possible > 0 else 0
        if ratio >= 0.7:
            return "Reckless"
        elif ratio >= 0.4:
            return "Calculated"
        else:
            return "Cautious"
    def has_visited(self, scene_name):
        """Returns True if the player has been to this scene before."""
        return scene_name in self.scenes_visited
    def attempts_remaining(self):
        """Returns how many tries the player has left."""
        return self.max_attempts - self.attempts
    def summary(self):
        """Prints a recap of the player's runs."""
        print(f"\n=== Run Summary: {self.player_name} ===")
        print(f"Total attempts:  {self.attempts}")
        print(f"Play style:      {self.get_play_style()}")
        print(f"Scenes visited:  {len(self.scenes_visited)}")
        print(f"Outcomes:")
        for i, outcome in enumerate(self.outcomes):
            print(f"  Run {i + 1}: {outcome}")
        print("=" * 34)
    def __repr__(self):
        return f"GameState(player={self.player_name}, attempts={self.attempts})"
