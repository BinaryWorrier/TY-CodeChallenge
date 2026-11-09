# Step 7: Food and growing (bonus)

**Goal:** put food on the screen. When the snake eats it, the snake grows and you score a point.

**You'll learn:** random numbers, `while` loops that search for something, checking whether a list contains something.

## Part A: grow

Open `src/snake.py` and fill in `grow`.

You've already done the hard work! In Step 6, `move` grows the snake while `self._grow_by` is more than 0. So `grow` only has to add `amount` onto `self._grow_by`.

```
python -m pytest -k step7
```

The two `test_growing_...` tests should pass.

## Part B: a random empty spot

Food has to go somewhere random, but **not on top of the snake**. Open `src/board.py` and fill in `random_empty_spot`.

The plan:

```
keep doing this:
    pick a random column and a random row
    if the snake isn't there, that's our spot!
```

Useful bits of Python:

| Code | What it does |
|------|--------------|
| `random.randrange(10)` | a random whole number from 0 to 9 (it never gives 10) |
| `spot in snake.body` | `True` if `spot` is part of the snake |
| `not` | means "not", so `spot not in snake.body` means "the snake is NOT there" |
| `while True:` | loops forever, until you `return` |

The `import random` line at the top of `board.py` is already there, ready for you.

<details>
<summary>Hint 1</summary>

`random.randrange(self.width)` gives a column that is definitely on the board. Why?
</details>

<details>
<summary>Hint 2</summary>

```python
while True:
    spot = Position(random.randrange(self.width), random.randrange(self.height))

    if ???:
        return spot
```
</details>

> If the snake ever filled the whole board, this would loop forever. If you manage that, you've won anyway!

Run the tests until they're green:

```
python -m pytest -k step7
```

## Part C: food in the game

Update `main.py`. These are the changes from Step 6.

**Before the loop**, replace the `snake = ...`, `direction = ...` and `playing = ...` lines with these, which start the snake in the middle and add the food and the score:

```python
snake = Snake(Position(board.width // 2, board.height // 2), start_length=5)
direction = RIGHT
food = board.random_empty_spot(snake)
score = 0
playing = True

draw(food, "*")
```

Remember `//` from Step 2? It divides and gives a whole number, because there's no such thing as column 40.5.

**Inside the loop**, after drawing the snake and before `time.sleep`:

```python
    # Did we eat the food?
    if snake.head == food:
        score = score + 1
        snake.grow(3)
        food = board.random_empty_spot(snake)
        draw(food, "*")

    # Show the score on the bottom row
    console.set_cursor_position(0, board.height)
    console.write(f"Score: {score}    Press Esc to quit")
```

These lines are inside the `while` loop, so they need to be indented by 4 spaces, the same as the other lines in the loop.

Remember we kept the bottom row free in Step 5? That's where the score goes.

Run it and eat some food!

## 🎯 Challenges

1. Make the food red. (Remember `console.reset_colour()` afterwards!)
2. Make the game get faster as your score goes up. Hint: instead of `time.sleep(0.1)`, use a variable for the wait time and make it smaller each time you eat.
3. Add `console.beep()` when the snake eats. (If you hear nothing, check your volume.)
4. Sometimes put down special gold food (`$`) that's worth 5 points.

## ✅ Done when

- [ ] Food appears, and when the snake eats it, it grows and the score goes up
- [ ] `python -m pytest -k "step3 or step4 or step5 or step6 or step7"` passes

## 💾 Save your work

```
git add .
git commit -m "Step 7 done"
git push
```

Next: [Step 8: Game over](08-game-over.md) (bonus)
