namespace SnakeGame.Tests;

// The board in these tests is 20 columns wide (0 to 19) and 10 rows tall (0 to 9).
public class Step7_FoodTests
{
    private readonly Board board = new Board(20, 10);

    // --- Part 1: growing ---

    [Fact]
    public void Growing_makes_the_snake_longer()
    {
        Snake snake = new Snake(new Position(5, 5), startLength: 1);

        snake.Grow(3);
        for (int i = 0; i < 5; i++)
        {
            snake.Move(Direction.Right, board);
        }

        Assert.Equal(4, snake.Length);
    }

    [Fact]
    public void Growing_happens_one_move_at_a_time()
    {
        Snake snake = new Snake(new Position(5, 5), startLength: 1);

        snake.Grow(2);

        snake.Move(Direction.Right, board);
        Assert.Equal(2, snake.Length);

        snake.Move(Direction.Right, board);
        Assert.Equal(3, snake.Length);

        snake.Move(Direction.Right, board);
        Assert.Equal(3, snake.Length);
    }

    // --- Part 2: placing food ---

    [Fact]
    public void Food_is_always_on_the_board()
    {
        // Giving Random a number (a "seed") makes it pick the same numbers every time we run the test.
        Random random = new Random(42);
        Snake snake = new Snake(new Position(5, 5), startLength: 1);

        for (int i = 0; i < 100; i++)
        {
            Position food = board.RandomEmptySpot(random, snake);

            Assert.InRange(food.X, 0, board.Width - 1);
            Assert.InRange(food.Y, 0, board.Height - 1);
        }
    }

    [Fact]
    public void Food_never_lands_on_the_snake()
    {
        // A tiny board with only 3 spots: (0,0) (1,0) (2,0)
        Board tinyBoard = new Board(3, 1);
        Random random = new Random(42);

        // Make a snake that covers (1,0) and (0,0), leaving only (2,0) free.
        Snake snake = new Snake(new Position(0, 0), startLength: 2);
        snake.Move(Direction.Right, tinyBoard);

        for (int i = 0; i < 20; i++)
        {
            Position food = tinyBoard.RandomEmptySpot(random, snake);

            Assert.Equal(new Position(2, 0), food);
        }
    }
}
