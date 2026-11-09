# Step 2: Rows and columns

**Goal:** write a character at any spot on the screen.

**You'll learn:** how the screen is a grid, `Console.SetCursorPosition`, putting variables inside strings.

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

```csharp
Console.SetCursorPosition(10, 5);   // column 10, row 5
Console.Write("@");
```

⚠️ **Column first, then row.** It's easy to mix these up.

## 2. Try it

Replace everything under `using SnakeGame;` in `Program.cs` with:

```csharp
Console.Clear();
Console.CursorVisible = false;

// SetCursorPosition(column, row) - column FIRST, then row.
Console.SetCursorPosition(10, 5);
Console.Write("@");

Console.SetCursorPosition(0, 0);
Console.Write("Top left");

int width = Console.WindowWidth;
int height = Console.WindowHeight;

Console.SetCursorPosition(width - 9, 0);
Console.Write("Top right");

Console.SetCursorPosition(0, height - 2);
Console.Write($"The screen is {width} columns wide and {height} rows tall.");

// Wait for a key, so we can see what we drew before the program ends.
Console.ReadKey(true);
Console.CursorVisible = true;
Console.Clear();
```

Run it. Press any key to finish.

Some new things:

- `Console.Clear()` wipes the screen.
- `Console.CursorVisible = false` hides the flashing cursor.
- `Console.WindowWidth` and `Console.WindowHeight` tell you how big the window is.
- `$"... {width} ..."` puts a variable's value straight into a string. That's easier than lots of `+`.
- Why `width - 9`? "Top right" is 9 characters long, so it has to start 9 columns from the right-hand edge.

> The bottom row is `height - 1`. Writing in the very last spot on the screen can make everything scroll up, so stay off the bottom row for now.

## 🎯 Challenges

Try at least two:

1. Put an `X` in the top-left, top-right and bottom-left corners. Use `height - 2` for the bottom.
2. Write your name in the **middle** of the screen. Hint: the middle column is `width / 2`. To centre text, start at `(width - name.Length) / 2`.
3. Draw a face using `SetCursorPosition` for each part. Remember from Step 1: type `\\` to get one `\`.
   ```
     o   o
       ^
     \___/
   ```
4. Make the window bigger or smaller and run it again. Do the numbers change?

## ✅ Done when

- [ ] You can put a character at any column and row you choose
- [ ] You know that `SetCursorPosition` takes the **column first**

## 💾 Save your work

```
git add .
git commit -m "Step 2 done"
git push
```

Next: [Step 3: Loops and moving](03-loops-and-moving.md)
