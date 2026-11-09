namespace SnakeGame;

/// <summary>
/// A spot on the screen.
/// X is the column: it starts at 0 on the left and counts up as you go RIGHT.
/// Y is the row: it starts at 0 at the top and counts up as you go DOWN.
/// </summary>
/// <remarks>
/// A "record struct" is a small bundle of values. C# gives it some free extras,
/// such as letting us compare two positions with ==.
/// </remarks>
public readonly record struct Position(int X, int Y)
{
    /// <summary>
    /// Gives back a NEW position that is <paramref name="dx"/> columns across
    /// and <paramref name="dy"/> rows down from this one.
    /// </summary>
    public Position Move(int dx, int dy)
    {
        // TODO Step 3: replace the line below.
        // See docs/03-loops-and-moving.md
        throw new NotImplementedException("Step 3: Position.Move");
    }
}
