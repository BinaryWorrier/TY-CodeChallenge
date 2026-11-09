namespace SnakeGame;

/// <summary>
/// The playing area.
/// Columns go from 0 to Width - 1 and rows go from 0 to Height - 1.
/// </summary>
public class Board
{
    public int Width { get; }
    public int Height { get; }

    public Board(int width, int height)
    {
        Width = width;
        Height = height;
    }

    /// <summary>
    /// If a position has gone off one edge of the board, bring it back on
    /// at the opposite edge. A position that is already on the board comes
    /// back unchanged.
    /// </summary>
    public Position Wrap(Position position)
    {
        // TODO Step 5: replace the line below.
        // See docs/05-wrap-around.md
        throw new NotImplementedException("Step 5: Board.Wrap");
    }

    /// <summary>
    /// Picks a random spot on the board that the snake is NOT on.
    /// </summary>
    public Position RandomEmptySpot(Random random, Snake snake)
    {
        // TODO Step 7: replace the line below.
        // See docs/07-food-and-growing.md
        throw new NotImplementedException("Step 7: Board.RandomEmptySpot");
    }
}
