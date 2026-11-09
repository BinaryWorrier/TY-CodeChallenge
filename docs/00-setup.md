# Step 0: Setup

**Goal:** get the project running on your computer, on your own branch.

## 1. Install the tools

You need three things. Your tutor may have done this already.

| Tool | What it's for | Where to get it |
|------|---------------|-----------------|
| Python 3 | Runs Python programs | https://www.python.org/downloads |
| Git | Saves your work and shares it on GitHub | https://git-scm.com/downloads |
| VS Code + the **Python** extension (by Microsoft) | Where you write the code | https://code.visualstudio.com |

> **Installing Python yourself?** On the first screen of the installer, tick **Add python.exe to PATH** before you click Install.

Check they work. Open a terminal (press the Windows key, type `Terminal` and press Enter) and type:

```
python --version
git --version
```

Both should print a version number. The Python one should start with `Python 3`.

> If `python` says "Python was not found" or opens the Microsoft Store, try `py --version`. If that works, type `py` instead of `python` in every step. If neither works, ask your tutor.

## 2. Tell Git who you are

You only do this once per computer:

```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Use the email address from your GitHub account.

## 3. Get the code

Your tutor will give you the address of the repository.

```
git clone https://github.com/OWNER/REPO.git
cd REPO
```

## 4. Make your own branch

A **branch** is your own copy of the code. You can change anything on it without affecting anyone else. Pick a name, such as your first name in lowercase:

```
git switch -c yourname
git push -u origin yourname
```

The first line makes the branch and moves you onto it. The second puts it on GitHub.

Check you're on it:

```
git branch
```

Your branch has a `*` next to it.

## 5. Open the project

In VS Code: **File > Open Folder** and pick the project folder (the one with `README.md` in it). If VS Code asks whether you trust the authors, say yes. If it offers to install the Python extension, say yes to that too.

Open the terminal inside VS Code with **Terminal > New Terminal**. You'll type all the commands there.

## 6. Install pytest

**pytest** is the program that runs the unit tests. Install it with:

```
python -m pip install -r requirements.txt
```

`requirements.txt` is a list of the extra things this project needs. At the moment, that's just pytest.

You might see one or both of these messages. They're fine, so carry on:

- `Defaulting to user installation because normal site-packages is not writeable`. This just means pytest is installed for you, not for everyone who uses the computer.
- A `WARNING` that a folder ending in `Scripts` is not on PATH. We always run pytest with `python -m pytest`, which doesn't need it.

> If you get a red `ERROR` instead, for example because it can't connect to the internet, ask your tutor.

## 7. Run the game

```
python src/main.py
```

You should see:

```
Hello, Snake!
```

Not much of a game yet. That's what the next steps are for.

> Always run the game by typing the command in the terminal. Don't use IDLE, and don't double-click `main.py`: the game needs a real terminal window to draw on and to read the keyboard.

## 8. Run the tests

```
python -m pytest -k step0
```

`-k step0` means "only run the tests with `step0` in their name". You should see something like:

```
tests/test_step0_setup.py::test_tests_are_working PASSED                 [100%]

======================= 1 passed, 55 deselected in 0.44s =======================
```

That means testing works on your computer. "Deselected" means the tests that `-k` skipped.

> Try `python -m pytest` without `-k step0`. You'll see lots of red `FAILED`. Don't panic! Those are the tests for steps you haven't done yet. Each step will turn some of them green.

## ✅ Done when

- [ ] `python src/main.py` prints `Hello, Snake!`
- [ ] `python -m pytest -k step0` passes
- [ ] `git branch` shows you're on your own branch

Next: [Step 1: Hello, console](01-hello-console.md)
