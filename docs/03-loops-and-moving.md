# Step 3: Loops and moving

**Goal:** make a character move across the screen, then write the code that the first unit tests check.

**You'll learn:** `for` loops, indenting, `time.sleep`, how animation works, functions, your first unit test.

## Part A: a loop

A **loop** runs the same code again and again. Replace everything under the `import` and `from` lines in `main.py` with:

```python
for i in range(10):
    print(f"Lap {i}")
```

Read it as: *"for each number `i` in the range 0 up to 10, print the lap number."*

Two important things:

- The line that starts the loop ends with a colon `:`.
- The line inside the loop is **indented** (pushed in by 4 spaces, or one press of Tab in VS Code). Python uses indenting to know which lines are inside the loop. Everything indented under the `for` line runs each time round. The first line that isn't indented runs after the loop has finished.

Run it. Why does it stop at 9 and not 10?

## Part B: make something move

Animation is a trick. Each time round the loop:

1. **Rub out** the character (write a space over it).
2. **Change** its position.
3. **Draw** it in the new place.
4. **Wait** a moment, so our eyes can see it.

Replace everything under the `import` and `from` lines with:

```python
console.clear()
console.hide_cursor()

x = 5
y = 5

for i in range(10):
    # 1. rub out the old @
    console.set_cursor_position(x, y)
    console.write(" ")

    # 2. move one column to the right
    x = x + 1

    # 3. draw the @ in its new place
    console.set_cursor_position(x, y)
    console.write("@")

    # 4. wait 0.2 seconds (a fifth of a second)
    time.sleep(0.2)

console.show_cursor()
console.set_cursor_position(0, y + 2)
```

Run it. You should see the `@` slide to the right.

`time.sleep(0.2)` pauses the program. The number is in **seconds**, so `0.2` is a fifth of a second.

### Add a "delta"

**Delta** means "how much something changes". Let's use `dx` for the change in column and `dy` for the change in row. Add these under `y = 5`:

```python
dx = 1
dy = 0
```

and change step 2 inside the loop to:

```python
    # 2. move by the delta
    x = x + dx
    y = y + dy
```

Keep the 4 spaces at the start of those lines, so they stay inside the loop.

Now you can change the direction just by changing `dx` and `dy`.

### 🎯 Challenges

1. Make it move **down** instead. What do `dx` and `dy` need to be?
2. Make it move **diagonally**.
3. Make it move **up**. Careful: if it goes above row 0 the program crashes with an `OffTheScreenError`. Start lower down!
4. Make it go 30 steps and go faster.
5. Comment out the "rub out" lines (put `#` in front). What happens?

## Part C: your first unit test

A **unit test** is a small piece of code that checks that another piece of code gives the right answer. Instead of running the game and looking, the computer checks for you, in less than a second.

### Position

Moving by `dx` and `dy` is going to happen a lot in this game, so it's worth putting it somewhere it can be tested. Open `src/position.py`:

```python
@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def move(self, dx, dy):
        """Gives back a NEW position that is dx columns across and dy rows down from this one."""
        # TODO Step 3: replace the line below.
        # See docs/03-loops-and-moving.md
        raise NotImplementedError("Step 3: Position.move")
```

A `Position` holds an `x` (the column) and a `y` (the row). You make one with `Position(5, 3)`.

`move` is a **function** that belongs to a position. (A function that belongs to something is also called a **method**.) It should give back a **new** position that is `dx` columns across and `dy` rows down.

- `self` means "this position", the one we're moving. Inside `move`, `self.x` is this position's column and `self.y` is its row.
- The text in triple quotes `"""..."""` is a **docstring**: a comment that says what the function does.
- `raise NotImplementedError(...)` stops the program with an error that says "this hasn't been written yet". That's the line you're going to replace.
- `@dataclass(frozen=True)` writes some boring code for us. It lets us compare two positions with `==`, and stops a position being changed once it's made.

### Look at the tests first

Open `tests/test_step3_position.py`. Here's one test:

```python
def test_moving_right_adds_one_to_x():
    start = Position(5, 5)

    moved = start.move(1, 0)

    assert moved == Position(6, 5)
```

Every test has three parts:

1. **Set up**: make a position at (5, 5).
2. **Do the thing**: move it by (1, 0).
3. **Check**: `assert` checks that something is true. Here it checks that we got (6, 5). If not, the test **fails**.

Test names start with `test_`. That's how pytest finds them.

### Run the tests: red 🔴

```
python -m pytest -k step3
```

They all fail with `NotImplementedError: Step 3: Position.move`. That's expected, because you haven't written it yet.

### Make them pass: green 🟢

Replace the `raise ...` line in `move` so it gives back a new position.

<details>
<summary>Hint 1</summary>

You make a new position with `Position(something, something)`. To give it back, use `return`. Inside `move`, `self.x` and `self.y` are this position's column and row.
</details>

<details>
<summary>Hint 2</summary>

```python
return Position(self.x + ???, self.y + ???)
```
</details>

Run the tests again until you see:

```
======================= 8 passed, 48 deselected in 0.30s =======================
```

### Use Position in your program

Now tidy up `main.py` to use `Position`. A small helper called `draw` saves us typing `set_cursor_position` again and again. Replace everything under the `import` and `from` lines with:

```python
# A helper that draws one character at a position on the screen.
def draw(position, symbol):
    console.set_cursor_position(position.x, position.y)
    console.write(symbol)


console.clear()
console.hide_cursor()

position = Position(5, 5)
dx = 1
dy = 0

for i in range(10):
    draw(position, " ")                 # 1. rub out the old @
    position = position.move(dx, dy)    # 2. move by the delta
    draw(position, "@")                 # 3. draw the @ in its new place
    time.sleep(0.2)                     # 4. wait

console.show_cursor()
console.set_cursor_position(0, position.y + 2)
```

- `def` makes a new function called `draw`. It needs two things: a `position` and a `symbol`. Each time you write `draw(...)`, the indented lines inside it run.
- In Python, you have to make a function before you can use it. That's why `draw` goes at the top, just under the imports.

Run it. It should do exactly the same as before, but the code is shorter and the moving part is tested.

## ✅ Done when

- [ ] The `@` slides across the screen
- [ ] You can make it go in different directions by changing `dx` and `dy`
- [ ] `python -m pytest -k step3` passes

## 💾 Save your work

```
git add .
git commit -m "Step 3 done"
git push
```

Next: [Step 4: Game loop and keys](04-game-loop-and-keys.md)
