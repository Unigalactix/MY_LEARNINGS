# Branching and Merging Quiz 📝

**Topic**: Git Branching and Merging  
**Difficulty**: ⭐⭐ Beginner to Intermediate  
**Time**: ~25 minutes

**Instructions**: 
- Try to answer all questions before checking the answers
- Focus on understanding branching concepts and merge strategies
- Practice the commands after taking the quiz

---

## Section 1: Branch Basics

### Question 1 (⭐ Beginner)
**What is a branch in Git?**

A) A copy of the entire repository  
B) A lightweight movable pointer to a commit  
C) A folder containing different code versions  
D) A backup of your project

<details>
<summary>Click to reveal answer</summary>

**Answer: B - A lightweight movable pointer to a commit**

**Explanation**: 
A branch in Git is essentially a pointer to a specific commit. It's not a copy of files or a new folder - it's just a reference that Git uses to track different lines of development.

**Key points**:
- Branches are very lightweight (just 41 bytes!)
- Creating a branch just creates a new pointer
- Multiple branches can point to the same commit
- The HEAD pointer indicates your current branch

**Misconceptions**:
- ❌ Branches don't duplicate files (that would waste space)
- ❌ Branches aren't folders in your file system
- ❌ Branches aren't backups (though they can serve that purpose)

</details>

---

### Question 2 (⭐ Beginner)
**Which command creates a new branch AND switches to it?**

A) `git branch -b new-feature`  
B) `git checkout -b new-feature`  
C) `git create new-feature`  
D) `git branch new-feature && git switch`

<details>
<summary>Click to reveal answer</summary>

**Answer: B - `git checkout -b new-feature`**

**Explanation**: 
The `-b` flag with `git checkout` both creates and switches to the new branch in one command.

**Alternative commands**:
```bash
# Modern equivalent (Git 2.23+)
git switch -c new-feature

# Two-step process (older method)
git branch new-feature
git checkout new-feature
```

**Why use the shortcut?**
- Saves time and typing
- Atomic operation (less chance of errors)
- Industry standard practice

</details>

---

### Question 3 (⭐ Beginner)
**What does the HEAD pointer represent?**

A) The most recent commit in the repository  
B) The first commit in the repository  
C) The branch you are currently on  
D) The main/master branch

<details>
<summary>Click to reveal answer</summary>

**Answer: C - The branch you are currently on**

**Explanation**: 
HEAD is a special pointer that always points to the current branch reference (or directly to a commit in a detached HEAD state).

**Visual representation**:
```
HEAD → main → [Commit C3]
```

**What happens when you switch branches**:
```bash
git checkout feature
# Now: HEAD → feature → [Commit C5]
```

**Special case - Detached HEAD**:
When HEAD points directly to a commit instead of a branch:
```bash
git checkout <commit-hash>
# HEAD → [Commit C2] (no branch)
```

</details>

---

## Section 2: Branch Operations

### Question 4 (⭐ Beginner)
**How do you list all branches (including remote branches)?**

A) `git branch`  
B) `git branch --all`  
C) `git branch -a`  
D) Both B and C

<details>
<summary>Click to reveal answer</summary>

**Answer: D - Both B and C**

**Explanation**: 
Both `git branch --all` and `git branch -a` show all branches (local and remote).

**Different branch listing commands**:
```bash
git branch          # Local branches only
git branch -r       # Remote branches only
git branch -a       # All branches
git branch -v       # With last commit message
git branch -vv      # With tracking information
```

**Example output**:
```
* main
  feature-login
  remotes/origin/main
  remotes/origin/develop
```
(The asterisk * shows your current branch)

</details>

---

### Question 5 (⭐⭐ Intermediate)
**What's the difference between `git branch -d` and `git branch -D`?**

A) They are the same command  
B) `-d` deletes local branches, `-D` deletes remote branches  
C) `-d` is safe (prevents deletion of unmerged work), `-D` forces deletion  
D) `-d` deletes the branch, `-D` deletes the commits too

<details>
<summary>Click to reveal answer</summary>

**Answer: C - `-d` is safe (prevents deletion of unmerged work), `-D` forces deletion**

**Explanation**: 

**`git branch -d` (safe delete)**:
- Only deletes if branch is fully merged
- Protects you from losing work
- Git will warn you if branch has unmerged commits

**`git branch -D` (force delete)**:
- Deletes branch regardless of merge status
- Use with caution - can lose work!
- Useful for abandoned experimental branches

**Examples**:
```bash
# Safe delete - will fail if unmerged
git branch -d feature-login
# Error if not merged!

# Force delete - always succeeds
git branch -D experimental-feature
# Deleted even with unmerged work
```

**When to use each**:
- Use `-d` as default (safety first)
- Use `-D` only when you're sure you want to discard work

</details>

---

## Section 3: Merging Concepts

### Question 6 (⭐⭐ Intermediate)
**What is a fast-forward merge?**

A) A merge that happens very quickly  
B) A merge where Git simply moves the branch pointer forward  
C) A merge that uses advanced algorithms  
D) A merge between two branches with many commits

<details>
<summary>Click to reveal answer</summary>

**Answer: B - A merge where Git simply moves the branch pointer forward**

**Explanation**: 
A fast-forward merge occurs when there's a direct linear path from the current branch to the target branch - no divergent changes.

**Visual example**:
```
Before merge:
main    → [C1] → [C2]
feature →              → [C3] → [C4]

After fast-forward:
main    → [C1] → [C2] → [C3] → [C4]
feature →                          ↑
```

**When does fast-forward happen?**
- No new commits on target branch since feature branch created
- Just a straight line of commits to add
- Git simply moves the pointer (very fast!)

**Prevent fast-forward** (create merge commit):
```bash
git merge --no-ff feature-branch
```

</details>

---

### Question 7 (⭐⭐ Intermediate)
**When does a three-way merge occur?**

A) When merging three branches at once  
B) When both branches have diverged with new commits  
C) When there are three merge conflicts  
D) When using three different merge strategies

<details>
<summary>Click to reveal answer</summary>

**Answer: B - When both branches have diverged with new commits**

**Explanation**: 
A three-way merge happens when both branches have new commits since they diverged, requiring Git to create a merge commit.

**Why "three-way"?**
Git looks at three commits:
1. **Common ancestor** (where branches diverged)
2. **Tip of current branch** (your changes)
3. **Tip of branch being merged** (their changes)

**Visual example**:
```
Before merge:
        ┌─ [C3] ← feature
       /
[C1] ─ [C2] ─ [C4] ← main

After three-way merge:
        ┌─ [C3] ─┐
       /          ↓
[C1] ─ [C2] ─ [C4] ─ [C5 merge] ← main
```

**The merge commit**:
- Has two parent commits
- Combines changes from both branches
- Preserves history of both development paths

</details>

---

### Question 8 (⭐⭐ Intermediate)
**What command would you use to merge 'feature-login' into 'main'?**

A) 
```bash
git checkout feature-login
git merge main
```

B) 
```bash
git checkout main
git merge feature-login
```

C) 
```bash
git merge main feature-login
```

D) 
```bash
git branch merge feature-login main
```

<details>
<summary>Click to reveal answer</summary>

**Answer: B**

**Correct workflow**:
```bash
git checkout main
git merge feature-login
```

**Why this order?**
1. **First**: Check out the branch you want to merge INTO (main)
2. **Second**: Merge the branch you want to merge FROM (feature-login)

**Remember**: "I'm on branch X, I want to merge Y into X"

**Complete workflow**:
```bash
# 1. Switch to target branch
git checkout main

# 2. Update it first (good practice)
git pull origin main

# 3. Merge feature branch
git merge feature-login

# 4. Push merged result
git push origin main
```

**Common mistake**: Option A merges main INTO feature-login (backwards!)

</details>

---

## Section 4: Merge Conflicts

### Question 9 (⭐⭐ Intermediate)
**What causes a merge conflict?**

A) Merging branches with different names  
B) Merging branches created by different people  
C) When the same lines are modified differently in both branches  
D) When branches are more than a week old

<details>
<summary>Click to reveal answer</summary>

**Answer: C - When the same lines are modified differently in both branches**

**Explanation**: 
A merge conflict occurs when Git cannot automatically determine which version of code to keep because the same lines were changed in incompatible ways.

**Common conflict scenarios**:

1. **Same line, different changes**:
```python
# Branch A
def greet():
    return "Hello!"

# Branch B  
def greet():
    return "Hi there!"
```

2. **File deleted vs modified**:
- Branch A: Deletes `config.py`
- Branch B: Modifies `config.py`

3. **Overlapping edits**:
- Both branches edit adjacent or same lines

**What doesn't cause conflicts**:
- ✅ Different files modified
- ✅ Different functions modified
- ✅ Different parts of same file modified
- ✅ Same file, different lines (usually)

</details>

---

### Question 10 (⭐⭐ Intermediate)
**What do the conflict markers mean?**

```
<<<<<<< HEAD
Code A
=======
Code B
>>>>>>> feature-branch
```

A) Code A is correct, Code B is wrong  
B) Code A is from current branch, Code B is from merging branch  
C) Code A is old code, Code B is new code  
D) Code A will be kept, Code B will be discarded

<details>
<summary>Click to reveal answer</summary>

**Answer: B - Code A is from current branch (HEAD), Code B is from merging branch**

**Explanation**: 
Conflict markers show you both versions so you can decide what to keep.

**Marker meanings**:
- `<<<<<<< HEAD` - Start of current branch's version
- `=======` - Separator between versions
- `>>>>>>> feature-branch` - End of incoming branch's version

**Example conflict**:
```python
def calculate_total(items):
<<<<<<< HEAD
    # Current branch: includes tax
    return sum(items) * 1.08
=======
    # Feature branch: includes discount
    return sum(items) * 0.9
>>>>>>> feature-discount
```

**Your options**:
1. Keep only HEAD version
2. Keep only feature-branch version
3. Keep both (combine them)
4. Write completely new code

**After resolving**, remove all markers and:
```bash
git add <file>
git commit -m "Resolve conflict"
```

</details>

---

### Question 11 (⭐⭐ Intermediate)
**How do you abort a merge that has conflicts?**

A) `git merge --cancel`  
B) `git merge --abort`  
C) `git reset --hard`  
D) `git checkout --abort`

<details>
<summary>Click to reveal answer</summary>

**Answer: B - `git merge --abort`**

**Explanation**: 
`git merge --abort` safely cancels the merge and returns your repository to the state before you started the merge.

**When to use it**:
- Conflicts are too complex to resolve immediately
- You merged the wrong branch
- You need to prepare or research before resolving
- You want to start over

**What happens**:
```bash
# During merge with conflicts
git status
# Shows "Unmerged paths"

# Abort the merge
git merge --abort

# Back to clean state
git status
# "nothing to commit, working tree clean"
```

**Alternative (more dangerous)**:
```bash
git reset --hard HEAD
```
⚠️ This discards ALL uncommitted changes, not just merge!

**After aborting**:
- Your working directory is restored
- No merge commit created
- Can try again when ready

</details>

---

## Section 5: Branch Best Practices

### Question 12 (⭐ Beginner)
**What is the recommended branch naming convention?**

A) Use spaces: `my new feature`  
B) Use underscores: `my_new_feature`  
C) Use hyphens with prefix: `feature/my-new-feature`  
D) Use random names: `branch123`

<details>
<summary>Click to reveal answer</summary>

**Answer: C - Use hyphens with prefix: `feature/my-new-feature`**

**Explanation**: 
Clear, prefixed branch names help teams understand the purpose and status of each branch at a glance.

**Common prefixes**:
- `feature/` or `feat/` - New features
- `bugfix/` or `fix/` - Bug fixes
- `hotfix/` - Urgent production fixes
- `release/` - Release preparation
- `docs/` - Documentation
- `test/` - Testing improvements
- `refactor/` - Code refactoring

**Good examples**:
```bash
feature/user-authentication
feature/shopping-cart
bugfix/login-validation
bugfix/navbar-responsive
hotfix/security-patch
release/v2.0.0
docs/api-documentation
test/unit-tests-auth
refactor/database-layer
```

**Bad examples**:
```bash
my branch          # Spaces don't work
temp              # Not descriptive
fix               # Too vague
johns_stuff       # Not about purpose
asdf              # Random
```

**Why this matters**:
- Easy to understand purpose
- Can be filtered/organized by type
- Professional and maintainable

</details>

---

### Question 13 (⭐⭐ Intermediate)
**Before merging a feature branch into main, what should you do?**

A) Delete the feature branch first  
B) Create a backup of your computer  
C) Pull latest changes from main and update your feature branch  
D) Nothing, just merge immediately

<details>
<summary>Click to reveal answer</summary>

**Answer: C - Pull latest changes from main and update your feature branch**

**Explanation**: 
Always sync with the latest main branch before merging to catch conflicts early and ensure your feature works with the latest code.

**Recommended workflow**:

```bash
# 1. Save your feature work
git checkout feature-branch
git add .
git commit -m "Complete feature implementation"

# 2. Update main branch
git checkout main
git pull origin main

# 3. Go back to feature and update it
git checkout feature-branch
git merge main
# Or: git rebase main (alternative)

# 4. Resolve any conflicts NOW (on feature branch)
# Fix conflicts, test thoroughly

# 5. NOW merge into main
git checkout main
git merge feature-branch

# 6. Push to remote
git push origin main
```

**Why this approach?**
- ✅ Conflicts resolved on feature branch (not main)
- ✅ Main branch stays clean and stable
- ✅ Feature tested with latest code
- ✅ Easier to fix problems

**Anti-pattern**:
```bash
# ❌ DON'T DO THIS
git checkout main
git merge old-feature-branch
# Conflicts on main! Main is now unstable!
```

</details>

---

### Question 14 (⭐⭐ Intermediate)
**When should you delete a branch?**

A) Never - keep all branches forever  
B) Immediately after creating it  
C) After it has been merged and pushed  
D) Only if it has no commits

<details>
<summary>Click to reveal answer</summary>

**Answer: C - After it has been merged and pushed**

**Explanation**: 
Once a feature branch is successfully merged into main and pushed to the remote, it's safe and recommended to delete it to keep the repository clean.

**Typical workflow**:

```bash
# 1. Create feature branch
git checkout -b feature/user-login

# 2. Work and commit
git commit -m "Implement login"

# 3. Merge to main
git checkout main
git merge feature/user-login

# 4. Push merged changes
git push origin main

# 5. NOW delete local branch
git branch -d feature/user-login

# 6. Delete remote branch
git push origin --delete feature/user-login
```

**Why delete merged branches?**
- ✅ Keeps `git branch` list manageable
- ✅ Reduces confusion about active work
- ✅ Work is preserved in commit history
- ✅ Professional repository maintenance

**Don't worry about losing work!**
- Commits are still in history
- Can recover if needed with `git reflog`
- GitHub/GitLab show closed branches in UI

**When NOT to delete**:
- Long-running branches (develop, staging)
- Release branches you want to keep
- Branches not yet merged

</details>

---

## Section 6: Advanced Scenarios

### Question 15 (⭐⭐⭐ Advanced)
**What is the difference between `git merge` and `git rebase`?**

A) They do exactly the same thing  
B) Merge creates merge commits; rebase rewrites history  
C) Merge is faster than rebase  
D) Rebase only works with remote branches

<details>
<summary>Click to reveal answer</summary>

**Answer: B - Merge creates merge commits; rebase rewrites history**

**Explanation**: 
Both integrate changes, but they create very different commit histories.

**Git Merge**:
```
Before:
main    → [C1] → [C2] → [C4]
feature →              → [C3] → [C5]

After merge:
main    → [C1] → [C2] → [C4] ──→ [C6 merge]
feature →              → [C3] → [C5] ──┘
```
- Creates a merge commit
- Preserves exact history
- Shows when branches merged

**Git Rebase**:
```
Before:
main    → [C1] → [C2] → [C4]
feature →              → [C3] → [C5]

After rebase:
main    → [C1] → [C2] → [C4] → [C3'] → [C5']
```
- Rewrites commits
- Creates linear history
- No merge commit

**When to use each**:

**Use Merge when**:
- Working on shared/public branches
- Want to preserve exact history
- Following GitHub Flow (PRs)

**Use Rebase when**:
- Cleaning up local commits
- Want linear history
- Feature branch not yet shared

**Golden Rule**: Never rebase public/shared branches!

</details>

---

## Section 7: Troubleshooting

### Question 16 (⭐⭐ Intermediate)
**You switched branches but your uncommitted changes came with you. What happened?**

A) Git is broken  
B) The changes weren't tracked by Git  
C) You forgot to commit before switching  
D) This is normal - Git carries over uncommitted changes

<details>
<summary>Click to reveal answer</summary>

**Answer: D - This is normal - Git carries over uncommitted changes**

**Explanation**: 
Git allows you to switch branches with uncommitted changes if they don't conflict with the target branch. This is actually a feature!

**What Git does**:
1. Checks if your changes conflict with target branch
2. If no conflict: carries changes over
3. If conflict: prevents branch switch

**Example**:
```bash
# On feature-a branch
echo "new code" >> new-file.txt
git status
# Changes not staged

# Switch branches
git checkout main
# Changes come with you!

git status
# Still shows new-file.txt as modified
```

**To prevent this**, commit or stash first:

**Option 1: Commit**
```bash
git add .
git commit -m "WIP: Save progress"
git checkout other-branch
```

**Option 2: Stash**
```bash
git stash save "Work in progress"
git checkout other-branch
# Later, return and restore:
git checkout feature-a
git stash pop
```

**When Git will prevent switching**:
```bash
# File conflicts with target branch
git checkout main
# error: Your local changes to the following files 
# would be overwritten by checkout
```

</details>

---

### Question 17 (⭐⭐⭐ Advanced)
**You accidentally deleted a branch. How can you recover it?**

A) It's gone forever  
B) Use `git branch --recover`  
C) Find the commit with `git reflog` and recreate the branch  
D) Restore from backup only

<details>
<summary>Click to reveal answer</summary>

**Answer: C - Find the commit with `git reflog` and recreate the branch**

**Explanation**: 
Even after deleting a branch, the commits still exist in Git's database. You can find them with `reflog` and recreate the branch.

**Recovery steps**:

**1. Find the lost commit**:
```bash
git reflog
# Shows all recent HEAD movements
```

Example output:
```
a1b2c3d HEAD@{0}: checkout: moving from feature-login to main
e4f5g6h HEAD@{1}: commit: Add login validation
7i8j9k0 HEAD@{2}: commit: Add login form
```

**2. Identify the commit** you want to recover (e.g., `e4f5g6h`)

**3. Recreate the branch**:
```bash
git branch recovered-feature e4f5g6h
```

**4. Verify**:
```bash
git checkout recovered-feature
git log
# Your commits are back!
```

**Important notes**:
- Reflog keeps history for ~90 days by default
- Only works for local repository
- Remote branches need different recovery (contact repo admin)

**Prevention**:
- Always push branches to remote before deleting
- Use `git branch -d` (safe) instead of `-D` (force)
- Double-check branch name before deleting

</details>

---

## Section 8: Practical Application

### Question 18 (⭐⭐⭐ Advanced)
**Which workflow is best for a team of 5 developers working on a web application?**

A) Everyone commits directly to main  
B) Each developer creates feature branches and merges via pull requests  
C) Use only one branch with numbered commits  
D) Create one branch per developer

<details>
<summary>Click to reveal answer</summary>

**Answer: B - Each developer creates feature branches and merges via pull requests**

**Explanation**: 
The Feature Branch Workflow with Pull Requests is the industry standard for team collaboration.

**Recommended workflow**:

```bash
# Developer 1: User Authentication
git checkout -b feature/user-auth
# ... work and commit ...
# Push and create pull request
git push origin feature/user-auth

# Developer 2: Shopping Cart
git checkout -b feature/shopping-cart
# ... work and commit ...
git push origin feature/shopping-cart

# Developer 3: Payment Integration
git checkout -b feature/payment
# ... work and commit ...
git push origin feature/payment
```

**Benefits**:
- ✅ Isolated development
- ✅ Code review via PRs
- ✅ Main branch stays stable
- ✅ Easy to track who's working on what
- ✅ Can merge independently
- ✅ Conflicts resolved before merging
- ✅ CI/CD can test each feature

**Pull Request Process**:
1. Create feature branch
2. Push to remote
3. Open PR on GitHub
4. Team reviews code
5. Address feedback
6. Merge when approved
7. Delete feature branch

**Why not other options?**

**A: Direct commits to main**
- ❌ No code review
- ❌ Breaks production
- ❌ Merge conflicts on main
- ❌ No isolation

**C: One branch, numbered commits**
- ❌ Can't work in parallel
- ❌ Everyone blocks everyone
- ❌ No organization

**D: One branch per developer**
- ❌ Developers work on multiple features
- ❌ Doesn't scale
- ❌ No feature isolation

</details>

---

## Practical Exercise Challenges

### Challenge 1: Basic Branch Flow
Complete this workflow in your terminal:

1. Create a repository
2. Create and switch to a branch called `feature/header`
3. Add a file called `header.html`
4. Commit the change
5. Switch back to main
6. Merge the feature branch
7. Delete the feature branch
8. Verify with `git log`

<details>
<summary>Click to see solution</summary>

```bash
# 1. Create repository
mkdir branch-practice && cd branch-practice
git init

# 2. Create and switch to feature branch
git checkout -b feature/header

# 3. Add file
echo "<header>My Site</header>" > header.html

# 4. Commit
git add header.html
git commit -m "Add header component"

# 5. Switch to main
git checkout main

# 6. Merge feature
git merge feature/header

# 7. Delete branch
git branch -d feature/header

# 8. Verify
git log --oneline
```

</details>

---

### Challenge 2: Merge Conflict Resolution
Create and resolve a merge conflict:

1. Create two branches from main
2. Modify the same line in both branches
3. Merge one branch to main
4. Attempt to merge the second (will conflict!)
5. Resolve the conflict manually
6. Complete the merge

<details>
<summary>Click to see solution</summary>

```bash
# Setup
mkdir conflict-practice && cd conflict-practice
git init
echo "Original" > file.txt
git add file.txt
git commit -m "Initial commit"

# Create branch A
git checkout -b branch-a
echo "Version A" > file.txt
git commit -am "Change to A"

# Create branch B from main
git checkout main
git checkout -b branch-b
echo "Version B" > file.txt
git commit -am "Change to B"

# Merge branch-a (success)
git checkout main
git merge branch-a

# Merge branch-b (conflict!)
git merge branch-b
# CONFLICT!

# Check status
git status
# Shows conflict in file.txt

# Edit file.txt, remove markers, choose or combine versions
# Example resolution:
echo "Version A and B combined" > file.txt

# Complete merge
git add file.txt
git commit -m "Resolve conflict between branch-a and branch-b"

# Verify
git log --oneline --graph
```

</details>

---

## Summary & Key Takeaways

✅ **Branches are lightweight pointers** to commits, not file copies

✅ **HEAD** points to your current branch

✅ **Fast-forward merge** happens when no divergent commits exist

✅ **Three-way merge** creates a merge commit when branches have diverged

✅ **Merge conflicts** occur when same lines modified differently

✅ **Always pull before merging** to stay up to date

✅ **Delete branches after merging** to keep repository clean

✅ **Use descriptive branch names** with prefixes

✅ **Feature branch workflow** is standard for teams

✅ **Git reflog** can recover deleted branches

---

## Score Yourself

- **14-18 correct**: 🌟 Branching Master! You understand Git branching deeply.
- **10-13 correct**: 💪 Strong understanding! Review topics you missed.
- **6-9 correct**: 📚 Good start! Practice more with hands-on exercises.
- **0-5 correct**: 🌱 Keep learning! Re-read notes and try exercises.

---

**Next Steps**: 
- Practice creating and merging branches
- Intentionally create conflicts to practice resolution
- Explore GitHub pull request workflow
- Learn about rebasing vs merging

**Happy Branching!** 🌿
