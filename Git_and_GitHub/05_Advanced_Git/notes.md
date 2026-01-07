# Advanced Git - Comprehensive Notes 🚀

## Introduction to Advanced Git

Once you're comfortable with basic Git operations, advanced techniques help you manage complex scenarios, maintain clean history, and work more efficiently.

### What You'll Learn

- **Rebase**: Alternative to merging for linear history
- **Cherry-pick**: Apply specific commits to other branches
- **Stash**: Temporarily save work without committing
- **Reset**: Undo commits and changes
- **Revert**: Safely undo commits in shared branches
- **Reflog**: Recover "lost" commits
- **Tags**: Mark important points in history
- **Interactive Rebase**: Clean up commit history

---

## Git Rebase

### What is Rebase?

Rebase rewrites commit history by moving commits to a new base. It creates a linear history instead of merge commits.

### Rebase vs Merge

**Merge**:
```
main    → [C1] → [C2] → [C4] ──→ [C6 merge]
feature →              → [C3] → [C5] ──┘
```
- Creates merge commit
- Preserves exact history
- Shows when branches merged

**Rebase**:
```
main    → [C1] → [C2] → [C4] → [C3'] → [C5']
```
- Linear history
- No merge commit
- Cleaner log

### Basic Rebase

```bash
# Update feature branch with latest main
git checkout feature-branch
git rebase main

# Or in one command
git rebase main feature-branch
```

**What happens**:
1. Git finds common ancestor
2. Saves your commits temporarily
3. Resets branch to target
4. Replays your commits one by one
5. Creates new commit hashes

### Resolving Rebase Conflicts

```bash
# During rebase, conflict occurs
git status  # Shows conflicting files

# Fix conflicts in files
# Remove <<<<<<<, =======, >>>>>>> markers

# Stage resolved files
git add resolved-file.txt

# Continue rebase
git rebase --continue

# Or skip this commit
git rebase --skip

# Or abort entire rebase
git rebase --abort
```

### Interactive Rebase

**Clean up your commit history**:

```bash
# Rebase last 3 commits
git rebase -i HEAD~3
```

**Editor opens with**:
```
pick a1b2c3d Add feature A
pick d4e5f6g Fix typo
pick g7h8i9j Add tests

# Commands:
# p, pick = use commit
# r, reword = use commit but edit message
# e, edit = use commit but stop for amending
# s, squash = meld into previous commit
# f, fixup = like squash but discard message
# d, drop = remove commit
```

**Common operations**:

**Squash commits**:
```
pick a1b2c3d Add feature A
squash d4e5f6g Fix typo
squash g7h8i9j Add tests
# Combines all three into one commit
```

**Reword commit message**:
```
reword a1b2c3d Add feature A
pick d4e5f6g Fix typo
# Opens editor to change first commit message
```

**Drop commits**:
```
pick a1b2c3d Add feature A
drop d4e5f6g Fix typo
pick g7h8i9j Add tests
# Removes the middle commit
```

### Golden Rule of Rebase

**❌ NEVER rebase public/shared branches!**

```bash
# ❌ DON'T DO THIS
git checkout main
git rebase feature  # Other people use main!

# ✅ DO THIS instead
git checkout feature
git rebase main  # Only affects your feature branch
```

**Why?**: Rebase changes commit hashes. If others have those commits, they'll have conflicts.

**Safe to rebase**:
- Your local feature branches
- Branches no one else uses
- Before pushing to remote

**Not safe to rebase**:
- main/master branch
- Shared team branches
- Already pushed commits others use

---

## Git Cherry-Pick

### What is Cherry-Pick?

Apply a specific commit from one branch to another without merging the entire branch.

### Basic Cherry-Pick

```bash
# On target branch
git checkout main

# Apply specific commit
git cherry-pick a1b2c3d

# Cherry-pick multiple commits
git cherry-pick a1b2c3d d4e5f6g

# Cherry-pick range of commits
git cherry-pick a1b2c3d..g7h8i9j
```

### Cherry-Pick Use Cases

**Scenario 1: Bug fix in wrong branch**
```bash
# Oops, committed to feature-A but needed in main
git checkout main
git cherry-pick bug-fix-commit
```

**Scenario 2: Backport fix to older version**
```bash
# Fix in main, need in v1.0 branch
git checkout v1.0-branch
git cherry-pick security-fix-commit
```

**Scenario 3: Selective changes**
```bash
# Want only one commit from feature branch
git cherry-pick specific-commit
# Don't want to merge entire branch
```

### Resolving Cherry-Pick Conflicts

```bash
# Conflict during cherry-pick
git status

# Fix conflicts
# Edit conflicting files

# Continue
git add resolved-file
git cherry-pick --continue

# Or abort
git cherry-pick --abort
```

---

## Git Stash

### What is Stash?

Temporarily save uncommitted changes without committing. Like a clipboard for your work.

### Basic Stash Commands

```bash
# Save current changes
git stash

# Stash with message
git stash save "Work in progress on login feature"

# List all stashes
git stash list

# Show stash contents
git stash show
git stash show -p  # Show full diff

# Apply most recent stash (keeps in stash)
git stash apply

# Apply and remove most recent stash
git stash pop

# Apply specific stash
git stash apply stash@{2}

# Drop specific stash
git stash drop stash@{1}

# Clear all stashes
git stash clear
```

### Stash Use Cases

**Scenario 1: Need to switch branches quickly**
```bash
# Working on feature-A
git add .  # Or don't add, stash works either way

# Need to fix urgent bug
git stash save "WIP: feature A partially done"
git checkout main
git checkout -b hotfix-bug
# Fix bug, commit, push

# Return to feature-A
git checkout feature-A
git stash pop
# Continue working
```

**Scenario 2: Experiments**
```bash
# Try something experimental
# Doesn't work out

git stash  # Save the attempt
# Or just: git checkout .  # Discard if you don't want to save
```

**Scenario 3: Conflict with incoming changes**
```bash
# Have uncommitted changes
git stash
git pull origin main  # Pull updates
git stash pop  # Reapply your changes
# Resolve any conflicts
```

### Advanced Stash

```bash
# Stash only unstaged changes
git stash --keep-index

# Stash untracked files too
git stash -u

# Stash everything including ignored files
git stash -a

# Create branch from stash
git stash branch feature-from-stash stash@{0}
```

---

## Git Reset

### What is Reset?

Move the branch pointer to a different commit. Can modify working directory and staging area.

### Reset Modes

**Three modes**: `--soft`, `--mixed`, `--hard`

**Visual representation**:
```
--soft:  Move HEAD, keep staged & working changes
--mixed: Move HEAD, unstage changes, keep working changes (default)
--hard:  Move HEAD, discard all changes ⚠️
```

### Reset Examples

**Undo last commit (keep changes)**:
```bash
git reset --soft HEAD~1
# Commit undone, changes still staged
```

**Unstage files**:
```bash
git reset HEAD file.txt
# Or (default mixed mode)
git reset file.txt
```

**Discard all changes** ⚠️:
```bash
git reset --hard HEAD
# Working directory reset to last commit
# ALL UNCOMMITTED CHANGES LOST!
```

**Go back 3 commits**:
```bash
git reset --hard HEAD~3
# Last 3 commits gone, changes lost ⚠️
```

**Reset to specific commit**:
```bash
git reset --hard a1b2c3d
# Branch now points to commit a1b2c3d
```

### Reset Use Cases

**Fix last commit message**:
```bash
git reset --soft HEAD~1
git commit -m "Correct message"
```

**Combine recent commits**:
```bash
git reset --soft HEAD~3
git commit -m "Combined changes from last 3 commits"
```

**Discard experimental work**:
```bash
git reset --hard HEAD
# Back to clean state
```

### ⚠️ Reset Warnings

- `--hard` permanently deletes changes
- Don't reset public commits
- Can recover with reflog (if recent)

---

## Git Revert

### What is Revert?

Create a new commit that undoes previous changes. **Safe for shared branches**.

### Revert vs Reset

**Reset**: Moves branch pointer backward (rewrites history)
**Revert**: Creates new commit that undoes changes (preserves history)

**Use revert when**:
- Commit is already pushed
- Branch is shared with others
- Want to preserve history

**Use reset when**:
- Commit is local only
- Working alone
- Want clean history

### Revert Examples

```bash
# Revert most recent commit
git revert HEAD

# Revert specific commit
git revert a1b2c3d

# Revert multiple commits
git revert HEAD~3..HEAD

# Revert without creating commit (stage only)
git revert -n a1b2c3d
```

### Revert Use Cases

**Scenario: Bad commit in production**
```bash
git revert bug-causing-commit
git push origin main
# Safely undoes bad commit
```

---

## Git Reflog

### What is Reflog?

Reference log tracking all HEAD movements. **Recovery tool for "lost" commits**.

### Viewing Reflog

```bash
# Show reflog
git reflog

# Example output:
a1b2c3d HEAD@{0}: commit: Add feature
d4e5f6g HEAD@{1}: checkout: moving from main to feature
g7h8i9j HEAD@{2}: commit: Fix bug
```

### Recovery with Reflog

**Scenario: Accidentally deleted branch**
```bash
# Deleted branch with unmerged commits
git branch -D feature-branch

# Find commit in reflog
git reflog
# See: a1b2c3d HEAD@{5}: commit: Last work on feature

# Recreate branch
git checkout -b feature-branch a1b2c3d
# Branch recovered! 🎉
```

**Scenario: Hard reset mistake**
```bash
# Accidentally reset too far
git reset --hard HEAD~10

# Use reflog to find old position
git reflog
# See: d4e5f6g HEAD@{1}: commit: Before reset

# Go back
git reset --hard d4e5f6g
```

---

## Git Tags

### What are Tags?

Permanent markers for specific commits. Usually for releases.

### Creating Tags

**Lightweight tag**:
```bash
git tag v1.0.0
```

**Annotated tag** (recommended):
```bash
git tag -a v1.0.0 -m "Version 1.0.0 release"
```

**Tag specific commit**:
```bash
git tag -a v0.9.0 a1b2c3d -m "Beta release"
```

### Viewing Tags

```bash
# List all tags
git tag

# Show tag details
git show v1.0.0

# List tags matching pattern
git tag -l "v1.*"
```

### Pushing Tags

```bash
# Push specific tag
git push origin v1.0.0

# Push all tags
git push origin --tags
```

### Deleting Tags

```bash
# Delete local tag
git tag -d v1.0.0

# Delete remote tag
git push origin --delete v1.0.0
```

---

## Best Practices

### Commit History Hygiene

**Before pushing**:
```bash
# Clean up with interactive rebase
git rebase -i HEAD~5
# Squash "WIP" commits
# Fix commit messages
# Reorder logical groups
```

**Result**: Clean, readable history

### When to Use What

| Scenario | Command |
|----------|---------|
| Update feature with main changes | `git rebase main` |
| Temporarily save work | `git stash` |
| Apply specific commit | `git cherry-pick` |
| Undo local commit | `git reset` |
| Undo public commit | `git revert` |
| Recover deleted commit | `git reflog` |
| Mark release | `git tag` |

### Safety Rules

1. **Never rebase public branches**
2. **Be careful with `reset --hard`**
3. **Use revert for shared branches**
4. **Push tags separately**
5. **Check reflog if you lose commits**

---

## Key Takeaways

✅ **Rebase** creates linear history but changes commit hashes

✅ **Cherry-pick** applies specific commits to other branches

✅ **Stash** temporarily saves work without committing

✅ **Reset** moves branch pointer (use carefully!)

✅ **Revert** safely undoes commits in shared branches

✅ **Reflog** can recover "lost" commits

✅ **Tags** mark important points (releases)

✅ **Interactive rebase** cleans up commit history

---

**Happy Advanced Git Usage!** 🚀

*"With great power comes great responsibility." - Use advanced Git commands wisely!*
