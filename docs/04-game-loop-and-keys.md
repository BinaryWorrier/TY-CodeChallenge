# Step 4: Game loop and keys

**Goal:** a loop that keeps running until you press Esc, with the arrow keys steering the `@`.

**You'll learn:** `while` loops, `bool`, `if`, reading the keyboard without stopping the game.

## The game loop

Nearly every game ever made works like this:

```
while the game is still going:
    1. check the keyboard
    2. update things (move!)
    3. draw
    4. wait a moment
```

Each time round is called a **tick** or a **frame**.

## Part A: directions

Our snake can go four ways. Open `src/SnakeGame/Direction.cs`:

```csharp
public static readonly Direction Up = new Direction(0, 0);
public static readonly Direction Down = new Direction(0, 0);
public static readonly Direction Left = new Direction(0, 0);
public static readonly Direction Right = new Direction(0, 0);
```

A `Direction` is just a `dx` and a `dy`, like in Step 3. Right now they're all `(0, 0)`, which means "don't move". Put in the right numbers.

⚠️ Remember from Step 2: rows count **down** from the top. Which way is "up"?

Check with:

```
dotnet test --filter Step4
```

The first four tests (`Up_goes_towards...`, `Down_goes_towards...` and so on) should now pass. The others still fail. That's Part B.

## Part B: from keys to directions

Open `src/SnakeGame/Controls.cs`. `ChangeDirection` is given the key that was pressed and the direction we're going now. It gives back the direction we should go next.

The rules are:

| Key pressed | New direction |
|-------------|---------------|
| ↑ or W | Up |
| ↓ or S | Down |
| ← or A | Left |
| → or D | Right |
| anything else | keep going the same way |

In C#, the keys are called `ConsoleKey.UpArrow`, `ConsoleKey.W`, `ConsoleKey.DownArrow`, `ConsoleKey.S` and so on.

<details>
<summary>Hint 1</summary>

Use `if` to check which key it was. `||` means "or":

```csharp
if (key == ConsoleKey.UpArrow || key == ConsoleKey.W)
{
    return Direction.Up;
}
```
</details>

<details>
<summary>Hint 2</summary>

After checking all four directions, what should happen if none of them matched? Look at the `current` parameter.
</details>

Run the tests until they're all green:

```
dotnet test --filter Step4
```

## Part C: the game loop

Replace everything under `using SnakeGame;` in `Program.cs` with:

```csharp
Console.Clear();
Console.CursorVisible = false;

Position position = new Position(5, 5);
Direction direction = Direction.Right;
bool playing = true;

while (playing)
{
    // 1. Has a key been pressed? KeyAvailable doesn't wait - it just checks.
    if (Console.KeyAvailable)
    {
        ConsoleKey key = Console.ReadKey(true).Key;

        if (key == ConsoleKey.Escape)
        {
            playing = false;
        }

        direction = Controls.ChangeDirection(key, direction);
    }

    // 2. and 3. Rub out, move, draw
    Draw(position, ' ');
    position = position.Move(direction.Dx, direction.Dy);
    Draw(position, '@');

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

Some new things:

- `bool` holds either `true` or `false`.
- `while (playing)` keeps looping as long as `playing` is `true`.
- `Console.KeyAvailable` is `true` if a key is waiting to be read. We check this first so the game doesn't **stop and wait** for a key, because the `@` has to keep moving.
- `Console.ReadKey(true)` reads the key. The `true` means "don't print it on the screen".

Run it and steer with the arrow keys. Press **Esc** to quit.

### 💥 What happens at the edge?

Drive the `@` off the edge of the screen. The program crashes with an `ArgumentOutOfRangeException`. That's because you can't put the cursor somewhere that isn't on the screen.

You'll fix that in the next step!

## 🎯 Challenges

1. Change `Thread.Sleep(100)` to make the game faster or slower.
2. Use a different character instead of `@`.
3. Comment out the line that rubs out the old `@`. Now you've got a drawing program!
4. Make the space bar stop the `@` (hint: a `Direction` of `(0, 0)` doesn't move). You'll need to add a test for it too. Copy one of the tests in `Step4_DirectionTests.cs` and change it.

## ✅ Done when

- [ ] You can steer the `@` with the arrow keys **and** W, A, S, D
- [ ] Esc quits the game
- [ ] `dotnet test --filter "Step3|Step4"` passes

## 💾 Save your work

```
git add .
git commit -m "Step 4 done"
git push
```

Next: [Step 5: Wrap around](05-wrap-around.md)
