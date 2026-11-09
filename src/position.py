from dataclasses import dataclass


# A spot on the screen.
# x is the column: it starts at 0 on the left and counts up as you go RIGHT.
# y is the row: it starts at 0 at the top and counts up as you go DOWN.
#
# @dataclass(frozen=True) writes some boring code for us. It means we can:
#   - make a position with Position(5, 3)
#   - compare two positions with ==
#   - NOT change a position once it's made (that's what "frozen" means)
@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def move(self, dx, dy):
        """Gives back a NEW position that is dx columns across and dy rows down from this one."""
        # TODO Step 3: replace the line below.
        # See docs/03-loops-and-moving.md
        raise NotImplementedError("Step 3: Position.move")
