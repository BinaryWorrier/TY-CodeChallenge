from direction import Direction, UP, DOWN, LEFT, RIGHT


def change_direction(key, current):
    """
    Works out which way to go after a key is pressed.

    key is the name of the key that was pressed, such as "up" or "w".
    current is the way we're going right now.
    Gives back the way we should go next.
    """
    # TODO Step 4: replace the line below.
    # The arrow keys AND W, A, S, D should both work.
    # Any other key should keep going the same way (give back current).
    # See docs/04-game-loop-and-keys.md
    #
    # TODO Step 8: don't let the snake turn straight back on itself.
    # See docs/08-game-over.md
    raise NotImplementedError("Step 4: change_direction")
