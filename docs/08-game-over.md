# Step 8: Game over (bonus)

**Goal:** if the snake crashes into itself, it's game over. Also stop the snake turning straight back on itself.

**You'll learn:** changing code safely with tests, looping through a list by number.

## Part A: no U-turns

At the moment, if the snake is going right and you press left, it turns straight back into its own body. Real Snake doesn't let you do that.

### Opposite

Open `src/SnakeGame/Direction.cs` and fill in `Opposite`. It should give back the direction that points the other way. The opposite of `(1, 0)` is `(-1, 0)`.

<details>
<summary>Hint</summary>

Flip the sign of both numbers. `-Dx` is the opposite of `Dx`.
</details>

### Change ChangeDirection

Now open `Controls.cs`. You wrote `ChangeDirection` in Step 4. Change it so that if the new direction is the opposite of `current`, it keeps going the `current` way instead.

<details>
<summary>Hint</summary>

If your Step 4 code `return`s as soon as it finds the key, you'll need to change it a bit. Put the new direction in a variable first, then check it at the end:

```csharp
Direction wanted = current;

if (key == ConsoleKey.UpArrow || key == ConsoleKey.W)
{
    wanted = Direction.Up;
}
// ...and the other keys...

if (wanted == current.Opposite)
{
    return ???;
}

return wanted;
```
</details>

### ⭐ Tests are a safety net

You've just changed code you wrote in Step 4. Did you break it? You don't have to guess. Run **both** sets of tests:

```
dotnet test --filter "Step4|Step8"
```

If the Step 4 tests still pass, you know your change didn't break anything. This is one of the best reasons to write tests.

## Part B: crashing into yourself

Open `Snake.cs` and fill in `HitItself`. It should be `true` if the head is in the same place as any **other** part of the body.

The head is `Body[0]`, so check `Body[1]`, `Body[2]` and so on, up to the end of the list.

<details>
<summary>Hint 1</summary>

A `for` loop that starts at 1 instead of 0:

```csharp
for (int i = 1; i < Body.Count; i++)
{
    // is Body[i] in the same place as Head?
}
```

Why start at 1 and not 0?
</details>

<details>
<summary>Hint 2</summary>

As soon as you find a match, `return true;`. If the loop finishes without finding one, `return false;`.
</details>

```
dotnet test --filter Step8
```

Have a look at the test called `Chasing_your_own_tail_is_allowed`. Why isn't that a crash?

## Part C: game over in the game

In `Program.cs`, inside the loop, after the food check:

```csharp
    // Did we crash into ourselves?
    if (snake.HitItself())
    {
        playing = false;
    }
```

And **after** the loop, replace the last two lines (`Console.CursorVisible = true;` and `Console.Clear();`) with:

```csharp
// Game over!
string message = $"GAME OVER - you scored {score}";
Console.SetCursorPosition((board.Width - message.Length) / 2, board.Height / 2);
Console.Write(message);

// Throw away any keys still waiting, then wait for a new key press.
while (Console.KeyAvailable)
{
    Console.ReadKey(true);
}
Console.ReadKey(true);

Console.CursorVisible = true;
Console.Clear();
```

Run it and crash on purpose!

## Check everything

You've finished, so now all the tests should pass:

```
dotnet test
```

Look for `Passed!` and `Failed: 0`.

## 💾 Save your work

```
git add .
git commit -m "Step 8 done"
git push
```

## 🚀 What next?

You've built a whole game. Here are some ideas to make it your own. For anything that isn't just drawing, try writing a test first.

- **Walls mode:** hitting the edge is game over instead of wrapping round.
- **Speed up:** the game gets faster as the score goes up.
- **High score:** save the best score to a file with `File.WriteAllText` and read it back with `File.ReadAllText`.
- **Pause:** press P to pause and unpause.
- **Obstacles:** put some `#` blocks on the board that you mustn't hit.
- **Two players:** one snake on the arrow keys, one on W A S D. You'll need to split `ChangeDirection` into two. Whoever crashes first loses. You are two people, after all!
