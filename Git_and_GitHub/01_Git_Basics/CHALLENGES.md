# Git Basics - Coding Challenges 💻

**Topic**: Git Fundamentals  
**Total Challenges**: 6  
**Estimated Time**: 2-3 hours

**Instructions**: 
- Work in the terminal/command line
- Create test repositories to practice safely
- Complete challenges in order
- Verify results with Git commands

---

## Challenge #1: First Repository ⭐

**Difficulty**: Beginner  
**Time**: 15 minutes  
**Concepts**: git init, git add, git commit, git log

### Problem Statement

Create your first Git repository from scratch with multiple commits.

### Requirements

1. Create a directory called `my-first-repo`
2. Initialize it as a Git repository
3. Create three files: `README.md`, `script.js`, `style.css`
4. Make separate commits for each file
5. View the commit history

### Expected Output

- Repository initialized successfully
- Three commits in history
- Each commit has a meaningful message

### Solution

<details>
<summary>Click to reveal solution</summary>

```bash
# Step 1: Create and enter directory
mkdir my-first-repo
cd my-first-repo

# Step 2: Initialize Git repository
git init
# Output: Initialized empty Git repository in /path/to/my-first-repo/.git/

# Step 3: Create first file and commit
echo "# My First Repository" > README.md
git add README.md
git commit -m "Initial commit: Add README"

# Step 4: Create second file and commit
echo "console.log('Hello Git!');" > script.js
git add script.js
git commit -m "Add JavaScript file"

# Step 5: Create third file and commit
echo "body { margin: 0; }" > style.css
git add style.css
git commit -m "Add CSS stylesheet"

# Step 6: View commit history
git log --oneline
# Output:
# abc1234 (HEAD -> main) Add CSS stylesheet
# def5678 Add JavaScript file
# ghi9012 Initial commit: Add README

# Verify all files are tracked
git status
# Output: On branch main, nothing to commit, working tree clean
```

**Verification**:
```bash
# Check that repository was created
ls -la .git
# Should see .git directory

# Check commit count
git log --oneline | wc -l
# Should output: 3

# Check all files are committed
git ls-files
# Should list: README.md, script.js, style.css
```

**Key Concepts**:
- `git init` creates a new repository
- Each commit should represent one logical change
- Commit messages should be descriptive
- Use `git log` to verify your work

</details>

---

## Challenge #2: Staging Control ⭐⭐

**Difficulty**: Intermediate  
**Time**: 20 minutes  
**Concepts**: Selective staging, git add, git diff, git status

### Problem Statement

Practice fine-grained control over what you commit by staging files selectively.

### Scenario

You've been working on multiple features:
- Updated `index.html` (ready to commit)
- Modified `app.js` (ready to commit)
- Changed `config.js` (NOT ready - still testing)
- Created `temp.txt` (should never be committed)

### Requirements

1. Create a repository with the four files
2. Make changes to all files
3. Create a `.gitignore` for `temp.txt`
4. Stage only `index.html` and `app.js`
5. Commit the staged files
6. Verify `config.js` is still modified
7. Verify `temp.txt` is ignored

### Solution

<details>
<summary>Click to reveal solution</summary>

```bash
# Step 1: Create repository and initial files
mkdir selective-staging
cd selective-staging
git init

# Create initial versions
echo "<!DOCTYPE html>" > index.html
echo "console.log('v1');" > app.js
echo "port=3000" > config.js
echo "temporary notes" > temp.txt

# Initial commit
git add index.html app.js config.js
git commit -m "Initial version"

# Step 2: Make changes to all files
echo "<html><body>Updated</body></html>" > index.html
echo "console.log('v2'); // Added feature" >> app.js
echo "port=8080" > config.js  # Changed but not ready
echo "more temp notes" >> temp.txt

# Step 3: Create .gitignore for temp.txt
echo "temp.txt" > .gitignore
git add .gitignore
git commit -m "Add .gitignore"

# Step 4: Check status
git status
# Shows: index.html, app.js, config.js modified
# temp.txt should NOT appear (it's ignored)

# Step 5: Stage only specific files
git add index.html app.js

# Step 6: Verify what's staged
git diff --staged
# Shows changes to index.html and app.js

# Step 7: Commit staged files
git commit -m "Update HTML and add feature to app.js"

# Step 8: Verify config.js is still modified
git status
# Shows: modified: config.js

# Step 9: Verify temp.txt is ignored
git status
# temp.txt should NOT appear in output

# View final state
git log --oneline
git status
```

**Expected Output**:
```
On branch main
Changes not staged for commit:
  modified:   config.js

nothing added to commit but untracked files present
```

**Key Concepts**:
- Use `.gitignore` to exclude files permanently
- `git add <file>` stages specific files
- `git diff --staged` shows what will be committed
- `git status` shows the current state
- Staged and unstaged changes can coexist

**Advanced**: Try `git add -p` for partial staging within a single file!

</details>

---

## Challenge #3: Commit History Master ⭐⭐

**Difficulty**: Intermediate  
**Time**: 25 minutes  
**Concepts**: git log variations, viewing history, finding commits

### Problem Statement

Create a repository with diverse commits and practice navigating the history using different `git log` options.

### Requirements

1. Create a repository with at least 10 commits
2. Include commits with different types of changes
3. Practice viewing history with:
   - `git log --oneline`
   - `git log -p` (show changes)
   - `git log --stat` (show file stats)
   - `git log --graph`
4. Find specific commits using grep
5. View commits from specific time periods

### Solution

<details>
<summary>Click to reveal solution</summary>

```bash
# Step 1: Create repository
mkdir history-practice
cd history-practice
git init

# Step 2: Create multiple commits (10 total)
echo "# Project" > README.md
git add README.md
git commit -m "docs: Add README"

mkdir src
echo "function main() {}" > src/main.js
git add src/
git commit -m "feat: Add main function"

echo "function helper() {}" >> src/main.js
git add src/main.js
git commit -m "feat: Add helper function"

echo "/* TODO: Add tests */" >> src/main.js
git add src/main.js
git commit -m "chore: Add TODO comment"

echo "body { margin: 0; }" > src/style.css
git add src/style.css
git commit -m "style: Add basic CSS"

echo "function validate() {}" >> src/main.js
git add src/main.js
git commit -m "feat: Add validation function"

echo "body { padding: 0; }" >> src/style.css
git add src/style.css
git commit -m "style: Update CSS padding"

echo "// Fix bug" >> src/main.js
git add src/main.js
git commit -m "fix: Resolve validation bug"

echo "## Installation" >> README.md
git add README.md
git commit -m "docs: Add installation section"

echo "function test() {}" > src/test.js
git add src/test.js
git commit -m "test: Add test file"

# Step 3: View history with different options

# Compact view
git log --oneline
# Shows: short hash + message

# Show changes in each commit
git log -p
# Shows: full diff for each commit

# Show file statistics
git log --stat
# Shows: which files changed and how many lines

# Show graph (useful with branches)
git log --graph --oneline --all
# Shows: ASCII graph of commits

# Last 5 commits
git log -5 --oneline

# Commits with "feat" in message
git log --oneline --grep="feat"
# Shows: only feature commits

# Commits by specific author
git config user.name  # See your name
git log --author="Your Name" --oneline

# Commits in last 24 hours
git log --since="1 day ago" --oneline

# Commits that modified specific file
git log --oneline -- src/main.js

# Pretty custom format
git log --pretty=format:"%h - %an, %ar : %s"
# Shows: hash - author, time ago : message

# Show commits with file changes
git log --name-status
# Shows: M (modified), A (added), D (deleted) before files

# Search for commits that changed specific content
git log -S "helper" --oneline
# Shows: commits that added or removed "helper"
```

**Practice Queries**:
```bash
# Find commit that added test.js
git log --diff-filter=A --oneline -- src/test.js

# Show commits that modified JavaScript files
git log --oneline -- "*.js"

# Show commits with extended description
git log --format=fuller

# Count commits per author
git shortlog -s -n

# Find commits between dates
git log --since="2024-01-01" --until="2024-01-07"

# Show only merge commits (if any)
git log --merges

# Show only non-merge commits
git log --no-merges
```

**Key Concepts**:
- `git log` has many powerful options
- Use `--oneline` for quick overview
- Use `-p` to see actual code changes
- Use `--grep` to find specific commits
- Use `--since` and `--until` for date ranges
- Use `-- <file>` to filter by file

**Pro Tips**:
```bash
# Create an alias for your favorite log format
git config --global alias.lg "log --graph --oneline --all --decorate"

# Now use it:
git lg
```

</details>

---

## Challenge #4: Undoing Mistakes ⭐⭐⭐

**Difficulty**: Advanced  
**Time**: 30 minutes  
**Concepts**: git restore, git commit --amend, undoing changes

### Problem Statement

Practice recovering from common Git mistakes without losing work.

### Scenarios

1. **Scenario A**: Staged wrong file - need to unstage
2. **Scenario B**: Made changes to file - want to discard
3. **Scenario C**: Committed too early - forgot to add a file
4. **Scenario D**: Committed with wrong message

### Solution

<details>
<summary>Click to reveal solution</summary>

```bash
# Setup
mkdir undo-practice
cd undo-practice
git init

echo "main content" > main.txt
git add main.txt
git commit -m "Add main file"

# ========================================
# SCENARIO A: Unstage a file
# ========================================

echo "feature 1" > feature.txt
echo "secret password" > secret.txt

# Oops! Accidentally staged secret.txt
git add feature.txt secret.txt

git status
# Both files staged

# Solution: Unstage secret.txt
git restore --staged secret.txt

git status
# feature.txt: staged
# secret.txt: not staged

# Commit only feature.txt
git commit -m "Add feature"

# ========================================
# SCENARIO B: Discard changes
# ========================================

echo "work in progress" >> main.txt
git status
# main.txt modified

# Decide you don't want these changes
git diff main.txt
# View changes

# Solution: Discard changes (⚠️ permanent!)
git restore main.txt

git status
# Working tree clean

cat main.txt
# Back to original "main content"

# ========================================
# SCENARIO C: Forgot to include file
# ========================================

echo "new feature" > feature2.txt
echo "related test" > feature2.test.txt

# Commit feature but forgot test
git add feature2.txt
git commit -m "Add feature 2"

git status
# feature2.test.txt not committed

# Solution: Amend the commit
git add feature2.test.txt
git commit --amend --no-edit

# Verify
git log --oneline -1
git show HEAD --name-only
# Shows both files in the commit

# ========================================
# SCENARIO D: Wrong commit message
# ========================================

echo "hotfix" > fix.txt
git add fix.txt
git commit -m "Add stuff"  # Oops! Bad message

# Solution: Amend with new message
git commit --amend -m "fix: Critical security hotfix"

git log --oneline -1
# Shows new message

# ========================================
# BONUS: Completely undo last commit
# ========================================

echo "mistake" > mistake.txt
git add mistake.txt
git commit -m "This is a mistake"

# Option 1: Undo commit, keep changes
git reset --soft HEAD~1
git status
# mistake.txt is staged

# Option 2: Undo commit and staging, keep file
git add mistake.txt
git commit -m "This is a mistake"
git reset HEAD~1
git status
# mistake.txt is not staged but exists

# Option 3: Completely remove commit and changes (⚠️ dangerous!)
git add mistake.txt
git commit -m "This is a mistake"
git reset --hard HEAD~1
git status
# mistake.txt is gone!
```

**Safety Tips**:
```bash
# Before discarding changes, view them
git diff

# Before reset --hard, create a backup branch
git branch backup-before-reset
git reset --hard HEAD~1
# If you mess up:
git reset --hard backup-before-reset

# Find "lost" commits with reflog
git reflog
# Shows all ref updates
# Can recover with: git reset --hard <commit-hash>
```

**Key Concepts**:
- `git restore --staged <file>` = unstage file
- `git restore <file>` = discard changes (⚠️ permanent!)
- `git commit --amend` = modify last commit
- `git reset --soft HEAD~1` = undo commit, keep changes staged
- `git reset HEAD~1` = undo commit and staging, keep changes
- `git reset --hard HEAD~1` = undo everything (⚠️ permanent!)

</details>

---

## Challenge #5: .gitignore Master ⭐⭐

**Difficulty**: Intermediate  
**Time**: 20 minutes  
**Concepts**: .gitignore patterns, preventing commits

### Problem Statement

Create a comprehensive `.gitignore` file for a web project with multiple types of files that should never be committed.

### Requirements

1. Create a project with these files:
   - Source files: `index.html`, `app.js`, `styles.css`
   - Build output: `dist/bundle.js`, `dist/bundle.css`
   - Dependencies: `node_modules/`
   - Environment: `.env`, `.env.local`
   - IDE: `.vscode/settings.json`
   - OS: `.DS_Store`, `Thumbs.db`
   - Logs: `error.log`, `debug.log`
2. Create `.gitignore` to exclude unnecessary files
3. Verify only source files are tracked

### Solution

<details>
<summary>Click to reveal solution</summary>

```bash
# Step 1: Create project structure
mkdir gitignore-practice
cd gitignore-practice
git init

# Create source files (should be committed)
echo "<html></html>" > index.html
echo "console.log('app');" > app.js
echo "body {}" > styles.css

# Create files that should NOT be committed
mkdir dist node_modules .vscode
echo "bundled code" > dist/bundle.js
echo "bundled styles" > dist/bundle.css
echo "dependency" > node_modules/package.json
echo "API_KEY=secret123" > .env
echo "DEBUG=true" > .env.local
echo '{"editor.fontSize": 14}' > .vscode/settings.json
echo "Mac metadata" > .DS_Store
echo "Windows metadata" > Thumbs.db
echo "ERROR: Something broke" > error.log
echo "DEBUG: Info" > debug.log

# Step 2: Create comprehensive .gitignore
cat > .gitignore << 'EOF'
# Dependencies
node_modules/
bower_components/
vendor/

# Build outputs
dist/
build/
out/
*.bundle.js
*.bundle.css

# Environment variables
.env
.env.local
.env.*.local

# IDE files
.vscode/
.idea/
*.sublime-project
*.sublime-workspace

# OS files
.DS_Store
Thumbs.db
*.swp
*.swo
*~

# Logs
*.log
logs/
npm-debug.log*

# Test coverage
coverage/
.nyc_output/

# Temporary files
*.tmp
temp/
.cache/
EOF

# Step 3: Add .gitignore first
git add .gitignore
git commit -m "Add .gitignore"

# Step 4: Add source files
git add index.html app.js styles.css
git commit -m "Add source files"

# Step 5: Verify correct files are tracked
git status
# Should show: "nothing to commit, working tree clean"

git ls-files
# Should only list:
# .gitignore
# app.js
# index.html
# styles.css

# Step 6: Verify ignored files don't show up
git status --ignored
# Shows all ignored files

# Test: Try to add an ignored file
git add dist/bundle.js
# Output: The following paths are ignored by one of your .gitignore files
```

**Additional .gitignore Patterns**:
```bash
# Ignore all .txt files
*.txt

# Except this one
!important.txt

# Ignore .txt files only in this directory
/*.txt

# Ignore .pdf files in all directories
**/*.pdf

# Ignore entire directory
temp/

# Ignore files matching pattern
backup_*
*_backup

# Ignore files with numbers
file[0-9].txt
```

**Debugging .gitignore**:
```bash
# Check if file is ignored
git check-ignore -v file.txt
# Shows which .gitignore rule matches

# List all ignored files
git status --ignored

# Force add an ignored file (not recommended)
git add -f ignored-file.txt
```

**Key Concepts**:
- Add `.gitignore` before adding other files
- Use patterns to match multiple files
- Commented lines start with `#`
- `/` at start = only this directory
- `/` at end = directory
- `*` = wildcard
- `**` = recursive wildcard
- `!` = exception (don't ignore)

</details>

---

## Challenge #6: Complete Project Workflow ⭐⭐⭐

**Difficulty**: Advanced  
**Time**: 45 minutes  
**Concepts**: Complete Git workflow from start to finish

### Problem Statement

Simulate a realistic development workflow for a small web project, demonstrating all Git basics concepts.

### Requirements

1. Initialize repository with proper structure
2. Create `.gitignore` before any commits
3. Make at least 8 commits with good messages
4. Practice staging selectively
5. Use `git log` to review history
6. Demonstrate undoing mistakes
7. Create meaningful commit history

### Project

Build a simple todo list website with:
- `index.html` - Main page
- `script.js` - JavaScript functionality
- `styles.css` - Styling
- `README.md` - Documentation

### Solution

<details>
<summary>Click to reveal solution</summary>

```bash
# ==========================================
# PHASE 1: Project Initialization
# ==========================================

mkdir todo-app
cd todo-app
git init

# Configure for this project
git config user.name "Your Name"
git config user.email "your@email.com"

# Create .gitignore first
cat > .gitignore << 'EOF'
# Development
node_modules/
.env
.DS_Store
*.log
EOF

git add .gitignore
git commit -m "chore: Initialize project with .gitignore"

# ==========================================
# PHASE 2: Initial Setup
# ==========================================

# Create README
cat > README.md << 'EOF'
# Todo List Application

A simple todo list web application.

## Features
- Add todos
- Mark as complete
- Delete todos
EOF

git add README.md
git commit -m "docs: Add README with project description"

# ==========================================
# PHASE 3: HTML Structure
# ==========================================

cat > index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Todo List</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>My Todo List</h1>
    <div id="app"></div>
    <script src="script.js"></script>
</body>
</html>
EOF

git add index.html
git commit -m "feat: Add basic HTML structure"

# ==========================================
# PHASE 4: Styling
# ==========================================

cat > styles.css << 'EOF'
body {
    font-family: Arial, sans-serif;
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
}

h1 {
    color: #333;
    text-align: center;
}
EOF

git add styles.css
git commit -m "style: Add basic CSS styling"

# ==========================================
# PHASE 5: JavaScript Functionality
# ==========================================

cat > script.js << 'EOF'
// Todo list array
let todos = [];

// Add todo function
function addTodo(text) {
    todos.push({
        id: Date.now(),
        text: text,
        completed: false
    });
}
EOF

git add script.js
git commit -m "feat: Add todo data structure and addTodo function"

# ==========================================
# PHASE 6: More Features (Selective Staging)
# ==========================================

# Add multiple features
cat >> script.js << 'EOF'

// Mark todo as complete
function completeTodo(id) {
    const todo = todos.find(t => t.id === id);
    if (todo) todo.completed = true;
}

// Delete todo
function deleteTodo(id) {
    todos = todos.filter(t => t.id !== id);
}
EOF

cat >> styles.css << 'EOF'

.todo-item {
    padding: 10px;
    margin: 5px 0;
    border: 1px solid #ddd;
}

.completed {
    text-decoration: line-through;
    opacity: 0.6;
}
EOF

# Commit JavaScript separately from CSS
git add script.js
git commit -m "feat: Add complete and delete todo functions"

git add styles.css
git commit -m "style: Add todo item styles"

# ==========================================
# PHASE 7: Documentation Update
# ==========================================

cat >> README.md << 'EOF'

## Usage
1. Open index.html in a browser
2. Add todos using the input field
3. Click to mark as complete
4. Delete unwanted todos

## Development
- Pure JavaScript (no frameworks)
- Responsive CSS
- Local storage coming soon
EOF

git add README.md
git commit -m "docs: Add usage instructions to README"

# ==========================================
# PHASE 8: Fixing a Mistake
# ==========================================

# Oops! Committed with wrong message
echo "// TODO: Add local storage" >> script.js
git add script.js
git commit -m "stuff"  # Bad message!

# Fix the message
git commit --amend -m "chore: Add TODO comment for local storage"

# ==========================================
# PHASE 9: Review Your Work
# ==========================================

# View commit history
echo "\n=== Commit History ==="
git log --oneline

# View project status
echo "\n=== Project Status ==="
git status

# List tracked files
echo "\n=== Tracked Files ==="
git ls-files

# View file changes over time
echo "\n=== Changes to script.js ==="
git log --oneline -- script.js

# Show statistics
echo "\n=== Project Statistics ==="
git log --stat

# View last commit in detail
echo "\n=== Last Commit Details ==="
git show HEAD

# ==========================================
# PHASE 10: Create Release Tag
# ==========================================

git tag -a v1.0.0 -m "Initial release"
git tag

echo "\n=== Project Complete! ==="
echo "Total commits: $(git log --oneline | wc -l)"
echo "Files tracked: $(git ls-files | wc -l)"
```

**Expected Final State**:
```bash
# Commit history should look like:
abc1234 (HEAD -> main, tag: v1.0.0) chore: Add TODO comment for local storage
def5678 docs: Add usage instructions to README
ghi9012 style: Add todo item styles
jkl3456 feat: Add complete and delete todo functions
mno7890 style: Add basic CSS styling
pqr1234 feat: Add basic HTML structure
stu5678 docs: Add README with project description
vwx9012 chore: Initialize project with .gitignore
```

**Verification Checklist**:
- [ ] Repository initialized
- [ ] .gitignore created first
- [ ] At least 8 meaningful commits
- [ ] Good commit messages (type: description)
- [ ] Selective staging used
- [ ] Mistake corrected with --amend
- [ ] All source files tracked
- [ ] No unwanted files committed
- [ ] Can view complete history
- [ ] Project is well-documented

</details>

---

## Progress Tracking

- [ ] Challenge #1: First Repository
- [ ] Challenge #2: Staging Control
- [ ] Challenge #3: Commit History Master
- [ ] Challenge #4: Undoing Mistakes
- [ ] Challenge #5: .gitignore Master
- [ ] Challenge #6: Complete Project Workflow

---

## Next Steps

After completing these challenges:

1. **Review**: Compare your approach with the solutions
2. **Experiment**: Try variations of the commands
3. **Practice**: Use Git for all your projects
4. **Advance**: Move to [02_Branching_and_Merging](../02_Branching_and_Merging/)
5. **Share**: Help others learn Git

---

**Happy Coding!** 🚀🔄
