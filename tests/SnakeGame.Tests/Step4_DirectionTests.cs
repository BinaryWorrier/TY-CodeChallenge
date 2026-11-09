namespace SnakeGame.Tests;

public class Step4_DirectionTests
{
    // --- Part 1: the four directions ---

    [Fact]
    public void Up_goes_towards_the_top_of_the_screen()
    {
        Assert.Equal(new Direction(0, -1), Direction.Up);
    }

    [Fact]
    public void Down_goes_towards_the_bottom_of_the_screen()
    {
        Assert.Equal(new Direction(0, 1), Direction.Down);
    }

    [Fact]
    public void Left_goes_towards_the_left_of_the_screen()
    {
        Assert.Equal(new Direction(-1, 0), Direction.Left);
    }

    [Fact]
    public void Right_goes_towards_the_right_of_the_screen()
    {
        Assert.Equal(new Direction(1, 0), Direction.Right);
    }

    // --- Part 2: turning with the keyboard ---

    [Theory]
    [InlineData(ConsoleKey.UpArrow)]
    [InlineData(ConsoleKey.W)]
    public void Up_keys_turn_up(ConsoleKey key)
    {
        Direction next = Controls.ChangeDirection(key, Direction.Right);

        Assert.Equal(Direction.Up, next);
    }

    [Theory]
    [InlineData(ConsoleKey.DownArrow)]
    [InlineData(ConsoleKey.S)]
    public void Down_keys_turn_down(ConsoleKey key)
    {
        Direction next = Controls.ChangeDirection(key, Direction.Right);

        Assert.Equal(Direction.Down, next);
    }

    [Theory]
    [InlineData(ConsoleKey.LeftArrow)]
    [InlineData(ConsoleKey.A)]
    public void Left_keys_turn_left(ConsoleKey key)
    {
        Direction next = Controls.ChangeDirection(key, Direction.Up);

        Assert.Equal(Direction.Left, next);
    }

    [Theory]
    [InlineData(ConsoleKey.RightArrow)]
    [InlineData(ConsoleKey.D)]
    public void Right_keys_turn_right(ConsoleKey key)
    {
        Direction next = Controls.ChangeDirection(key, Direction.Up);

        Assert.Equal(Direction.Right, next);
    }

    [Theory]
    [InlineData(ConsoleKey.X)]
    [InlineData(ConsoleKey.Q)]
    [InlineData(ConsoleKey.Enter)]
    public void Other_keys_keep_going_the_same_way(ConsoleKey key)
    {
        Direction next = Controls.ChangeDirection(key, Direction.Left);

        Assert.Equal(Direction.Left, next);
    }
}
