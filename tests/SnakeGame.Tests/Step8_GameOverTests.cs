namespace SnakeGame.Tests;

// The board in these tests is 20 columns wide (0 to 19) and 10 rows tall (0 to 9).
public class Step8_GameOverTests
{
    private readonly Board board = new Board(20, 10);

    // --- Part 1: no turning straight back ---

    [Fact]
    public void The_opposite_of_up_is_down()
    {
        Assert.Equal(Direction.Down, Direction.Up.Opposite);
    }

    [Fact]
    public void The_opposite_of_down_is_up()
    {
        Assert.Equal(Direction.Up, Direction.Down.Opposite);
    }

    [Fact]
    public void The_opposite_of_left_is_right()
    {
        Assert.Equal(Direction.Right, Direction.Left.Opposite);
    }

    [Fact]
    public void The_opposite_of_right_is_left()
    {
        Assert.Equal(Direction.Left, Direction.Right.Opposite);
    }

    [Theory]
    [InlineData(ConsoleKey.LeftArrow)]
    [InlineData(ConsoleKey.A)]
    public void Going_right_you_cannot_turn_straight_back_left(ConsoleKey key)
    {
        Direction next = Controls.ChangeDirection(key, Direction.Right);

        Assert.Equal(Direction.Right, next);
    }

    [Theory]
    [InlineData(ConsoleKey.DownArrow)]
    [InlineData(ConsoleKey.S)]
    public void Going_up_you_cannot_turn_straight_back_down(ConsoleKey key)
    {
        Direction next = Controls.ChangeDirection(key, Direction.Up);

        Assert.Equal(Direction.Up, next);
    }

    // --- Part 2: crashing into yourself ---

    [Fact]
    public void A_straight_snake_has_not_hit_itself()
    {
        Snake snake = new Snake(new Position(5, 5), startLength: 5);

        for (int i = 0; i < 6; i++)
        {
            snake.Move(Direction.Right, board);
        }

        Assert.False(snake.HitItself());
    }

    [Fact]
    public void A_snake_that_curls_round_into_its_body_has_hit_itself()
    {
        Snake snake = new Snake(new Position(5, 5), startLength: 5);
        for (int i = 0; i < 4; i++)
        {
            snake.Move(Direction.Right, board);
        }

        snake.Move(Direction.Down, board);
        snake.Move(Direction.Left, board);
        snake.Move(Direction.Up, board);

        Assert.True(snake.HitItself());
    }

    [Fact]
    public void Chasing_your_own_tail_is_allowed()
    {
        // The tail moves out of the way just as the head arrives, so this is not a crash.
        Snake snake = new Snake(new Position(5, 5), startLength: 4);

        snake.Move(Direction.Right, board);
        snake.Move(Direction.Down, board);
        snake.Move(Direction.Left, board);
        snake.Move(Direction.Up, board);

        Assert.False(snake.HitItself());
    }
}
