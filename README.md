# Snake

Build a classic text-based Snake game in Python, one small step at a time.

```
                                    *

         o o o o o o @

Score: 3    Press Esc to quit
```

You start by printing "Hello" and finish with a snake that moves round the screen, eats food, grows and crashes into itself. Each step is small enough to finish in one go. From Step 3 onwards, **unit tests** tell you when your code is right.

## The steps

| Step | What you build | Tests? |
|------|----------------|--------|
| [0. Setup](docs/00-setup.md) | Get the project running on your computer and make your own branch | `step0` |
| [1. Hello, console](docs/01-hello-console.md) | Write text and colours to the screen | - |
| [2. Rows and columns](docs/02-rows-and-columns.md) | Write a character at any spot on the screen | - |
| [3. Loops and moving](docs/03-loops-and-moving.md) | Move a character across the screen with a loop. Your first unit test! | `step3` |
| [4. Game loop and keys](docs/04-game-loop-and-keys.md) | A loop that runs forever, with the arrow keys steering | `step4` |
| [5. Wrap around](docs/05-wrap-around.md) | Go off one side of the screen and come back on the other | `step5` |
| [6. The tail](docs/06-the-tail.md) | Turn the single character into a snake with a tail | `step6` |
| [7. Food and growing](docs/07-food-and-growing.md) (bonus) | Eat food, grow longer, keep score | `step7` |
| [8. Game over](docs/08-game-over.md) (bonus) | Crash into yourself and it's game over | `step8` |

Start at [Step 0](docs/00-setup.md).

## Running the game and the tests

From the top folder of the project (the one with this README in it):

```
python src/main.py
python -m pytest -k step3
```

The second command runs only the Step 3 tests. Change the number for other steps. To run more than one step, use `or`:

```
python -m pytest -k "step3 or step4"
```

> If `python` doesn't work, try `py` instead.

> **Seeing lots of red?** That's normal. The tests for every step are there from the start, so the ones for steps you haven't done yet will fail. Use `-k` to run the step you're working on.

## How the project is laid out

```
Snake/
├── README.md               <- you are here
├── requirements.txt        <- extra things Python needs (just pytest)
├── pytest.ini              <- settings for the tests
├── docs/                   <- the step-by-step guide
├── src/                    <- the game
│   ├── main.py             <- the main program: drawing, keyboard, the game loop
│   ├── console.py          <- helpers for the screen and keyboard (you don't need to change this)
│   ├── position.py         <- a spot on the screen (column, row)
│   ├── direction.py        <- which way we're going (up, down, left, right)
│   ├── controls.py         <- turns key presses into directions
│   ├── board.py            <- the playing area and wrapping round the edges
│   └── snake.py            <- the snake: its body, moving, growing
└── tests/                  <- the unit tests, one file per step
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
  python -m pytest
  ```
- **The tests are built so each step can be done on its own:**
  - Steps 1 and 2 are console-only and have no tests.
  - Step 3 introduces testing with the simplest possible function.
  - Step 8 changes `change_direction` from Step 4. The Step 4 tests never ask for a U-turn, so they still pass, and that's a good moment to talk about tests as a safety net when you change code.
- **What `console.py` is for.** Python has no simple built-in way to move the cursor or read a key without waiting for Enter. `src/console.py` fills that gap, using Python's built-in `msvcrt` module on Windows plus ANSI escape codes for the drawing. (It also works on Mac and Linux, using `termios`.) It works like C#'s `Console` class, and the students only ever call it. It also does these things on purpose:
  - It raises `OffTheScreenError` if the cursor goes off the screen, so the "drive off the edge and it crashes" moment in Step 4 still happens. (A terminal would otherwise just stop the cursor at the edge.)
  - It raises a clear error if a column or row isn't a whole number. That catches the `/` vs `//` mistake.
  - If the game crashes, it puts the cursor and colours back and prints the error below the game, so the message is readable.
- **Use a real terminal.** The game reads the keyboard one key at a time, which needs a real terminal window: the VS Code terminal, or Windows Terminal (PowerShell or Command Prompt both work). **IDLE won't work**, and neither will double-clicking `main.py`. `console.py` stops with a message if it's run from IDLE.
- **No VS Code?** Any editor will do for writing the code, even IDLE. Just run the game from a terminal window: open Windows Terminal, `cd` to the project folder, and type `python src/main.py`.
- **Installing pytest.** `python -m pip install -r requirements.txt` doesn't need admin rights. If Python was installed for all users, pip installs pytest for the current user instead, and says so. It does need to reach pypi.org, so a school network that blocks it will stop the install. Step 0 tells the students to ignore the harmless "not on PATH" warning, because every command uses `python -m pytest`.
- **If `python` opens the Microsoft Store.** Windows has a shortcut called `python` that points to the Store when Python isn't on the PATH. Either use `py` instead (Step 0 suggests this), or turn off the `python.exe` and `python3.exe` shortcuts in **Settings > Apps > Advanced app settings > App execution aliases**.
- **VS Code.** `.vscode/settings.json` points VS Code at the `src` folder, so the imports in the tests don't get squiggly lines, and switches on the **Testing** panel (the flask icon), where the students can run tests by clicking.
