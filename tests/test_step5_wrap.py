import pytest

from board import Board
from position import Position

# The board in these tests is 20 columns wide (0 to 19) and 10 rows tall (0 to 9).
board = Board(20, 10)


@pytest.mark.parametrize(
    "x, y",
    [
        (5, 5),
        (0, 0),
        (19, 0),
        (0, 9),
        (19, 9),
    ],
)
def test_a_position_on_the_board_does_not_change(x, y):
    wrapped = board.wrap(Position(x, y))

    assert wrapped == Position(x, y)


def test_off_the_right_edge_comes_back_on_the_left():
    wrapped = board.wrap(Position(20, 5))

    assert wrapped == Position(0, 5)


def test_off_the_left_edge_comes_back_on_the_right():
    wrapped = board.wrap(Position(-1, 5))

    assert wrapped == Position(19, 5)


def test_off_the_bottom_comes_back_at_the_top():
    wrapped = board.wrap(Position(5, 10))

    assert wrapped == Position(5, 0)


def test_off_the_top_comes_back_at_the_bottom():
    wrapped = board.wrap(Position(5, -1))

    assert wrapped == Position(5, 9)


def test_off_a_corner_wraps_both_ways():
    wrapped = board.wrap(Position(20, -1))

    assert wrapped == Position(0, 9)
