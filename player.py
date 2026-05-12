from inventory import Inventory


class Player:
    """Represents the player in the text adventure game.
    """

    MAX_HEALTH = 100

    def __init__(self, name):
        """Initialize a new player with full health and empty inventory.
        """
        self.name = name
        self.health = Player.MAX_HEALTH
        self.inventory = Inventory()
        self.alive = True

    def take_damage(self, amount):
        """Reduce health by the given amount.
        """
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.alive = False
            print(f"\n{self.name} didn't make it.")

    def heal(self, amount):
        """Restore health, capped at MAX_HEALTH. 
        """
        self.health += amount
        if self.health > Player.MAX_HEALTH:
            self.health = Player.MAX_HEALTH

    def pick_up(self, item):
        """Add an item to the player's inventory.
        """
        self.inventory.add_item(item)

    def has_item(self, item):
        """Check if the player is carrying a specific item.
        """
        return item in self.inventory

    def show_status(self):
        """Print the player's current health and inventory."""
        print(f"\n[ {self.name} | Health: {self.health}/{Player.MAX_HEALTH} ]")
        if len(self.inventory) == 0:
            print("Inventory: empty")
        else:
            print(f"Inventory: {', '.join(self.inventory.items)}")

    def __bool__(self):
        """
        Allows the engine to check: if player:
        """
        return self.alive

    def __repr__(self):
        return f"Player(name={self.name}, health={self.health}, alive={self.alive})"