# Snake

Build a classic text-based Snake game in C#, one small step at a time.

```
                                    *

         o o o o o o @

Score: 3    Press Esc to quit
```

You start by printing "Hello" and finish with a snake that moves round the screen, eats food, grows and crashes into itself. Each step is small enough to finish in one go. From Step 3 onwards, **unit tests** tell you when your code is right.

## The steps

| Step | What you build | Tests? |
|------|----------------|--------|
| [0. Setup](docs/00-setup.md) | Get the project running on your computer and make your own branch | `Step0` |
| [1. Hello, console](docs/01-hello-console.md) | Write text and colours to the screen | - |
| [2. Rows and columns](docs/02-rows-and-columns.md) | Write a character at any spot on the screen | - |
| [3. Loops and moving](docs/03-loops-and-moving.md) | Move a character across the screen with a loop. Your first unit test! | `Step3` |
| [4. Game loop and keys](docs/04-game-loop-and-keys.md) | A loop that runs forever, with the arrow keys steering | `Step4` |
| [5. Wrap around](docs/05-wrap-around.md) | Go off one side of the screen and come back on the other | `Step5` |
| [6. The tail](docs/06-the-tail.md) | Turn the single character into a snake with a tail | `Step6` |
| [7. Food and growing](docs/07-food-and-growing.md) (bonus) | Eat food, grow longer, keep score | `Step7` |
| [8. Game over](docs/08-game-over.md) (bonus) | Crash into yourself and it's game over | `Step8` |

Start at [Step 0](docs/00-setup.md).

## Running the game and the tests

From the top folder of the project (the one with this README in it):

```
dotnet run --project src/SnakeGame
dotnet test --filter Step3
```

The second command runs only the Step 3 tests. Change the number for other steps.

> **Seeing lots of red?** That's normal. The tests for every step are there from the start, so the ones for steps you haven't done yet will fail. Use `--filter` to run the step you're working on.

## How the project is laid out

```
Snake/
├── README.md               <- you are here
├── docs/                   <- the step-by-step guide
├── src/SnakeGame/          <- the game
│   ├── Program.cs          <- the main program: drawing, keyboard, the game loop
│   ├── Position.cs         <- a spot on the screen (column, row)
│   ├── Direction.cs        <- which way we're going (up, down, left, right)
│   ├── Controls.cs         <- turns key presses into directions
│   ├── Board.cs            <- the playing area and wrapping round the edges
│   └── Snake.cs            <- the snake: its body, moving, growing
└── tests/SnakeGame.Tests/  <- the unit tests, one file per step
```

Look for `TODO Step N` comments in the code. Those are the parts you write.

## Saving your work

You each work on your own **branch**, so you can't break each other's code. At the end of every step:

```
git add .
git commit -m "Step 3 done"
git push
```

---

## Notes for the tutor

- **Branches**
  - `main` is the starter code. Each student makes a branch from `main` (Step 0 shows them how).
  - `solution` is the reference answer, with one commit per step.
- **The solution branch.** You decide whether to push it to GitHub. If the students can see it, they can peek. To push only the starter code, use `git push -u origin main`.
- **Answer for one step:** run `git log solution --oneline`, then `git show <commit>` for that step's commit.
- **Pushing.** Add both students as collaborators on the GitHub repo so they can push their branches. You might also protect `main` so nobody pushes to it by accident.
- **Checking progress:**

  ```
  git fetch
  git log origin/<student-branch> --oneline
  git switch <student-branch>
  dotnet test
  ```
- **The tests are built so each step can be done on its own:**
  - Steps 1 and 2 are console-only and have no tests.
  - Step 3 introduces testing with the simplest possible method.
  - Step 8 changes `Controls.ChangeDirection` from Step 4. The Step 4 tests never ask for a U-turn, so they still pass, and that's a good moment to talk about tests as a safety net when you change code.
- **Use a real terminal.** The game reads the keyboard with `Console.KeyAvailable`, which needs a real terminal window (the VS Code terminal or Windows Terminal). An editor's debug output panel won't work.
