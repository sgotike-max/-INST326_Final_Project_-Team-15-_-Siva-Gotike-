"Main file to start the text adventure game."

from scene import approach
from engine import run_game


def main():
    "Run the game starting from the approach scene."
    run_game(approach)


if __name__ == "__main__":
    main()
