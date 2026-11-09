from board import Board
from direction import RIGHT, DOWN
from position import Position
from snake import Snake

# The board in these tests is 20 columns wide (0 to 19) and 10 rows tall (0 to 9).
board = Board(20, 10)


def test_a_new_snake_is_just_a_head():
    snake = Snake(Position(5, 5), start_length=4)

    assert snake.length == 1
    assert snake.head == Position(5, 5)


def test_moving_moves_the_head():
    snake = Snake(Position(5, 5), start_length=1)

    snake.move(RIGHT, board)

    assert snake.head == Position(6, 5)


def test_a_snake_of_length_one_stays_length_one():
    snake = Snake(Position(5, 5), start_length=1)

    snake.move(RIGHT, board)
    snake.move(RIGHT, board)
    snake.move(RIGHT, board)

    assert snake.length == 1


def test_the_snake_grows_until_it_reaches_its_start_length():
    snake = Snake(Position(5, 5), start_length=4)

    snake.move(RIGHT, board)
    assert snake.length == 2

    snake.move(RIGHT, board)
    assert snake.length == 3

    snake.move(RIGHT, board)
    assert snake.length == 4

    snake.move(RIGHT, board)
    assert snake.length == 4


def test_the_body_follows_the_head():
    snake = Snake(Position(5, 5), start_length=3)

    snake.move(RIGHT, board)
    snake.move(RIGHT, board)
    snake.move(DOWN, board)

    # Head first, tail last.
    expected = [
        Position(7, 6),
        Position(7, 5),
        Position(6, 5),
    ]
    assert snake.body == expected
    assert snake.tail == Position(6, 5)


def test_the_snake_wraps_round_the_edges():
    snake = Snake(Position(19, 5), start_length=1)

    snake.move(RIGHT, board)

    assert snake.head == Position(0, 5)
