namespace SnakeGame.Tests;

// The board in these tests is 20 columns wide (0 to 19) and 10 rows tall (0 to 9).
public class Step5_WrapTests
{
    private readonly Board board = new Board(20, 10);

    [Theory]
    [InlineData(5, 5)]
    [InlineData(0, 0)]
    [InlineData(19, 0)]
    [InlineData(0, 9)]
    [InlineData(19, 9)]
    public void A_position_on_the_board_does_not_change(int x, int y)
    {
        Position wrapped = board.Wrap(new Position(x, y));

        Assert.Equal(new Position(x, y), wrapped);
    }

    [Fact]
    public void Off_the_right_edge_comes_back_on_the_left()
    {
        Position wrapped = board.Wrap(new Position(20, 5));

        Assert.Equal(new Position(0, 5), wrapped);
    }

    [Fact]
    public void Off_the_left_edge_comes_back_on_the_right()
    {
        Position wrapped = board.Wrap(new Position(-1, 5));

        Assert.Equal(new Position(19, 5), wrapped);
    }

    [Fact]
    public void Off_the_bottom_comes_back_at_the_top()
    {
        Position wrapped = board.Wrap(new Position(5, 10));

        Assert.Equal(new Position(5, 0), wrapped);
    }

    [Fact]
    public void Off_the_top_comes_back_at_the_bottom()
    {
        Position wrapped = board.Wrap(new Position(5, -1));

        Assert.Equal(new Position(5, 9), wrapped);
    }

    [Fact]
    public void Off_a_corner_wraps_both_ways()
    {
        Position wrapped = board.Wrap(new Position(20, -1));

        Assert.Equal(new Position(0, 9), wrapped);
    }
}
