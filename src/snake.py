class Snake:
    """
    The snake! Its body is a list of positions.
    body[0] is the head. The last item in the list is the tail.
    """

    def __init__(self, start, start_length):
        """
        Makes a new snake. It starts as just a head at start,
        and grows to start_length parts as it moves.
        """
        # Every part of the snake. body[0] is the head.
        self.body = [start]

        # How many more moves the snake should grow for.
        # While this is more than 0, the tail stays where it is and the snake gets longer.
        self._grow_by = start_length - 1

    # @property means you can write snake.head instead of snake.head()
    @property
    def head(self):
        """The front of the snake."""
        return self.body[0]

    @property
    def tail(self):
        """The very end of the snake. (In Python, [-1] means "the last one".)"""
        return self.body[-1]

    @property
    def length(self):
        """How many parts the snake has."""
        return len(self.body)

    def move(self, direction, board):
        """Moves the snake one step in direction, wrapping round the edges of the board."""
        # TODO Step 6: replace the line below.
        # See docs/06-the-tail.md
        raise NotImplementedError("Step 6: Snake.move")

    def grow(self, amount):
        """Makes the snake grow by amount parts over its next few moves."""
        # TODO Step 7: replace the line below.
        # See docs/07-food-and-growing.md
        raise NotImplementedError("Step 7: Snake.grow")

    def hit_itself(self):
        """True if the snake's head has bumped into another part of its body."""
        # TODO Step 8: replace the line below.
        # See docs/08-game-over.md
        raise NotImplementedError("Step 8: Snake.hit_itself")
