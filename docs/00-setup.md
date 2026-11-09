# Step 0: Setup

**Goal:** get the project running on your computer, on your own branch.

## 1. Install the tools

You need three things. Your tutor may have done this already.

| Tool | What it's for | Where to get it |
|------|---------------|-----------------|
| .NET 10 SDK | Builds and runs C# programs | https://dotnet.microsoft.com/download |
| Git | Saves your work and shares it on GitHub | https://git-scm.com/downloads |
| VS Code + the **C# Dev Kit** extension | Where you write the code | https://code.visualstudio.com |

(Visual Studio works too, if you prefer it.)

Check they work. Open a terminal and type:

```
dotnet --version
git --version
```

Both should print a version number. The `dotnet` one should start with `10`.

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

In VS Code: **File > Open Folder** and pick the project folder (the one with `README.md` in it).

Open the terminal inside VS Code with **Terminal > New Terminal**. You'll type all the commands there.

## 6. Run the game

```
dotnet run --project src/SnakeGame
```

You should see:

```
Hello, Snake!
```

Not much of a game yet. That's what the next steps are for.

## 7. Run the tests

```
dotnet test --filter Step0
```

You should see something like:

```
Passed!  - Failed: 0, Passed: 1, Skipped: 0, Total: 1
```

That means testing works on your computer.

> Try `dotnet test` without the filter. You'll see lots of failures. Don't panic! Those are the tests for steps you haven't done yet. Each step will turn some of them green.

## ✅ Done when

- [ ] `dotnet run --project src/SnakeGame` prints `Hello, Snake!`
- [ ] `dotnet test --filter Step0` passes
- [ ] `git branch` shows you're on your own branch

Next: [Step 1: Hello, console](01-hello-console.md)
