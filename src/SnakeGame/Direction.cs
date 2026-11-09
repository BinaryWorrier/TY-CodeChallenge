namespace SnakeGame;

/// <summary>
/// Which way something is moving.
/// Dx is how many columns to move each turn, Dy is how many rows.
/// </summary>
public readonly record struct Direction(int Dx, int Dy)
{
    // TODO Step 4: put the right numbers in for each direction.
    // Remember: on the screen, rows count DOWN from the top.
    // See docs/04-game-loop-and-keys.md
    public static readonly Direction Up = new Direction(0, 0);
    public static readonly Direction Down = new Direction(0, 0);
    public static readonly Direction Left = new Direction(0, 0);
    public static readonly Direction Right = new Direction(0, 0);

    /// <summary>
    /// The direction that points back the way we came.
    /// </summary>
    public Direction Opposite
    {
        get
        {
            // TODO Step 8: replace the line below.
            // See docs/08-game-over.md
            throw new NotImplementedException("Step 8: Direction.Opposite");
        }
    }
}
