import pytest

from controls import change_direction
from direction import Direction, UP, DOWN, LEFT, RIGHT

# --- Part A: the four directions ---


def test_up_goes_towards_the_top_of_the_screen():
    assert UP == Direction(0, -1)


def test_down_goes_towards_the_bottom_of_the_screen():
    assert DOWN == Direction(0, 1)


def test_left_goes_towards_the_left_of_the_screen():
    assert LEFT == Direction(-1, 0)


def test_right_goes_towards_the_right_of_the_screen():
    assert RIGHT == Direction(1, 0)


# --- Part B: turning with the keyboard ---
# Each of these tests runs once for each key in its list.


@pytest.mark.parametrize("key", ["up", "w"])
def test_up_keys_turn_up(key):
    new_direction = change_direction(key, RIGHT)

    assert new_direction == UP


@pytest.mark.parametrize("key", ["down", "s"])
def test_down_keys_turn_down(key):
    new_direction = change_direction(key, RIGHT)

    assert new_direction == DOWN


@pytest.mark.parametrize("key", ["left", "a"])
def test_left_keys_turn_left(key):
    new_direction = change_direction(key, UP)

    assert new_direction == LEFT


@pytest.mark.parametrize("key", ["right", "d"])
def test_right_keys_turn_right(key):
    new_direction = change_direction(key, UP)

    assert new_direction == RIGHT


@pytest.mark.parametrize("key", ["x", "q", "enter"])
def test_other_keys_keep_going_the_same_way(key):
    new_direction = change_direction(key, LEFT)

    assert new_direction == LEFT
