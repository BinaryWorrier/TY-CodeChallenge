import pytest

from board import Board
from controls import change_direction
from direction import UP, DOWN, LEFT, RIGHT
from position import Position
from snake import Snake

# The board in these tests is 20 columns wide (0 to 19) and 10 rows tall (0 to 9).
board = Board(20, 10)

# --- Part A: no turning straight back ---


def test_the_opposite_of_up_is_down():
    assert UP.opposite() == DOWN


def test_the_opposite_of_down_is_up():
    assert DOWN.opposite() == UP


def test_the_opposite_of_left_is_right():
    assert LEFT.opposite() == RIGHT


def test_the_opposite_of_right_is_left():
    assert RIGHT.opposite() == LEFT


@pytest.mark.parametrize("key", ["left", "a"])
def test_going_right_you_cannot_turn_straight_back_left(key):
    new_direction = change_direction(key, RIGHT)

    assert new_direction == RIGHT


@pytest.mark.parametrize("key", ["down", "s"])
def test_going_up_you_cannot_turn_straight_back_down(key):
    new_direction = change_direction(key, UP)

    assert new_direction == UP


# --- Part B: crashing into yourself ---


def test_a_straight_snake_has_not_hit_itself():
    snake = Snake(Position(5, 5), start_length=5)

    for i in range(6):
        snake.move(RIGHT, board)

    assert snake.hit_itself() == False


def test_a_snake_that_curls_round_into_its_body_has_hit_itself():
    snake = Snake(Position(5, 5), start_length=5)
    for i in range(4):
        snake.move(RIGHT, board)

    snake.move(DOWN, board)
    snake.move(LEFT, board)
    snake.move(UP, board)

    assert snake.hit_itself() == True


def test_chasing_your_own_tail_is_allowed():
    # The tail moves out of the way just as the head arrives, so this is not a crash.
    snake = Snake(Position(5, 5), start_length=4)

    snake.move(RIGHT, board)
    snake.move(DOWN, board)
    snake.move(LEFT, board)
    snake.move(UP, board)

    assert snake.hit_itself() == False
