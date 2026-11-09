# Step 4: Game loop and keys

**Goal:** a loop that keeps running until you press Esc, with the arrow keys steering the `@`.

**You'll learn:** `while` loops, `True` and `False`, `if`, reading the keyboard without stopping the game.

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

Our snake can go four ways. Open `src/direction.py` and look at the bottom:

```python
UP = Direction(0, 0)
DOWN = Direction(0, 0)
LEFT = Direction(0, 0)
RIGHT = Direction(0, 0)
```

A `Direction` is just a `dx` and a `dy`, like in Step 3. Right now they're all `(0, 0)`, which means "don't move". Put in the right numbers.

Names in CAPITALS are **constants**: values that never change while the program runs.

⚠️ Remember from Step 2: rows count **down** from the top. Which way is "up"?

Check with:

```
python -m pytest -k step4
```

The first four tests (`test_up_goes_towards...`, `test_down_goes_towards...` and so on) should now pass. The others still fail. That's Part B.

## Part B: from keys to directions

Open `src/controls.py`. `change_direction` is given the key that was pressed and the direction we're going now. It gives back the direction we should go next.

The rules are:

| Key pressed | New direction |
|-------------|---------------|
| ↑ or W | `UP` |
| ↓ or S | `DOWN` |
| ← or A | `LEFT` |
| → or D | `RIGHT` |
| anything else | keep going the same way |

The key is a string with the key's name in it: `"up"`, `"down"`, `"left"` and `"right"` for the arrow keys, and `"w"`, `"a"`, `"s"`, `"d"` for the letters (always lowercase).

<details>
<summary>Hint 1</summary>

Use `if` to check which key it was. `or` means "or":

```python
if key == "up" or key == "w":
    return UP
```

Notice the **two** equals signs. One `=` puts a value into a variable. Two `==` asks a question: "are these the same?"
</details>

<details>
<summary>Hint 2</summary>

After checking all four directions, what should happen if none of them matched? Look at the `current` parameter.
</details>

Run the tests until they're all green:

```
python -m pytest -k step4
```

## Part C: the game loop

Replace everything under the `import` and `from` lines in `main.py` with:

```python
# A helper that draws one character at a position on the screen.
def draw(position, symbol):
    console.set_cursor_position(position.x, position.y)
    console.write(symbol)


console.clear()
console.hide_cursor()

position = Position(5, 5)
direction = RIGHT
playing = True

while playing:
    # 1. Has a key been pressed? key_available() doesn't wait - it just checks.
    if console.key_available():
        key = console.read_key()

        if key == "escape":
            playing = False

        direction = change_direction(key, direction)

    # 2. and 3. Rub out, move, draw
    draw(position, " ")
    position = position.move(direction.dx, direction.dy)
    draw(position, "@")

    # 4. Wait a moment before the next tick
    time.sleep(0.1)

console.show_cursor()
console.clear()
```

Some new things:

- `True` and `False` are values too. Like `print`, they need the capital letter.
- `while playing:` keeps looping as long as `playing` is `True`.
- `console.key_available()` is `True` if a key is waiting to be read. We check this first so the game doesn't **stop and wait** for a key, because the `@` has to keep moving.
- `console.read_key()` reads the key and gives back its name, such as `"up"`, `"w"` or `"escape"`. The key isn't printed on the screen.
- Look at the indenting. The lines under `if console.key_available():` are pushed in further, because they're inside the `if` as well as inside the loop.

Run it and steer with the arrow keys. Press **Esc** to quit.

### 💥 What happens at the edge?

Drive the `@` off the edge of the screen. The program crashes with an `OffTheScreenError`. That's because you can't put the cursor somewhere that isn't on the screen.

You'll fix that in the next step!

## 🎯 Challenges

1. Change `time.sleep(0.1)` to make the game faster or slower.
2. Use a different character instead of `@`.
3. Comment out the line that rubs out the old `@`. Now you've got a drawing program!
4. Make the space bar stop the `@` (hint: the space bar's name is `"space"`, and `Direction(0, 0)` doesn't move). You'll need to add a test for it too. Copy one of the tests in `tests/test_step4_direction.py` and change it.

## ✅ Done when

- [ ] You can steer the `@` with the arrow keys **and** W, A, S, D
- [ ] Esc quits the game
- [ ] `python -m pytest -k "step3 or step4"` passes

## 💾 Save your work

```
git add .
git commit -m "Step 4 done"
git push
```

Next: [Step 5: Wrap around](05-wrap-around.md)
