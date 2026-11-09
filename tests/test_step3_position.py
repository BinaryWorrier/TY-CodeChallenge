import pytest

from position import Position


def test_moving_right_adds_one_to_x():
    start = Position(5, 5)

    moved = start.move(1, 0)

    assert moved == Position(6, 5)


def test_moving_left_takes_one_from_x():
    start = Position(5, 5)

    moved = start.move(-1, 0)

    assert moved == Position(4, 5)


def test_moving_down_adds_one_to_y():
    start = Position(5, 5)

    moved = start.move(0, 1)

    assert moved == Position(5, 6)


def test_moving_up_takes_one_from_y():
    start = Position(5, 5)

    moved = start.move(0, -1)

    assert moved == Position(5, 4)


def test_moving_gives_a_new_position_and_leaves_the_old_one_alone():
    start = Position(5, 5)

    start.move(1, 1)

    assert start == Position(5, 5)


# parametrize runs this test once for each line in the list.
# Each line is: x, y, dx, dy, expected_x, expected_y
@pytest.mark.parametrize(
    "x, y, dx, dy, expected_x, expected_y",
    [
        (0, 0, 3, 4, 3, 4),
        (10, 10, -2, -3, 8, 7),
        (7, 2, 0, 0, 7, 2),
    ],
)
def test_moving_by_any_amount(x, y, dx, dy, expected_x, expected_y):
    start = Position(x, y)

    moved = start.move(dx, dy)

    assert moved == Position(expected_x, expected_y)
