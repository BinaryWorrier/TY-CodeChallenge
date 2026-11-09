# Step 8: Game over (bonus)

**Goal:** if the snake crashes into itself, it's game over. Also stop the snake turning straight back on itself.

**You'll learn:** changing code safely with tests, looping through a list by number.

## Part A: no U-turns

At the moment, if the snake is going right and you press left, it turns straight back into its own body. Real Snake doesn't let you do that.

### opposite

Open `src/direction.py` and fill in `opposite`. It should give back the direction that points the other way. The opposite of `Direction(1, 0)` is `Direction(-1, 0)`.

<details>
<summary>Hint</summary>

Flip the sign of both numbers. `-self.dx` is the opposite of `self.dx`.
</details>

### Change change_direction

Now open `src/controls.py`. You wrote `change_direction` in Step 4. Change it so that if the new direction is the opposite of `current`, it keeps going the `current` way instead.

<details>
<summary>Hint</summary>

If your Step 4 code `return`s as soon as it finds the key, you'll need to change it a bit. Put the new direction in a variable first, then check it at the end:

```python
wanted = current

if key == "up" or key == "w":
    wanted = UP
# ...and the other keys...

if wanted == current.opposite():
    return ???

return wanted
```
</details>

### ⭐ Tests are a safety net

You've just changed code you wrote in Step 4. Did you break it? You don't have to guess. Run **both** sets of tests:

```
python -m pytest -k "step4 or step8"
```

If the Step 4 tests still pass, you know your change didn't break anything. This is one of the best reasons to write tests.

## Part B: crashing into yourself

Open `src/snake.py` and fill in `hit_itself`. It should give back `True` if the head is in the same place as any **other** part of the body, and `False` if it isn't.

The head is `self.body[0]`, so check `self.body[1]`, `self.body[2]` and so on, up to the end of the list.

<details>
<summary>Hint 1</summary>

A `for` loop that starts at 1 instead of 0. `range(1, len(self.body))` counts from 1 up to (but not including) the length of the snake:

```python
for i in range(1, len(self.body)):
    ...  # is self.body[i] in the same place as self.head?
```

Why start at 1 and not 0?
</details>

<details>
<summary>Hint 2</summary>

As soon as you find a match, `return True`. If the loop finishes without finding one, `return False`. Be careful with the indenting: the `return False` goes **after** the loop, not inside it.
</details>

```
python -m pytest -k step8
```

Have a look at the test called `test_chasing_your_own_tail_is_allowed`. Why isn't that a crash?

## Part C: game over in the game

In `main.py`, inside the loop, after the food check:

```python
    # Did we crash into ourselves?
    if snake.hit_itself():
        playing = False
```

And **after** the loop, replace the last two lines (`console.show_cursor()` and `console.clear()`) with these. They're not indented, because they run after the loop has finished:

```python
# Game over!
message = f"GAME OVER - you scored {score}"
console.set_cursor_position((board.width - len(message)) // 2, board.height // 2)
console.write(message)

# Throw away any keys still waiting, then wait for a new key press.
while console.key_available():
    console.read_key()
console.read_key()

console.show_cursor()
console.clear()
```

Run it and crash on purpose!

## Check everything

You've finished, so now all the tests should pass:

```
python -m pytest
```

Look for `passed` in green at the bottom, and no `failed`.

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
- **High score:** save the best score to a file and read it back next time. Look up Python's `open` function.
- **Pause:** press P to pause and unpause.
- **Obstacles:** put some `#` blocks on the board that you mustn't hit.
- **One-liner:** write `hit_itself` in one line, using `in` and `self.body[1:]` (that means "the list, without the first one").
- **Two players:** one snake on the arrow keys, one on W A S D. You'll need to split `change_direction` into two. Whoever crashes first loses. You are two people, after all!
