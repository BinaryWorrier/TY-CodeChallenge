# Step 5: Wrap around

**Goal:** go off the right of the screen and come back on the left, and the same for the other edges.

**You'll learn:** `if` with `<` and `>=`, classes with properties, off-by-one mistakes.

## The board

Open `src/SnakeGame/Board.cs`. A `Board` has a `Width` (number of columns) and a `Height` (number of rows).

If the board is 20 wide, the columns are numbered **0 to 19**. So column 20 is already off the board!

```
column:  0  1  2  ...  17 18 19 | 20
         .  .  .  ...  .  .  .  |  @   <- off the board!
```

## Part A: Wrap

Fill in `Wrap`. It's given a position that might have gone off the board, and gives back a position that's on the board:

| If... | ...then |
|-------|---------|
| X is too big (off the right) | X becomes 0 |
| X is too small (off the left) | X becomes the last column |
| Y is too big (off the bottom) | Y becomes 0 |
| Y is too small (off the top) | Y becomes the last row |
| none of these | leave it alone |

The tests use a board 20 wide and 10 tall. Look in `tests/SnakeGame.Tests/Step5_WrapTests.cs` to see exactly what they expect.

<details>
<summary>Hint 1</summary>

You can't change `position.X` directly, because positions can't be changed once they're made. Copy X and Y into variables, fix them, then make a new position at the end:

```csharp
int x = position.X;
int y = position.Y;

// fix x and y here

return new Position(x, y);
```
</details>

<details>
<summary>Hint 2</summary>

```csharp
if (x >= Width)
{
    x = 0;
}
```

Why `>=` and not `>`? What's the last column number on a board that is `Width` wide?
</details>

Run the tests:

```
dotnet test --filter Step5
```

If `Off_the_right_edge_comes_back_on_the_left` fails but the others pass, you've probably made an **off-by-one** mistake. They're one of the most common bugs in programming, which is exactly why we test for them.

## Part B: use it in the game

In `Program.cs`, make a board the size of the window. Put this just after `Console.CursorVisible = false;`:

```csharp
// The board is the whole window, except the bottom row (we'll use that for the score later).
Board board = new Board(Console.WindowWidth, Console.WindowHeight - 1);
```

Then change the moving line in the loop from:

```csharp
    position = position.Move(direction.Dx, direction.Dy);
```

to:

```csharp
    Position next = position.Move(direction.Dx, direction.Dy);
    position = board.Wrap(next);
```

Run it. Drive off every edge. No more crashes!

> Don't resize the window while the game is running. The board won't know it's changed size.

## 🎯 Challenges

1. Make the board smaller than the window, for example `new Board(40, 15)`. Draw a border around it with `#` characters before the game loop starts.
2. Hard: write `Wrap` a different way, using the `%` (remainder) operator. Your tests will tell you if it still works!

## ✅ Done when

- [ ] The `@` goes off each edge and comes back on the other side
- [ ] `dotnet test --filter "Step3|Step4|Step5"` passes

## 💾 Save your work

```
git add .
git commit -m "Step 5 done"
git push
```

Next: [Step 6: The tail](06-the-tail.md)
