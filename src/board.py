import random

from position import Position


class Board:
    """
    The playing area.
    Columns go from 0 to width - 1 and rows go from 0 to height - 1.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def wrap(self, position):
        """
        If a position has gone off one edge of the board, bring it back on
        at the opposite edge. A position that is already on the board comes
        back unchanged.
        """
        # TODO Step 5: replace the line below.
        # See docs/05-wrap-around.md
        raise NotImplementedError("Step 5: Board.wrap")

    def random_empty_spot(self, snake):
        """Picks a random spot on the board that the snake is NOT on."""
        # TODO Step 7: replace the line below.
        # See docs/07-food-and-growing.md
        raise NotImplementedError("Step 7: Board.random_empty_spot")
