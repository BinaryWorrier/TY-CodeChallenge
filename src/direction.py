from dataclasses import dataclass


# Which way something is moving.
# dx is how many columns to move each turn, dy is how many rows.
@dataclass(frozen=True)
class Direction:
    dx: int
    dy: int

    def opposite(self):
        """Gives back the direction that points back the way we came."""
        # TODO Step 8: replace the line below.
        # See docs/08-game-over.md
        raise NotImplementedError("Step 8: Direction.opposite")


# The four directions the snake can go.
# Names in CAPITALS are "constants": values that never change while the program runs.
#
# TODO Step 4: put the right numbers in for each direction.
# Remember: on the screen, rows count DOWN from the top.
# See docs/04-game-loop-and-keys.md
UP = Direction(0, 0)
DOWN = Direction(0, 0)
LEFT = Direction(0, 0)
RIGHT = Direction(0, 0)
