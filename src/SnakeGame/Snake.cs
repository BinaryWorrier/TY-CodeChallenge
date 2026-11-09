namespace SnakeGame;

/// <summary>
/// The snake! Its body is a list of positions.
/// Body[0] is the head. The last item in the list is the tail.
/// </summary>
public class Snake
{
    // How many more moves the snake should grow for.
    // While this is more than 0, the tail stays where it is and the snake gets longer.
    private int _growBy;

    /// <summary>Every part of the snake. Body[0] is the head.</summary>
    public List<Position> Body { get; } = new List<Position>();

    /// <summary>The front of the snake.</summary>
    public Position Head => Body[0];

    /// <summary>The very end of the snake.</summary>
    public Position Tail => Body[Body.Count - 1];

    /// <summary>How many parts the snake has.</summary>
    public int Length => Body.Count;

    /// <summary>
    /// Makes a new snake. It starts as just a head at <paramref name="start"/>
    /// and grows to <paramref name="startLength"/> parts as it moves.
    /// </summary>
    public Snake(Position start, int startLength)
    {
        Body.Add(start);
        _growBy = startLength - 1;
    }

    /// <summary>
    /// Moves the snake one step in <paramref name="direction"/>,
    /// wrapping round the edges of the board.
    /// </summary>
    public void Move(Direction direction, Board board)
    {
        // TODO Step 6: replace the line below.
        // See docs/06-the-tail.md
        throw new NotImplementedException("Step 6: Snake.Move");
    }

    /// <summary>
    /// Makes the snake grow by <paramref name="amount"/> parts over its next few moves.
    /// </summary>
    public void Grow(int amount)
    {
        // TODO Step 7: replace the line below.
        // See docs/07-food-and-growing.md
        throw new NotImplementedException("Step 7: Snake.Grow");
    }

    /// <summary>
    /// True if the snake's head has bumped into another part of its body.
    /// </summary>
    public bool HitItself()
    {
        // TODO Step 8: replace the line below.
        // See docs/08-game-over.md
        throw new NotImplementedException("Step 8: Snake.HitItself");
    }
}
