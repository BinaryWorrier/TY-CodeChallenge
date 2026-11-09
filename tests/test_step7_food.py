import random

from board import Board
from direction import RIGHT
from position import Position
from snake import Snake

# The board in these tests is 20 columns wide (0 to 19) and 10 rows tall (0 to 9).
board = Board(20, 10)

# --- Part A: growing ---


def test_growing_makes_the_snake_longer():
    snake = Snake(Position(5, 5), start_length=1)

    snake.grow(3)
    for i in range(5):
        snake.move(RIGHT, board)

    assert snake.length == 4


def test_growing_happens_one_move_at_a_time():
    snake = Snake(Position(5, 5), start_length=1)

    snake.grow(2)

    snake.move(RIGHT, board)
    assert snake.length == 2

    snake.move(RIGHT, board)
    assert snake.length == 3

    snake.move(RIGHT, board)
    assert snake.length == 3


# --- Part B: placing food ---


def test_food_is_always_on_the_board():
    # Giving random a "seed" number makes it pick the same numbers every time we run the test.
    random.seed(42)
    snake = Snake(Position(5, 5), start_length=1)

    for i in range(100):
        food = board.random_empty_spot(snake)

        assert 0 <= food.x <= board.width - 1
        assert 0 <= food.y <= board.height - 1


def test_food_never_lands_on_the_snake():
    # A tiny board with only 3 spots: (0,0) (1,0) (2,0)
    tiny_board = Board(3, 1)
    random.seed(42)

    # Make a snake that covers (1,0) and (0,0), leaving only (2,0) free.
    snake = Snake(Position(0, 0), start_length=2)
    snake.move(RIGHT, tiny_board)

    for i in range(20):
        food = tiny_board.random_empty_spot(snake)

        assert food == Position(2, 0)


def test_food_does_not_always_land_in_the_same_place():
    random.seed(42)
    snake = Snake(Position(5, 5), start_length=1)

    first_food = board.random_empty_spot(snake)
    found_a_different_spot = False
    for i in range(20):
        if board.random_empty_spot(snake) != first_food:
            found_a_different_spot = True

    assert found_a_different_spot
