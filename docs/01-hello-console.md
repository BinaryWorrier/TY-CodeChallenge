# Step 1: Hello, console

**Goal:** write text and colours to the screen.

**You'll learn:** `Console.WriteLine`, `Console.Write`, variables, colours.

## 1. Open Program.cs

Open `src/SnakeGame/Program.cs`. It looks like this:

```csharp
// Welcome to Snake!
// Start with the guide in docs/01-hello-console.md

// This line lets us use the game's building blocks (Position, Direction, Snake...).
using SnakeGame;

Console.WriteLine("Hello, Snake!");
```

- Lines starting with `//` are **comments**. The computer ignores them. They're notes for people.
- `Console.WriteLine("...")` writes text to the screen, then moves to a new line.
- Every instruction ends with a semicolon `;`.

Leave the `using SnakeGame;` line where it is. We'll need it from Step 3.

## 2. Write some more

Add these lines underneath:

```csharp
Console.WriteLine("This is a new line.");

Console.Write("Write ");
Console.Write("stays ");
Console.Write("on the same line.");
Console.WriteLine();
```

Run it:

```
dotnet run --project src/SnakeGame
```

What's the difference between `Write` and `WriteLine`?

## 3. Variables

A **variable** is a box with a name that holds a value. Add:

```csharp
string name = "Snakey";
Console.WriteLine("My snake is called " + name);

int length = 5;
Console.WriteLine("It is " + length + " parts long");
```

- `string` holds text. `int` holds a whole number.
- `+` joins text together.

## 4. Colours

```csharp
Console.ForegroundColor = ConsoleColor.Green;
Console.WriteLine("Sssssss!");
Console.ResetColor();
```

Type `ConsoleColor.` and your editor will pop up a list of all the colours you can use.

## 🎯 Challenges

Try at least two:

1. Print your own name in your favourite colour.
2. Change the **background** colour too, with `Console.BackgroundColor`.
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
- [ ] You know the difference between `Write` and `WriteLine`

## 💾 Save your work

```
git add .
git commit -m "Step 1 done"
git push
```

Next: [Step 2: Rows and columns](02-rows-and-columns.md)
