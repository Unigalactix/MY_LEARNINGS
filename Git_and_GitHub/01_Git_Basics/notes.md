# Git Basics - Comprehensive Notes 📚

## What is Git?

Git is a distributed version control system (VCS) that tracks changes in files and coordinates work among multiple people. Created by Linus Torvalds in 2005, Git has become the industry standard for version control.

### Why Use Git?

- **Track Changes**: See what changed, when, and by whom
- **Collaboration**: Work with others without conflicts
- **Backup**: Never lose your work
- **Experimentation**: Try new ideas safely with branches
- **History**: Travel back in time to any previous version
- **Professionalism**: Industry-standard tool for developers

---

## Core Concepts

### Repository (Repo)
A repository is a directory that Git tracks. It contains:
- Your project files
- `.git` folder (Git's database)
- Complete history of all changes

### Commit
A snapshot of your project at a specific point in time. Think of it as a save point in a video game.

### Working Directory
The files you're currently working on (what you see in your file explorer).

### Staging Area (Index)
A holding area for changes you want to include in your next commit.

### The Three States
Every file in Git exists in one of three states:

1. **Modified**: You've changed the file but haven't committed it
2. **Staged**: You've marked a modified file to go into your next commit
3. **Committed**: The data is safely stored in your local repository

```
Working Directory  →  Staging Area  →  Repository
     (Edit)           (git add)       (git commit)
```

---

## Installation & Setup

### Installing Git

**Windows**:
```bash
# Download from git-scm.com and run installer
# Or use chocolatey:
choco install git
```

**macOS**:
```bash
# Using Homebrew:
brew install git

# Or Xcode Command Line Tools:
xcode-select --install
```

**Linux (Ubuntu/Debian)**:
```bash
sudo apt-get update
sudo apt-get install git
```

**Verify Installation**:
```bash
git --version
# Should output: git version 2.x.x
```

### Initial Configuration

**Set Your Identity** (Required):
```bash
# Set your name
git config --global user.name "Your Name"

# Set your email
git config --global user.email "your.email@example.com"
```

**Set Default Editor** (Optional):
```bash
# Use VS Code
git config --global core.editor "code --wait"

# Use Vim
git config --global core.editor "vim"

# Use Nano
git config --global core.editor "nano"
```

**Set Default Branch Name**:
```bash
# Modern convention is 'main' instead of 'master'
git config --global init.defaultBranch main
```

**View All Configuration**:
```bash
git config --list
```

---

## Essential Commands

### 1. Creating a Repository

**Initialize a New Repository**:
```bash
# Create project directory
mkdir my-project
cd my-project

# Initialize Git
git init

# What happens:
# - Creates .git folder
# - Repository is now tracking this directory
```

**Clone an Existing Repository**:
```bash
# Clone from URL
git clone https://github.com/username/repository.git

# Clone to specific folder
git clone https://github.com/username/repository.git my-folder
```

### 2. Checking Status

**See Current State**:
```bash
git status

# Shows:
# - Which branch you're on
# - Which files are modified
# - Which files are staged
# - Which files are untracked
```

**Example Output**:
```
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   file1.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
        modified:   file2.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        file3.txt
```

### 3. Staging Changes

**Stage Specific Files**:
```bash
# Stage one file
git add filename.txt

# Stage multiple files
git add file1.txt file2.txt

# Stage all files in directory
git add .

# Stage all modified files (not new files)
git add -u
```

**Why Stage?**
Staging lets you choose exactly what goes in your next commit. You might have modified 10 files but only want to commit 3.

### 4. Committing Changes

**Create a Commit**:
```bash
# Commit with message
git commit -m "Add user login feature"

# Commit with detailed message (opens editor)
git commit

# Stage and commit modified files in one command
git commit -am "Update documentation"
```

**Good Commit Messages**:
```bash
# ✅ Good - Clear and specific
git commit -m "Fix null pointer exception in user controller"
git commit -m "Add email validation to signup form"
git commit -m "Update README with installation instructions"

# ❌ Bad - Vague and unhelpful
git commit -m "fixed stuff"
git commit -m "updates"
git commit -m "asdfasdf"
```

### 5. Viewing History

**View Commit Log**:
```bash
# Full log
git log

# Compact one-line format
git log --oneline

# Last 5 commits
git log -5

# Show file changes
git log --stat

# Show actual changes
git log -p

# Pretty format
git log --graph --oneline --all
```

**Example Output**:
```
commit 1a2b3c4d5e6f (HEAD -> main)
Author: John Doe <john@example.com>
Date:   Mon Jan 7 10:30:00 2024 -0500

    Add user authentication

commit 9z8y7x6w5v4u
Author: John Doe <john@example.com>
Date:   Mon Jan 7 09:15:00 2024 -0500

    Initial commit
```

### 6. Viewing Changes

**See Uncommitted Changes**:
```bash
# Changes in working directory (not staged)
git diff

# Changes in staging area
git diff --staged

# Changes in specific file
git diff filename.txt
```

**Example Output**:
```diff
diff --git a/file.txt b/file.txt
index e69de29..1234567 100644
--- a/file.txt
+++ b/file.txt
@@ -1,3 +1,4 @@
 Line 1
 Line 2
+Line 3 (new line added)
 Line 4
```

---

## Common Workflows

### Workflow 1: Starting a New Project

```bash
# 1. Create and enter project directory
mkdir my-website
cd my-website

# 2. Initialize Git
git init

# 3. Create initial files
echo "# My Website" > README.md
echo "console.log('Hello');" > index.js

# 4. Stage files
git add .

# 5. Create first commit
git commit -m "Initial commit: Add README and index.js"

# 6. Verify
git log --oneline
```

### Workflow 2: Making Changes

```bash
# 1. Check status
git status

# 2. Make changes to files
# (edit files in your editor)

# 3. See what changed
git diff

# 4. Stage changes
git add filename.txt

# 5. Commit changes
git commit -m "Describe what you changed"

# 6. Verify commit
git log --oneline
```

### Workflow 3: Daily Development

```bash
# Morning: Check status
git status

# Work: Edit files as needed

# Frequently: Check what changed
git diff

# When ready: Stage and commit
git add .
git commit -m "Add new feature X"

# Repeat throughout the day
# End of day: Review your commits
git log --oneline --since="today"
```

---

## Undoing Changes

### Unstage Files

```bash
# Unstage specific file (keep changes)
git restore --staged filename.txt

# Unstage all files
git restore --staged .
```

### Discard Changes in Working Directory

```bash
# ⚠️ WARNING: This permanently removes your changes!

# Discard changes in specific file
git restore filename.txt

# Discard all changes
git restore .
```

### Amend Last Commit

```bash
# Forgot to include a file?
git add forgotten-file.txt
git commit --amend --no-edit

# Want to change commit message?
git commit --amend -m "New commit message"
```

---

## The .gitignore File

### What is .gitignore?

A file that tells Git which files or directories to ignore (not track).

### Common .gitignore Patterns

```bash
# Create .gitignore file
cat > .gitignore << EOF
# Dependencies
node_modules/
venv/
*.pyc

# IDE files
.vscode/
.idea/
*.swp

# Build outputs
dist/
build/
*.exe

# OS files
.DS_Store
Thumbs.db

# Environment variables
.env
.env.local

# Logs
*.log
logs/
EOF
```

### .gitignore Patterns Explained

```bash
# Ignore specific file
secret.txt

# Ignore all files with extension
*.log

# Ignore directory
node_modules/

# Ignore all .txt files in specific directory
docs/*.txt

# Ignore all .pdf files in all directories
**/*.pdf

# Exception: Don't ignore this specific file
!important.log
```

---

## Helpful Aliases

Speed up your workflow with aliases:

```bash
# Set up useful aliases
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'restore --staged'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual 'log --graph --oneline --all'

# Now you can use:
git st          # instead of git status
git co main     # instead of git checkout main
git unstage .   # instead of git restore --staged .
```

---

## Best Practices

### 1. Commit Often
- Make small, focused commits
- Easier to understand and revert if needed
- Better documentation of your progress

### 2. Write Good Commit Messages
```bash
# Format:
# <type>: <subject>
# 
# <body>

# Examples:
git commit -m "feat: Add user login functionality"
git commit -m "fix: Correct null pointer in payment processor"
git commit -m "docs: Update API documentation"
git commit -m "refactor: Simplify database query logic"
```

### 3. Keep Commits Atomic
Each commit should represent one logical change:
```bash
# ✅ Good - One feature per commit
git commit -m "Add email validation"
git commit -m "Add password strength checker"

# ❌ Bad - Multiple unrelated changes
git commit -m "Add validation, fix bug, update docs"
```

### 4. Review Before Committing
```bash
# Always check what you're committing
git diff --staged

# Verify which files are staged
git status
```

### 5. Don't Commit Sensitive Data
- Never commit passwords, API keys, or secrets
- Use environment variables
- Add sensitive files to .gitignore

---

## Troubleshooting

### "I made changes but git status shows nothing"

**Problem**: File might not be tracked yet.

**Solution**:
```bash
# Add the file
git add filename.txt
```

### "I committed too early"

**Solution**:
```bash
# Add more changes and amend
git add forgotten-file.txt
git commit --amend --no-edit
```

### "I want to undo my last commit"

**Solution**:
```bash
# Undo commit but keep changes
git reset --soft HEAD~1

# Undo commit and discard changes (⚠️ careful!)
git reset --hard HEAD~1
```

### "Git is slow"

**Solution**:
```bash
# Run garbage collection
git gc

# Check repo size
du -sh .git
```

---

## Quick Reference

### Most Used Commands
```bash
git init                # Create repository
git status              # Check status
git add <file>          # Stage file
git add .               # Stage all
git commit -m "msg"     # Commit
git log                 # View history
git log --oneline       # Compact history
git diff                # View changes
```

### File Lifecycle
```
Untracked → (git add) → Staged → (git commit) → Committed
                          ↓
                    (git restore --staged)
                          ↓
                      Modified
```

---

## Practice Exercises

### Exercise 1: First Repository
1. Create a new directory called `git-practice`
2. Initialize a Git repository
3. Create a file called `hello.txt` with some text
4. Stage and commit the file
5. View the commit history

### Exercise 2: Multiple Commits
1. Modify `hello.txt`
2. Create a new file `world.txt`
3. Make three separate commits:
   - Commit modified hello.txt
   - Commit new world.txt
   - Create and commit another file
4. View your commit history

### Exercise 3: Using .gitignore
1. Create files: `secret.txt`, `notes.txt`, `data.log`
2. Create .gitignore to ignore `.log` files
3. Add and commit `notes.txt` and `.gitignore`
4. Verify `data.log` is ignored

---

## Next Steps

After mastering Git basics:
1. Move to [02_Branching_and_Merging](../02_Branching_and_Merging/) to learn branching
2. Practice daily with real projects
3. Take the [Git Basics Quiz](./QUIZ.md)
4. Complete [Coding Challenges](./CHALLENGES.md)

---

**Congratulations!** You now understand Git fundamentals. Keep practicing! 🚀
