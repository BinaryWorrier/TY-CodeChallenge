# Step 1: Hello, console

**Goal:** write text and colours to the screen.

**You'll learn:** `print`, variables, joining text together, colours.

## 1. Open main.py

Open `src/main.py`. It looks like this:

```python
# Welcome to Snake!
# Start with the guide in docs/01-hello-console.md

# These lines let us use the game's building blocks (the screen, Position, Direction, Snake...).
# Leave them here at the top. We'll need them in later steps.
import time

import console
from board import Board
from controls import change_direction
from direction import RIGHT
from position import Position
from snake import Snake

print("Hello, Snake!")
```

- Lines starting with `#` are **comments**. The computer ignores them. They're notes for people.
- `print("...")` writes text to the screen, then moves to a new line.
- Each instruction goes on its own line. Python doesn't need a semicolon `;` at the end.
- Capital letters matter. `print` works, but `Print` doesn't.

Leave the lines that start with `import` and `from` where they are. They let `main.py` use the other files in the `src` folder.

## 2. Write some more

Add these lines underneath:

```python
print("This is a new line.")

print("Print ", end="")
print("stays ", end="")
print("on the same line.", end="")
print()
```

Run it:

```
python src/main.py
```

What does `end=""` do? What does `print()` do on its own, with nothing in the brackets?

## 3. Variables

A **variable** is a box with a name that holds a value. Add:

```python
name = "Snakey"
print("My snake is called " + name)

length = 5
print("It is " + str(length) + " parts long")
```

- `name` holds text. Python calls text a **string** (`str`).
- `length` holds a whole number. Python calls that an **int**.
- You don't have to tell Python which kind of value goes in a variable. It works it out.
- `+` joins text together.
- `str(length)` turns the number 5 into the text "5".

Try taking out the `str( )` so the line is `print("It is " + length + " parts long")`. Python stops with a `TypeError`. It won't join text and a number together unless you turn the number into text first. Put the `str( )` back.

## 4. Colours

```python
console.set_colour("green")
print("Sssssss!")
console.reset_colour()
```

`console` is a helper file in `src/console.py`. Plain Python doesn't have an easy way to do colours that works on every computer, so we've written one for you.

You can use these colours:

| | | | |
|---|---|---|---|
| `"black"` | `"red"` | `"green"` | `"yellow"` |
| `"blue"` | `"magenta"` | `"cyan"` | `"white"` |
| `"grey"` | `"bright_red"` | `"bright_green"` | `"bright_yellow"` |
| `"bright_blue"` | `"bright_magenta"` | `"bright_cyan"` | `"bright_white"` |

If you spell a colour wrong, the error message lists them all.

## 🎯 Challenges

Try at least two:

1. Print your own name in your favourite colour.
2. Change the **background** colour too, with `console.set_background_colour("blue")`.
3. Draw a snake out of characters over a few lines, for example:
   ```
       ____
      / . .\
      \  ---<
       \  /
   ____/ /
   ```
   Hint: to print a `\` inside a string you need to type `\\`.
4. Make a variable for your age. Print how old you'll be in 10 years.

## ✅ Done when

- [ ] Your program prints a few lines, including at least one in colour
- [ ] You know what `end=""` does

## 💾 Save your work

```
git add .
git commit -m "Step 1 done"
git push
```

Next: [Step 2: Rows and columns](02-rows-and-columns.md)
