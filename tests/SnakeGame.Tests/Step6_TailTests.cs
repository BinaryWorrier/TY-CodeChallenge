namespace SnakeGame.Tests;

// The board in these tests is 20 columns wide (0 to 19) and 10 rows tall (0 to 9).
public class Step6_TailTests
{
    private readonly Board board = new Board(20, 10);

    [Fact]
    public void A_new_snake_is_just_a_head()
    {
        Snake snake = new Snake(new Position(5, 5), startLength: 4);

        Assert.Equal(1, snake.Length);
        Assert.Equal(new Position(5, 5), snake.Head);
    }

    [Fact]
    public void Moving_moves_the_head()
    {
        Snake snake = new Snake(new Position(5, 5), startLength: 1);

        snake.Move(Direction.Right, board);

        Assert.Equal(new Position(6, 5), snake.Head);
    }

    [Fact]
    public void A_snake_of_length_one_stays_length_one()
    {
        Snake snake = new Snake(new Position(5, 5), startLength: 1);

        snake.Move(Direction.Right, board);
        snake.Move(Direction.Right, board);
        snake.Move(Direction.Right, board);

        Assert.Equal(1, snake.Length);
    }

    [Fact]
    public void The_snake_grows_until_it_reaches_its_start_length()
    {
        Snake snake = new Snake(new Position(5, 5), startLength: 4);

        snake.Move(Direction.Right, board);
        Assert.Equal(2, snake.Length);

        snake.Move(Direction.Right, board);
        Assert.Equal(3, snake.Length);

        snake.Move(Direction.Right, board);
        Assert.Equal(4, snake.Length);

        snake.Move(Direction.Right, board);
        Assert.Equal(4, snake.Length);
    }

    [Fact]
    public void The_body_follows_the_head()
    {
        Snake snake = new Snake(new Position(5, 5), startLength: 3);

        snake.Move(Direction.Right, board);
        snake.Move(Direction.Right, board);
        snake.Move(Direction.Down, board);

        // Head first, tail last.
        Position[] expected =
        {
            new Position(7, 6),
            new Position(7, 5),
            new Position(6, 5),
        };
        Assert.Equal(expected, snake.Body);
        Assert.Equal(new Position(6, 5), snake.Tail);
    }

    [Fact]
    public void The_snake_wraps_round_the_edges()
    {
        Snake snake = new Snake(new Position(19, 5), startLength: 1);

        snake.Move(Direction.Right, board);

        Assert.Equal(new Position(0, 5), snake.Head);
    }
}
