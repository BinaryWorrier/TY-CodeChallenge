namespace SnakeGame.Tests;

public class Step3_PositionTests
{
    [Fact]
    public void Moving_right_adds_one_to_X()
    {
        Position start = new Position(5, 5);

        Position moved = start.Move(1, 0);

        Assert.Equal(new Position(6, 5), moved);
    }

    [Fact]
    public void Moving_left_takes_one_from_X()
    {
        Position start = new Position(5, 5);

        Position moved = start.Move(-1, 0);

        Assert.Equal(new Position(4, 5), moved);
    }

    [Fact]
    public void Moving_down_adds_one_to_Y()
    {
        Position start = new Position(5, 5);

        Position moved = start.Move(0, 1);

        Assert.Equal(new Position(5, 6), moved);
    }

    [Fact]
    public void Moving_up_takes_one_from_Y()
    {
        Position start = new Position(5, 5);

        Position moved = start.Move(0, -1);

        Assert.Equal(new Position(5, 4), moved);
    }

    [Fact]
    public void Moving_gives_a_new_position_and_leaves_the_old_one_alone()
    {
        Position start = new Position(5, 5);

        start.Move(1, 1);

        Assert.Equal(new Position(5, 5), start);
    }

    // A Theory is a test that runs once for each line of InlineData.
    [Theory]
    [InlineData(0, 0, 3, 4, 3, 4)]
    [InlineData(10, 10, -2, -3, 8, 7)]
    [InlineData(7, 2, 0, 0, 7, 2)]
    public void Moving_by_any_amount(int x, int y, int dx, int dy, int expectedX, int expectedY)
    {
        Position start = new Position(x, y);

        Position moved = start.Move(dx, dy);

        Assert.Equal(new Position(expectedX, expectedY), moved);
    }
}
