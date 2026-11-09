namespace SnakeGame;

/// <summary>
/// Turns key presses into directions.
/// </summary>
public static class Controls
{
    /// <summary>
    /// Works out which way to go after a key is pressed.
    /// </summary>
    /// <param name="key">The key that was pressed.</param>
    /// <param name="current">The way we are going right now.</param>
    /// <returns>The way we should go next.</returns>
    public static Direction ChangeDirection(ConsoleKey key, Direction current)
    {
        // TODO Step 4: replace the line below.
        // The arrow keys AND W, A, S, D should both work.
        // Any other key should keep going the same way (return current).
        // See docs/04-game-loop-and-keys.md
        //
        // TODO Step 8: don't let the snake turn straight back on itself.
        // See docs/08-game-over.md
        throw new NotImplementedException("Step 4: Controls.ChangeDirection");
    }
}
