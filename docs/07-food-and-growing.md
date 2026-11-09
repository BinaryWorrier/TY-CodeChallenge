# Step 7: Food and growing (bonus)

**Goal:** put food on the screen. When the snake eats it, the snake grows and you score a point.

**You'll learn:** random numbers, `while` loops that search for something, checking whether a list contains something.

## Part A: Grow

Open `src/SnakeGame/Snake.cs` and fill in `Grow`.

You've already done the hard work! In Step 6, `Move` grows the snake while `_growBy` is more than 0. So `Grow` only has to add `amount` onto `_growBy`.

```
dotnet test --filter Step7
```

The two `Growing_...` tests should pass.

## Part B: a random empty spot

Food has to go somewhere random, but **not on top of the snake**. Open `src/SnakeGame/Board.cs` and fill in `RandomEmptySpot`.

The plan:

```
keep doing this:
    pick a random column and a random row
    if the snake isn't there, that's our spot!
```

Useful bits of C#:

| Code | What it does |
|------|--------------|
| `random.Next(10)` | a random whole number from 0 to 9 (it never gives 10) |
| `snake.Body.Contains(spot)` | `true` if `spot` is part of the snake |
| `!` | means "not", so `!snake.Body.Contains(spot)` means "the snake is NOT there" |
| `while (true) { ... }` | loops forever, until you `return` |

<details>
<summary>Hint 1</summary>

`random.Next(Width)` gives a column that is definitely on the board. Why?
</details>

<details>
<summary>Hint 2</summary>

```csharp
while (true)
{
    Position spot = new Position(random.Next(Width), random.Next(Height));

    if (???)
    {
        return spot;
    }
}
```
</details>

> If the snake ever filled the whole board, this would loop forever. If you manage that, you've won anyway!

Run the tests until they're green:

```
dotnet test --filter Step7
```

## Part C: food in the game

Update `Program.cs`. These are the changes from Step 6:

**Before the loop**, start the snake in the middle and add the food and score:

```csharp
Snake snake = new Snake(new Position(board.Width / 2, board.Height / 2), startLength: 5);
Direction direction = Direction.Right;
Random random = new Random();
Position food = board.RandomEmptySpot(random, snake);
int score = 0;
bool playing = true;

Draw(food, '*');
```

**Inside the loop**, after drawing the snake and before `Thread.Sleep`:

```csharp
    // Did we eat the food?
    if (snake.Head == food)
    {
        score = score + 1;
        snake.Grow(3);
        food = board.RandomEmptySpot(random, snake);
        Draw(food, '*');
    }

    // Show the score on the bottom row
    Console.SetCursorPosition(0, board.Height);
    Console.Write($"Score: {score}    Press Esc to quit");
```

Remember we kept the bottom row free in Step 5? That's where the score goes.

Run it and eat some food!

## 🎯 Challenges

1. Make the food red. (Remember `Console.ResetColor()` afterwards!)
2. Make the game get faster as your score goes up. Hint: instead of `Thread.Sleep(100)`, use a variable for the wait time and make it smaller each time you eat.
3. Add `Console.Beep();` when the snake eats.
4. Sometimes put down special gold food (`$`) that's worth 5 points.

## ✅ Done when

- [ ] Food appears, and when the snake eats it, it grows and the score goes up
- [ ] `dotnet test --filter "Step3|Step4|Step5|Step6|Step7"` passes

## 💾 Save your work

```
git add .
git commit -m "Step 7 done"
git push
```

Next: [Step 8: Game over](08-game-over.md) (bonus)
