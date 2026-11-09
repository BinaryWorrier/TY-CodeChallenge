# Step 3: Loops and moving

**Goal:** make a character move across the screen, then write the code that the first unit tests check.

**You'll learn:** `for` loops, `Thread.Sleep`, how animation works, your first unit test.

## Part A: a loop

A **loop** runs the same code again and again. Try this in `Program.cs` (under `using SnakeGame;`):

```csharp
for (int i = 0; i < 10; i++)
{
    Console.WriteLine("Lap " + i);
}
```

Read it as: *"start `i` at 0; keep going while `i` is less than 10; add 1 to `i` each time round."*

Run it. Why does it stop at 9 and not 10?

## Part B: make something move

Animation is a trick. Each time round the loop:

1. **Rub out** the character (write a space over it).
2. **Change** its position.
3. **Draw** it in the new place.
4. **Wait** a moment, so our eyes can see it.

Replace everything under `using SnakeGame;` with:

```csharp
Console.Clear();
Console.CursorVisible = false;

int x = 5;
int y = 5;

for (int i = 0; i < 10; i++)
{
    // 1. rub out the old @
    Console.SetCursorPosition(x, y);
    Console.Write(' ');

    // 2. move one column to the right
    x = x + 1;

    // 3. draw the @ in its new place
    Console.SetCursorPosition(x, y);
    Console.Write('@');

    // 4. wait 200 milliseconds (a fifth of a second)
    Thread.Sleep(200);
}

Console.CursorVisible = true;
Console.SetCursorPosition(0, y + 2);
```

Run it. You should see the `@` slide to the right.

### Add a "delta"

**Delta** means "how much something changes". Let's use `dx` for the change in column and `dy` for the change in row. Add these under `int y = 5;`:

```csharp
int dx = 1;
int dy = 0;
```

and change step 2 inside the loop to:

```csharp
    // 2. move by the delta
    x = x + dx;
    y = y + dy;
```

Now you can change the direction just by changing `dx` and `dy`.

### 🎯 Challenges

1. Make it move **down** instead. What do `dx` and `dy` need to be?
2. Make it move **diagonally**.
3. Make it move **up**. Careful: if it goes above row 0 the program crashes. Start lower down!
4. Make it go 30 steps and go faster.
5. Comment out the "rub out" lines (put `//` in front). What happens?

## Part C: your first unit test

A **unit test** is a small piece of code that checks that another piece of code gives the right answer. Instead of running the game and looking, the computer checks for you, in less than a second.

### Position

Moving by `dx` and `dy` is going to happen a lot in this game, so it's worth putting it somewhere it can be tested. Open `src/SnakeGame/Position.cs`:

```csharp
public readonly record struct Position(int X, int Y)
{
    public Position Move(int dx, int dy)
    {
        // TODO Step 3: replace the line below.
        throw new NotImplementedException("Step 3: Position.Move");
    }
}
```

A `Position` holds an `X` (the column) and a `Y` (the row). `Move` should give back a **new** position that is `dx` columns across and `dy` rows down.

### Look at the tests first

Open `tests/SnakeGame.Tests/Step3_PositionTests.cs`. Here's one test:

```csharp
[Fact]
public void Moving_right_adds_one_to_X()
{
    Position start = new Position(5, 5);

    Position moved = start.Move(1, 0);

    Assert.Equal(new Position(6, 5), moved);
}
```

Every test has three parts:

1. **Set up**: make a position at (5, 5).
2. **Do the thing**: move it by (1, 0).
3. **Check**: `Assert.Equal(expected, actual)` checks that we got (6, 5). If not, the test **fails**.

### Run the tests: red 🔴

```
dotnet test --filter Step3
```

They all fail with `NotImplementedException : Step 3: Position.Move`. That's expected, because you haven't written it yet.

### Make them pass: green 🟢

Replace the `throw ...` line in `Position.Move` so it gives back a new position.

<details>
<summary>Hint 1</summary>

You make a new position with `new Position(something, something)`. Inside `Move`, you can use `X` and `Y` to get this position's column and row.
</details>

<details>
<summary>Hint 2</summary>

```csharp
return new Position(X + ???, Y + ???);
```
</details>

Run the tests again until you see:

```
Passed!  - Failed: 0, Passed: 8, Skipped: 0, Total: 8
```

### Use Position in your program

Now tidy up `Program.cs` to use `Position`. A small helper called `Draw` saves us typing `SetCursorPosition` again and again:

```csharp
Console.Clear();
Console.CursorVisible = false;

Position position = new Position(5, 5);
int dx = 1;
int dy = 0;

for (int i = 0; i < 10; i++)
{
    Draw(position, ' ');                 // 1. rub out the old @
    position = position.Move(dx, dy);    // 2. move by the delta
    Draw(position, '@');                 // 3. draw the @ in its new place
    Thread.Sleep(200);                   // 4. wait
}

Console.CursorVisible = true;
Console.SetCursorPosition(0, position.Y + 2);

// A helper that draws one character at a position on the screen.
static void Draw(Position position, char symbol)
{
    Console.SetCursorPosition(position.X, position.Y);
    Console.Write(symbol);
}
```

Run it. It should do exactly the same as before, but the code is shorter and the moving part is tested.

## ✅ Done when

- [ ] The `@` slides across the screen
- [ ] You can make it go in different directions by changing `dx` and `dy`
- [ ] `dotnet test --filter Step3` passes

## 💾 Save your work

```
git add .
git commit -m "Step 3 done"
git push
```

Next: [Step 4: Game loop and keys](04-game-loop-and-keys.md)
