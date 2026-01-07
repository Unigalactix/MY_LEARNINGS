# Branching and Merging - Comprehensive Notes 🌿

## Introduction to Branching

Branching is one of Git's most powerful features. It allows you to diverge from the main line of development and work independently without affecting the main codebase.

### Why Use Branches?

- **Feature Development**: Work on new features without affecting production code
- **Bug Fixes**: Create hotfix branches to fix issues quickly
- **Experimentation**: Try new ideas safely without risk
- **Parallel Development**: Multiple developers work on different features simultaneously
- **Code Organization**: Keep different types of work separate

### Branch Analogy
Think of branches like parallel universes in a story. You can create alternate timelines, make changes, and then merge the best outcomes back into the main timeline.

---

## Core Branching Concepts

### What is a Branch?

A branch is a lightweight movable pointer to a commit. The default branch in Git is usually called `main` (or `master` in older repositories).

```
main    →  [C1] → [C2] → [C3]
feature →              → [C4] → [C5]
```

### HEAD Pointer

`HEAD` is a special pointer that indicates which branch you're currently on. When you switch branches, `HEAD` moves to point to the new branch.

---

## Basic Branch Commands

### Creating Branches

**Create a new branch**:
```bash
git branch <branch-name>
```

Example:
```bash
git branch feature-login
```

**List all branches**:
```bash
git branch           # Local branches only
git branch -a        # All branches (local + remote)
git branch -r        # Remote branches only
```

**Create and switch to a branch** (shortcut):
```bash
git checkout -b <branch-name>
```

Modern alternative:
```bash
git switch -c <branch-name>
```

Example:
```bash
git checkout -b feature-authentication
# Creates and switches to feature-authentication branch
```

### Switching Branches

**Old method** (still widely used):
```bash
git checkout <branch-name>
```

**New method** (Git 2.23+):
```bash
git switch <branch-name>
```

Example:
```bash
git switch main
git switch feature-login
```

**Check current branch**:
```bash
git branch          # Current branch marked with *
git status          # Shows current branch at top
```

### Deleting Branches

**Delete a local branch** (safe - prevents deletion if unmerged):
```bash
git branch -d <branch-name>
```

**Force delete a branch** (deletes even if unmerged):
```bash
git branch -D <branch-name>
```

**Delete a remote branch**:
```bash
git push origin --delete <branch-name>
```

Examples:
```bash
git branch -d feature-login        # Delete after merging
git branch -D experimental-feature # Force delete
git push origin --delete old-feature # Delete from GitHub
```

---

## Branch Naming Conventions

### Common Prefixes

- `feature/` or `feat/` - New features
- `bugfix/` or `fix/` - Bug fixes
- `hotfix/` - Urgent production fixes
- `release/` - Release preparation
- `docs/` - Documentation updates
- `test/` - Test improvements
- `refactor/` - Code refactoring

### Examples of Good Branch Names

```bash
feature/user-authentication
feature/shopping-cart
bugfix/login-error
bugfix/navbar-alignment
hotfix/security-vulnerability
release/v2.0.0
docs/api-documentation
test/unit-tests-for-auth
refactor/database-connection
```

### Best Practices for Naming

- Use lowercase and hyphens (kebab-case)
- Be descriptive but concise
- Include issue/ticket number if applicable
- Avoid special characters except `/` and `-`

---

## Understanding Merging

Merging is the process of combining changes from one branch into another.

### Types of Merges

#### 1. Fast-Forward Merge

Occurs when there are no new commits on the target branch since the feature branch was created.

```
Before merge:
main    → [C1] → [C2]
feature →              → [C3] → [C4]

After fast-forward merge:
main    → [C1] → [C2] → [C3] → [C4]
```

Git simply moves the pointer forward.

**Command**:
```bash
git checkout main
git merge feature-branch
```

#### 2. Three-Way Merge (Merge Commit)

Occurs when both branches have new commits. Git creates a new merge commit with two parents.

```
Before merge:
main    → [C1] → [C2] → [C4]
feature →              → [C3] → [C5]

After three-way merge:
main    → [C1] → [C2] → [C4] ──→ [C6 MERGE]
feature →              → [C3] → [C5] ──┘
```

**Command**:
```bash
git checkout main
git merge feature-branch
# Git opens editor for merge commit message
```

---

## Merge Workflow

### Standard Merge Process

```bash
# 1. Switch to the branch you want to merge INTO
git checkout main

# 2. Make sure it's up to date
git pull origin main

# 3. Merge the feature branch
git merge feature-login

# 4. Push the merged changes
git push origin main
```

### Typical Feature Branch Workflow

```bash
# 1. Create and switch to feature branch
git checkout -b feature-user-profile

# 2. Make changes and commit
git add .
git commit -m "Add user profile page"

# 3. Switch back to main
git checkout main

# 4. Merge feature into main
git merge feature-user-profile

# 5. Delete feature branch (optional)
git branch -d feature-user-profile

# 6. Push to remote
git push origin main
```

---

## Handling Merge Conflicts

### What is a Merge Conflict?

A conflict occurs when Git can't automatically merge changes because:
- Same line modified in both branches
- File deleted in one branch but modified in another
- Complex overlapping changes

### Conflict Indicators

When a conflict occurs, Git marks the conflicting areas in files:

```
<<<<<<< HEAD
Code from your current branch
=======
Code from the branch being merged
>>>>>>> feature-branch
```

### Resolving Conflicts - Step by Step

**Step 1: Identify conflicts**
```bash
git status
# Shows "both modified:" for conflicting files
```

**Step 2: Open conflicting files**
Look for conflict markers: `<<<<<<<`, `=======`, `>>>>>>>`

**Step 3: Decide what to keep**
Options:
- Keep current branch changes only
- Keep incoming branch changes only
- Keep both (combine them)
- Write completely new code

**Step 4: Remove conflict markers**
Delete the `<<<<<<<`, `=======`, `>>>>>>>` lines

**Step 5: Stage resolved files**
```bash
git add <resolved-file>
```

**Step 6: Complete the merge**
```bash
git commit -m "Resolve merge conflict in <file>"
```

### Example Conflict Resolution

**Before resolution**:
```python
def greet(name):
<<<<<<< HEAD
    return f"Hello, {name}!"
=======
    return f"Hi there, {name}!"
>>>>>>> feature-greeting
```

**After resolution** (keeping both):
```python
def greet(name, style="hello"):
    if style == "hello":
        return f"Hello, {name}!"
    else:
        return f"Hi there, {name}!"
```

Then:
```bash
git add greet.py
git commit -m "Resolve greeting conflict by adding style parameter"
```

---

## Merge Strategies and Options

### Merge Options

**Fast-forward only** (fail if fast-forward not possible):
```bash
git merge --ff-only feature-branch
```

**No fast-forward** (always create merge commit):
```bash
git merge --no-ff feature-branch
```

**Abort a merge**:
```bash
git merge --abort
```

### When to Use Each

- `--ff-only`: When you want clean, linear history
- `--no-ff`: When you want to preserve feature branch context
- `--abort`: When conflicts are too complex or you made a mistake

---

## Viewing Branch Information

### See branch relationships
```bash
git log --oneline --graph --all
```

Example output:
```
* 7a3b2c1 (HEAD -> main) Merge feature-login
|\
| * 4f5e6d7 (feature-login) Add login validation
| * 2c3d4e5 Add login form
|/
* 1a2b3c4 Initial commit
```

### See differences between branches
```bash
git diff main..feature-branch        # All differences
git diff main...feature-branch       # Changes since branching point
```

### See commits in one branch but not another
```bash
git log main..feature-branch         # Commits in feature not in main
git log feature-branch..main         # Commits in main not in feature
```

---

## Branch Best Practices

### 1. Keep Branches Short-Lived
- Merge frequently to avoid large conflicts
- Delete branches after merging
- Don't let branches get too far behind main

### 2. Pull Before You Merge
```bash
git checkout main
git pull origin main
git merge feature-branch
```

### 3. Use Descriptive Branch Names
```bash
# Good
git branch feature/user-authentication
git branch bugfix/login-error-handling

# Bad
git branch temp
git branch test
git branch fix
```

### 4. Commit Before Switching Branches
```bash
# Make sure working directory is clean
git status
git commit -am "Save work in progress"
git checkout other-branch
```

### 5. Keep Main Branch Stable
- Never commit directly to main
- Always merge from feature branches
- Ensure tests pass before merging

---

## Common Branching Workflows

### 1. Feature Branch Workflow

```bash
# Start new feature
git checkout -b feature/new-dashboard
# Work and commit
git add .
git commit -m "Add dashboard layout"
# Merge when complete
git checkout main
git merge feature/new-dashboard
git branch -d feature/new-dashboard
```

### 2. Hotfix Workflow

```bash
# Create hotfix from main
git checkout -b hotfix/security-patch main
# Fix and commit
git commit -am "Fix security vulnerability"
# Merge to main
git checkout main
git merge hotfix/security-patch
# Also merge to develop if using Git Flow
git checkout develop
git merge hotfix/security-patch
# Delete branch
git branch -d hotfix/security-patch
```

### 3. Multiple Features in Parallel

```bash
# Developer A
git checkout -b feature/shopping-cart

# Developer B
git checkout -b feature/user-reviews

# Both work independently
# Merge separately when ready
```

---

## Stashing Changes (When Switching Branches)

Sometimes you need to switch branches but have uncommitted changes.

### Save work temporarily
```bash
git stash
git stash save "Work in progress on login feature"
```

### Switch branches and work
```bash
git checkout other-branch
# Do work on other branch
```

### Return and restore stashed changes
```bash
git checkout original-branch
git stash pop      # Apply and remove from stash
# or
git stash apply    # Apply but keep in stash
```

### List stashes
```bash
git stash list
```

### Apply specific stash
```bash
git stash apply stash@{1}
```

---

## Visualizing Branches

### Using Command Line
```bash
git log --graph --oneline --all --decorate
```

### Using Git GUI Tools
- **GitKraken**: Visual branch timeline
- **Sourcetree**: Tree view of branches
- **GitHub Desktop**: Simple branch visualization
- **VS Code Git Graph**: Extension for VS Code

---

## Common Issues and Solutions

### Issue 1: Switched Branch with Uncommitted Changes

**Problem**: Files modified, switched branches, changes follow you

**Solution**:
```bash
# Option 1: Commit changes
git add .
git commit -m "WIP: Save progress"

# Option 2: Stash changes
git stash
git checkout other-branch
```

### Issue 2: Merge Conflict Too Complex

**Problem**: Can't resolve conflicts easily

**Solution**:
```bash
# Abort merge and try again
git merge --abort

# Or use a merge tool
git mergetool
```

### Issue 3: Accidentally Merged Wrong Branch

**Problem**: Merged feature-branch into wrong branch

**Solution**:
```bash
# Undo merge (if not pushed)
git reset --hard HEAD~1

# Or revert merge commit (if already pushed)
git revert -m 1 <merge-commit-hash>
```

### Issue 4: Delete Branch by Accident

**Problem**: Deleted branch with unmerged commits

**Solution**:
```bash
# Find the commit
git reflog

# Recreate branch
git branch recovered-branch <commit-hash>
```

---

## Practical Exercises

### Exercise 1: Basic Branching
```bash
# 1. Create a repository
mkdir branch-practice && cd branch-practice
git init

# 2. Create initial commit
echo "# My Project" > README.md
git add README.md
git commit -m "Initial commit"

# 3. Create and switch to feature branch
git checkout -b feature-hello

# 4. Add feature
echo "print('Hello, World!')" > hello.py
git add hello.py
git commit -m "Add hello script"

# 5. Switch back to main
git checkout main

# 6. Merge feature
git merge feature-hello

# 7. Verify
git log --oneline
```

### Exercise 2: Practice Merge Conflicts
```bash
# 1. Create conflict scenario
git checkout -b branch-a
echo "Version A" > file.txt
git add file.txt
git commit -m "Add version A"

git checkout main
git checkout -b branch-b
echo "Version B" > file.txt
git add file.txt
git commit -m "Add version B"

# 2. Create conflict
git checkout main
git merge branch-a    # Merges cleanly
git merge branch-b    # Creates conflict!

# 3. Resolve conflict
# Edit file.txt, remove markers, choose version
git add file.txt
git commit -m "Resolve conflict"
```

---

## Key Takeaways

✅ **Branches are cheap** - Create them freely for features, experiments, and fixes

✅ **Merge often** - Keep branches up to date to minimize conflicts

✅ **Name branches descriptively** - Use prefixes and clear names

✅ **Keep main stable** - Never work directly on main/master

✅ **Delete merged branches** - Keep repository clean

✅ **Learn to resolve conflicts** - It's a normal part of collaboration

✅ **Use visualization tools** - They make branch management much easier

---

## Next Steps

After mastering branching and merging:
- Learn about **remote branches** and syncing with GitHub
- Explore **rebasing** as an alternative to merging
- Study **Git workflows** (Git Flow, GitHub Flow)
- Practice **collaborative development** with pull requests

---

**Happy Branching!** 🌿

*"Branching means you diverge from the main line of development and continue to work without messing with that main line." - Pro Git Book*
