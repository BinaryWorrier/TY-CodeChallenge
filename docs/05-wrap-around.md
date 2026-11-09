# Step 5: Wrap around

**Goal:** go off the right of the screen and come back on the left, and the same for the other edges.

**You'll learn:** `if` with `<` and `>=`, classes, `self`, off-by-one mistakes.

## The board

Open `src/board.py`. A `Board` is a **class**: a recipe for making things that hold values and have their own functions. Each board has a `width` (number of columns) and a `height` (number of rows).

```python
def __init__(self, width, height):
    self.width = width
    self.height = height
```

`__init__` is the code that runs when a board is made, for example with `Board(20, 10)`. It saves the width and height inside the board, as `self.width` and `self.height`.

If the board is 20 wide, the columns are numbered **0 to 19**. So column 20 is already off the board!

```
column:  0  1  2  ...  17 18 19 | 20
         .  .  .  ...  .  .  .  |  @   <- off the board!
```

## Part A: wrap

Fill in `wrap`. It's given a position that might have gone off the board, and gives back a position that's on the board:

| If... | ...then |
|-------|---------|
| x is too big (off the right) | x becomes 0 |
| x is too small (off the left) | x becomes the last column |
| y is too big (off the bottom) | y becomes 0 |
| y is too small (off the top) | y becomes the last row |
| none of these | leave it alone |

The tests use a board 20 wide and 10 tall. Look in `tests/test_step5_wrap.py` to see exactly what they expect.

⚠️ Inside the class, the board's width is `self.width`, not just `width`. If you see `NameError: name 'width' is not defined`, you've forgotten the `self.`.

<details>
<summary>Hint 1</summary>

You can't change `position.x` directly, because positions can't be changed once they're made. Copy x and y into variables, fix them, then make a new position at the end:

```python
x = position.x
y = position.y

# fix x and y here

return Position(x, y)
```
</details>

<details>
<summary>Hint 2</summary>

```python
if x >= self.width:
    x = 0
```

Why `>=` and not `>`? What's the last column number on a board that is `self.width` wide?
</details>

Run the tests:

```
python -m pytest -k step5
```

If `test_off_the_right_edge_comes_back_on_the_left` fails but the others pass, you've probably made an **off-by-one** mistake. They're one of the most common bugs in programming, which is exactly why we test for them.

## Part B: use it in the game

In `main.py`, make a board the size of the window. Put this just after `console.hide_cursor()`:

```python
# The board is the whole window, except the bottom row (we'll use that for the score later).
board = Board(console.window_width(), console.window_height() - 1)
```

Then change the moving line in the loop from:

```python
    position = position.move(direction.dx, direction.dy)
```

to:

```python
    new_position = position.move(direction.dx, direction.dy)
    position = board.wrap(new_position)
```

Run it. Drive off every edge. No more crashes!

> Don't resize the window while the game is running. The board won't know it's changed size.

## 🎯 Challenges

1. Make the board smaller than the window, for example `Board(40, 15)`. Draw a border around it with `#` characters before the game loop starts.
2. Write `wrap` a different way, using the `%` (remainder) operator. `17 % 5` is 2, because 17 divided by 5 is 3 remainder 2. Here's a surprise: in Python, `-1 % 20` is `19`. Try it! Type `python` on its own in the terminal, then type `-1 % 20` and press Enter. (Type `exit()` to get out again.) Can you write `wrap` in one line? Your tests will tell you if it still works!

## ✅ Done when

- [ ] The `@` goes off each edge and comes back on the other side
- [ ] `python -m pytest -k "step3 or step4 or step5"` passes

## 💾 Save your work

```
git add .
git commit -m "Step 5 done"
git push
```

Next: [Step 6: The tail](06-the-tail.md)
