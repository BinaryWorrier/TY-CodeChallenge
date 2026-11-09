# Step 6: The tail

**Goal:** turn the `@` into a snake with a tail that follows it around.

**You'll learn:** lists, `foreach` loops, a neat trick for moving a snake.

## How the snake is stored

Open `src/SnakeGame/Snake.cs`. The snake's body is a **list** of positions:

```csharp
public List<Position> Body { get; } = new List<Position>();
```

`Body[0]` is the **head**. The last one in the list is the **tail**.

```
    o  o  o  @
    ^        ^
   tail     head

   Body = [ (8,5), (7,5), (6,5), (5,5) ]
             head                 tail
```

## The trick

Moving every part of the snake one by one would be a lot of work. Here's a much easier way:

```
Before:          o  o  o  @           Body = [ (8,5), (7,5), (6,5), (5,5) ]

1. Add a new head at the FRONT:
                 o  o  o  o  @        Body = [ (9,5), (8,5), (7,5), (6,5), (5,5) ]

2. Remove the tail from the BACK:
                    o  o  o  @        Body = [ (9,5), (8,5), (7,5), (6,5) ]
```

It looks like the whole snake moved, but we only changed the two ends!

## Growing at the start

A new snake starts as just a head. It grows to its full length over its first few moves. The constructor (the code that runs when a snake is made) sets this up for you:

```csharp
public Snake(Position start, int startLength)
{
    Body.Add(start);
    _growBy = startLength - 1;
}
```

`_growBy` counts how many more moves the snake should grow for. While `_growBy` is more than 0, **don't** remove the tail. Just take one off `_growBy` instead.

## Part A: write Move

Fill in `Move` in `Snake.cs`. It needs to:

1. Work out where the new head goes. Move the current `Head` in the `direction`, then wrap it on the `board`.
2. Put the new head at the **front** of `Body`.
3. If `_growBy` is more than 0, take 1 off it. Otherwise, remove the tail from the **back** of `Body`.

Useful bits of C#:

| Code | What it does |
|------|--------------|
| `Body.Insert(0, something)` | puts something at the front of the list |
| `Body.RemoveAt(Body.Count - 1)` | removes the last thing in the list |
| `Body.Count` | how many things are in the list |

<details>
<summary>Hint 1</summary>

For step 1 you need two things you've already built: `Position.Move` (Step 3) and `Board.Wrap` (Step 5). It's the same as the two lines you wrote in `Program.cs` in Step 5.
</details>

<details>
<summary>Hint 2</summary>

```csharp
Position newHead = board.Wrap(Head.Move(direction.Dx, direction.Dy));
Body.Insert(0, newHead);

if (_growBy > 0)
{
    // ???
}
else
{
    // ???
}
```
</details>

Run the tests:

```
dotnet test --filter Step6
```

## Part B: draw the snake

In `Program.cs`, the snake replaces `position`. Replace everything under `using SnakeGame;` with:

```csharp
Console.Clear();
Console.CursorVisible = false;

Board board = new Board(Console.WindowWidth, Console.WindowHeight - 1);
Snake snake = new Snake(new Position(5, 5), startLength: 8);
Direction direction = Direction.Right;
bool playing = true;

while (playing)
{
    // 1. Has a key been pressed?
    if (Console.KeyAvailable)
    {
        ConsoleKey key = Console.ReadKey(true).Key;

        if (key == ConsoleKey.Escape)
        {
            playing = false;
        }

        direction = Controls.ChangeDirection(key, direction);
    }

    // 2. Move the snake, but remember where its tail was first
    Position oldTail = snake.Tail;
    snake.Move(direction, board);

    // 3. Rub out the old tail, then draw the whole snake
    Draw(oldTail, ' ');
    foreach (Position part in snake.Body)
    {
        Draw(part, 'o');
    }
    Draw(snake.Head, '@');

    // 4. Wait a moment before the next tick
    Thread.Sleep(100);
}

Console.CursorVisible = true;
Console.Clear();

// A helper that draws one character at a position on the screen.
static void Draw(Position position, char symbol)
{
    Console.SetCursorPosition(position.X, position.Y);
    Console.Write(symbol);
}
```

`foreach` is a loop that goes through every item in a list. Here, it draws every part of the snake's body.

Why do we only rub out the **old tail**? Every other part of the snake is still part of the snake, so it gets drawn again anyway.

Run it. You have a snake! 🐍

## 🎯 Challenges

1. Make the snake start longer.
2. Draw the body in green and the head in yellow.
3. Try steering the snake straight back on itself. What happens? (You'll fix this in Step 8.)

## ✅ Done when

- [ ] The snake moves around with a tail following it
- [ ] The snake wraps around the edges, tail and all
- [ ] `dotnet test --filter "Step3|Step4|Step5|Step6"` passes

## 💾 Save your work

```
git add .
git commit -m "Step 6 done"
git push
```

**You've built the core of Snake!** If you want to keep going, try the bonus steps.

Next: [Step 7: Food and growing](07-food-and-growing.md) (bonus)
