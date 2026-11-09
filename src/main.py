# Welcome to Snake!
# Start with the guide in docs/01-hello-console.md

# These lines let us use the game's building blocks (the screen, Position, Direction, Snake...).
# Leave them here at the top. We'll need them in later steps.
import time

import console
from board import Board
from controls import change_direction
from direction import RIGHT
from position import Position
from snake import Snake

print("Hello, Snake!")
