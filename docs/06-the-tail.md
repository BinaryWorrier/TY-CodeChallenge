# Step 6: The tail

**Goal:** turn the `@` into a snake with a tail that follows it around.

**You'll learn:** lists, looping through a list with `for`, a neat trick for moving a snake.

## How the snake is stored

Open `src/snake.py`. The snake's body is a **list** of positions:

```python
self.body = [start]
```

A list is written with square brackets `[ ]`. You get things out of a list by their number, starting at 0. `self.body[0]` is the **head**. The last one in the list is the **tail**. (In Python, `self.body[-1]` means "the last one".)

```
    o  o  o  @
    ^        ^
   tail     head

   body = [ (8,5), (7,5), (6,5), (5,5) ]
            head                 tail
```

`snake.py` already has `head`, `tail` and `length` written for you, so you can write `self.head` instead of `self.body[0]`.

## The trick

Moving every part of the snake one by one would be a lot of work. Here's a much easier way:

```
Before:          o  o  o  @           body = [ (8,5), (7,5), (6,5), (5,5) ]

1. Add a new head at the FRONT:
                 o  o  o  o  @        body = [ (9,5), (8,5), (7,5), (6,5), (5,5) ]

2. Remove the tail from the BACK:
                    o  o  o  @        body = [ (9,5), (8,5), (7,5), (6,5) ]
```

It looks like the whole snake moved, but we only changed the two ends!

## Growing at the start

A new snake starts as just a head. It grows to its full length over its first few moves. The `__init__` code (the code that runs when a snake is made) sets this up for you. Without its comments, it looks like this:

```python
def __init__(self, start, start_length):
    self.body = [start]
    self._grow_by = start_length - 1
```

`self._grow_by` counts how many more moves the snake should grow for. While `self._grow_by` is more than 0, **don't** remove the tail. Just take one off `self._grow_by` instead.

The `_` at the start of `_grow_by` means "this belongs to the snake". Code outside the `Snake` class shouldn't touch it.

## Part A: write move

Fill in `move` in `snake.py`. It needs to:

1. Work out where the new head goes. Move the current head (`self.head`) in the `direction`, then wrap it on the `board`.
2. Put the new head at the **front** of `self.body`.
3. If `self._grow_by` is more than 0, take 1 off it. Otherwise, remove the tail from the **back** of `self.body`.

Useful bits of Python:

| Code | What it does |
|------|--------------|
| `self.body.insert(0, something)` | puts something at the front of the list |
| `self.body.pop()` | removes the last thing in the list |
| `len(self.body)` | how many things are in the list |

<details>
<summary>Hint 1</summary>

For step 1 you need two things you've already built: `move` from `Position` (Step 3) and `wrap` from `Board` (Step 5). It's the same as the two lines you wrote in `main.py` in Step 5.
</details>

<details>
<summary>Hint 2</summary>

```python
new_head = board.wrap(self.head.move(direction.dx, direction.dy))
self.body.insert(0, new_head)

if self._grow_by > 0:
    ...  # what goes here?
else:
    ...  # and here?
```

Replace each `...` with your own code.
</details>

Run the tests:

```
python -m pytest -k step6
```

## Part B: draw the snake

In `main.py`, the snake replaces `position`. Replace everything under the `import` and `from` lines with:

```python
# A helper that draws one character at a position on the screen.
def draw(position, symbol):
    console.set_cursor_position(position.x, position.y)
    console.write(symbol)


console.clear()
console.hide_cursor()

board = Board(console.window_width(), console.window_height() - 1)
snake = Snake(Position(5, 5), start_length=8)
direction = RIGHT
playing = True

while playing:
    # 1. Has a key been pressed?
    if console.key_available():
        key = console.read_key()

        if key == "escape":
            playing = False

        direction = change_direction(key, direction)

    # 2. Move the snake, but remember where its tail was first
    old_tail = snake.tail
    snake.move(direction, board)

    # 3. Rub out the old tail, then draw the whole snake
    draw(old_tail, " ")
    for part in snake.body:
        draw(part, "o")
    draw(snake.head, "@")

    # 4. Wait a moment before the next tick
    time.sleep(0.1)

console.show_cursor()
console.clear()
```

`for part in snake.body:` is the same kind of `for` loop as in Step 3. There, `range(10)` gave us the numbers 0 to 9 one at a time. Here, `snake.body` gives us each position in the snake's body, one at a time, and we draw it.

`start_length=8` gives the value a name, so it's clear what the 8 is for.

Why do we only rub out the **old tail**? Every other part of the snake is still part of the snake, so it gets drawn again anyway.

Run it. You have a snake! 🐍

## 🎯 Challenges

1. Make the snake start longer.
2. Draw the body in green and the head in yellow. (Remember `console.reset_colour()` afterwards!)
3. Try steering the snake straight back on itself. What happens? (You'll fix this in Step 8.)

## ✅ Done when

- [ ] The snake moves around with a tail following it
- [ ] The snake wraps around the edges, tail and all
- [ ] `python -m pytest -k "step3 or step4 or step5 or step6"` passes

## 💾 Save your work

```
git add .
git commit -m "Step 6 done"
git push
```

**You've built the core of Snake!** If you want to keep going, try the bonus steps.

Next: [Step 7: Food and growing](07-food-and-growing.md) (bonus)
