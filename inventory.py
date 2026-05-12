class Inventory:
    """Stores and manages items the player is carrying."""

    def __init__(self):
        """Initialize with an empty item list."""
        self.items = []

    def add_item(self, item):
        """Add an item to the inventory.
        """
        self.items.append(item)
        print(f"Added to inventory: {item}")

    def remove_item(self, item):
        """Remove an item from the inventory.
        """
        if item in self.items:
            self.items.remove(item)
            return True
        return False

    def __contains__(self, item):
        """Support 'in' checks on the inventory.

        Allows: 'key' in player.inventory
        """
        return item in self.items

    def __len__(self):
        """Return number of items in the inventory.

        Allows: len(player.inventory)
        """
        return len(self.items)

    def __iadd__(self, item):
        """Support += to add an item.

        Allows: player.inventory += 'gold'
        """
        self.add_item(item)
        return self

    def __repr__(self):
        """Return a string showing inventory contents."""
        return f"Inventory({self.items})"
