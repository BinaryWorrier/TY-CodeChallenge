# Step 2: Rows and columns

**Goal:** write a character at any spot on the screen.

**You'll learn:** how the screen is a grid, `console.set_cursor_position`, putting variables inside strings.

## The screen is a grid

The console is a grid of **columns** (across) and **rows** (down). Counting starts at **0** in the top-left corner.

```
         column 0   1   2   3   4   5 ...
row 0           .   .   .   .   .   .
row 1           .   .   .   .   .   .
row 2           .   .   .   @   .   .      <- the @ is at column 3, row 2
row 3           .   .   .   .   .   .
```

⚠️ Rows count **down** from the top, not up like on a graph in maths class.

## 1. Move the cursor

The **cursor** is the spot where the next character will appear. You can move it anywhere:

```python
console.set_cursor_position(10, 5)   # column 10, row 5
console.write("@")
```

⚠️ **Column first, then row.** It's easy to mix these up.

## 2. Try it

Replace everything under the `import` and `from` lines in `main.py` with:

```python
console.clear()
console.hide_cursor()

# set_cursor_position(column, row) - column FIRST, then row.
console.set_cursor_position(10, 5)
console.write("@")

console.set_cursor_position(0, 0)
console.write("Top left")

width = console.window_width()
height = console.window_height()

console.set_cursor_position(width - 9, 0)
console.write("Top right")

console.set_cursor_position(0, height - 2)
console.write(f"The screen is {width} columns wide and {height} rows tall.")

# Wait for a key, so we can see what we drew before the program ends.
console.read_key()
console.show_cursor()
console.clear()
```

Run it. Press any key to finish.

Some new things:

- `console.clear()` wipes the screen.
- `console.hide_cursor()` hides the flashing cursor. `console.show_cursor()` brings it back.
- `console.write("...")` is like `print`, but it doesn't start a new line, and the text appears straight away.
- `console.window_width()` and `console.window_height()` tell you how big the window is.
- `f"... {width} ..."` puts a variable's value straight into a string. The `f` at the front stands for "format". It's easier than lots of `+` and `str()`.
- `console.read_key()` waits until you press a key.
- Why `width - 9`? "Top right" is 9 characters long, so it has to start 9 columns from the right-hand edge.

> The bottom row is `height - 1`. Writing in the very last spot on the screen can make everything scroll up, so stay off the bottom row for now.

## 🎯 Challenges

Try at least two:

1. Put an `X` in the top-left, top-right and bottom-left corners. Use `height - 2` for the bottom.
2. Write your name in the **middle** of the screen. Hint: the middle column is `width // 2`. To centre text, start at `(width - len(name)) // 2`.
   - `len(name)` is how many characters are in `name`.
   - `//` divides and throws away any remainder, so you always get a whole number. If you use `/`, you might get `40.0` or `40.5`, and there's no column 40.5! The error message will remind you.
3. Draw a face using `set_cursor_position` for each part. Remember from Step 1: type `\\` to get one `\`.
   ```
     o   o
       ^
     \___/
   ```
4. Make the window bigger or smaller and run it again. Do the numbers change?

## ✅ Done when

- [ ] You can put a character at any column and row you choose
- [ ] You know that `set_cursor_position` takes the **column first**

## 💾 Save your work

```
git add .
git commit -m "Step 2 done"
git push
```

Next: [Step 3: Loops and moving](03-loops-and-moving.md)
