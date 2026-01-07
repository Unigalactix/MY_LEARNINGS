# Git Basics Quiz 📝

**Topic**: Git Fundamentals and Basic Commands  
**Difficulty**: ⭐ Beginner  
**Time**: ~20 minutes

**Instructions**: 
- Try to answer all questions before checking the answers
- Focus on understanding core Git concepts
- Practice commands after taking the quiz

---

## Section 1: Core Concepts

### Question 1 (⭐ Beginner)
**What is Git?**

A) A programming language  
B) A distributed version control system  
C) A code editor  
D) A cloud storage service

<details>
<summary>Click to reveal answer</summary>

**Answer: B - A distributed version control system**

**Explanation**: 
Git is a distributed version control system (VCS) that tracks changes in files and enables collaboration. It was created by Linus Torvalds in 2005 and has become the industry standard for version control.

**Key characteristics**:
- **Distributed**: Every developer has a full copy of the repository
- **Version Control**: Tracks all changes over time
- **Collaboration**: Multiple people can work on the same project
- **History**: Complete record of who changed what and when

**What Git is NOT**:
- Not GitHub (GitHub is a hosting service for Git repositories)
- Not a backup service (though it provides backup benefits)
- Not a programming language
- Not a cloud storage like Dropbox

**Real-world analogy**:
Think of Git as a time machine for your code. You can:
- Save snapshots (commits) at any point
- Go back to any previous version
- See who made what changes
- Try new ideas without breaking working code

</details>

---

### Question 2 (⭐ Beginner)
**What are the three states of a file in Git?**

A) Draft, Published, Archived  
B) Modified, Staged, Committed  
C) Created, Updated, Deleted  
D) Local, Remote, Shared

<details>
<summary>Click to reveal answer</summary>

**Answer: B - Modified, Staged, Committed**

**Explanation**: 
In Git, every file exists in one of three states as it moves through your workflow:

**1. Modified (Working Directory)**:
- You've changed the file but haven't saved it to Git yet
- Git sees the changes but they're not tracked
- Use `git diff` to see what changed

```bash
# Edit file
echo "new line" >> file.txt

# File is now modified
git status  # Shows: modified: file.txt
```

**2. Staged (Staging Area/Index)**:
- You've marked the file to be included in the next commit
- Changes are ready but not yet saved permanently
- Use `git diff --staged` to see what's staged

```bash
# Stage the file
git add file.txt

# File is now staged
git status  # Shows: Changes to be committed
```

**3. Committed (Repository)**:
- Changes are safely stored in Git's database
- File is now part of the repository history
- Use `git log` to see commit history

```bash
# Commit the file
git commit -m "Add new line to file"

# File is now committed
git log  # Shows the commit
```

**The Workflow**:
```
Working Directory  →  Staging Area  →  Repository
   (Modified)          (Staged)        (Committed)
      ↓                   ↓                ↓
   Edit files         git add          git commit
```

**Why three states?**
- Allows you to group related changes together
- Gives you control over what goes in each commit
- Lets you review changes before committing

</details>

---

## Section 2: Basic Commands

### Question 3 (⭐ Beginner)
**Which command initializes a new Git repository?**

A) `git start`  
B) `git new`  
C) `git init`  
D) `git create`

<details>
<summary>Click to reveal answer</summary>

**Answer: C - `git init`**

**Explanation**: 
The `git init` command creates a new Git repository in the current directory. It's the first command you run when starting a new project with Git.

**What `git init` does**:
```bash
# Navigate to your project directory
cd my-project

# Initialize Git repository
git init

# What happens:
# 1. Creates a .git folder (hidden directory)
# 2. Sets up Git database and configuration
# 3. Makes the directory a Git repository
```

**After running `git init`**:
```bash
# Check that .git folder exists
ls -la
# You'll see: .git/

# Check Git status
git status
# Output: On branch main (or master)
#         No commits yet
```

**Important notes**:
- Only run `git init` once per project
- The .git folder contains all Git data - don't delete it!
- You can now use all Git commands in this directory
- Nothing is committed yet - repository is empty

**Example workflow**:
```bash
# Create new project
mkdir my-website
cd my-website

# Initialize Git
git init
# Output: Initialized empty Git repository in /path/to/my-website/.git/

# Create files
echo "# My Website" > README.md

# Stage and commit
git add README.md
git commit -m "Initial commit"
```

</details>

---

### Question 4 (⭐⭐ Intermediate)
**What's the difference between `git add .` and `git add -u`?**

A) No difference  
B) `.` adds all files including new ones, `-u` only adds modified tracked files  
C) `.` is faster than `-u`  
D) `-u` uploads files to server, `.` doesn't

<details>
<summary>Click to reveal answer</summary>

**Answer: B - `.` adds all files including new ones, `-u` only adds modified tracked files**

**Explanation**: 
These commands stage files differently:

**`git add .` (Add all)**:
- Stages ALL changes in current directory
- Includes new (untracked) files
- Includes modified files
- Includes deleted files

```bash
# Scenario
# Created: new-file.txt
# Modified: existing-file.txt
# Deleted: old-file.txt

git add .
# Stages: new-file.txt, existing-file.txt, deletion of old-file.txt
```

**`git add -u` (Add updated)**:
- Stages only TRACKED files that were modified or deleted
- Does NOT stage new (untracked) files
- `-u` stands for "update"

```bash
# Same scenario
git add -u
# Stages: existing-file.txt, deletion of old-file.txt
# Does NOT stage: new-file.txt (because it's new/untracked)
```

**Comparison table**:
| File Status | `git add .` | `git add -u` |
|------------|-------------|--------------|
| New file (untracked) | ✅ Staged | ❌ Not staged |
| Modified file | ✅ Staged | ✅ Staged |
| Deleted file | ✅ Staged | ✅ Staged |

**When to use each**:

**Use `git add .` when**:
- Starting a new project and want to add everything
- You want to include new files in your commit
- You're sure all changes should be committed

**Use `git add -u` when**:
- You have new files you don't want to commit yet
- You only want to commit updates to existing files
- You want to be more selective

**Example**:
```bash
# Create files for testing
echo "existing" > tracked.txt
git add tracked.txt
git commit -m "Add tracked file"

# Make changes
echo "modified" > tracked.txt
echo "new" > untracked.txt
rm tracked.txt  # Delete a file

# Compare results
git add -u
git status
# Shows: tracked.txt modified and deleted
# Does NOT show: untracked.txt

git reset  # Unstage

git add .
git status
# Shows: ALL changes including untracked.txt
```

**Pro tip**:
```bash
# Add all files including new ones
git add .

# Add only modified/deleted tracked files
git add -u

# Add specific file
git add filename.txt

# Add all files of certain type
git add *.js
```

</details>

---

## Section 3: Viewing History

### Question 5 (⭐⭐ Intermediate)
**What does `git log --oneline` do?**

A) Shows only the first line of each commit message  
B) Shows a compact one-line summary of each commit  
C) Shows commits made today  
D) Shows only merge commits

<details>
<summary>Click to reveal answer</summary>

**Answer: B - Shows a compact one-line summary of each commit**

**Explanation**: 
The `--oneline` flag formats git log output to show each commit on a single line, making it easier to scan through history.

**Regular `git log`**:
```bash
git log

# Output (verbose):
commit 1a2b3c4d5e6f7g8h9i0j (HEAD -> main)
Author: John Doe <john@example.com>
Date:   Mon Jan 7 10:30:00 2024 -0500

    Add user authentication feature
    
    This commit adds login functionality
    with password hashing and JWT tokens.

commit 9z8y7x6w5v4u3t2s1r0q
Author: John Doe <john@example.com>
Date:   Mon Jan 7 09:15:00 2024 -0500

    Initial commit
```

**With `git log --oneline`**:
```bash
git log --oneline

# Output (compact):
1a2b3c4 (HEAD -> main) Add user authentication feature
9z8y7x6 Initial commit
```

**What you see in oneline format**:
- **Short commit hash** (first 7 characters): `1a2b3c4`
- **Branch pointer** (if applicable): `(HEAD -> main)`
- **Commit message** (first line only): `Add user authentication feature`

**Useful variations**:
```bash
# Oneline with graph (shows branches)
git log --oneline --graph
# Output:
# * 1a2b3c4 (HEAD -> main) Add user authentication
# * 9z8y7x6 Initial commit

# Oneline for last 5 commits
git log --oneline -5

# Oneline for specific branch
git log --oneline feature-branch

# Oneline with all branches
git log --oneline --all

# Oneline with dates
git log --oneline --date=short

# Pretty format (custom)
git log --pretty=format:"%h - %s (%cr)"
# 1a2b3c4 - Add user authentication (2 hours ago)
```

**Why use --oneline?**
- **Quick overview**: See many commits at once
- **Easy scanning**: Find commits faster
- **Less clutter**: Focus on what matters
- **Better for scripts**: Easier to parse programmatically

**Real-world usage**:
```bash
# Find recent work
git log --oneline -10

# See branch history
git log --oneline --graph --all

# Find specific commit
git log --oneline | grep "authentication"

# Check what you did today
git log --oneline --since="today"

# Compare branches
git log --oneline main..feature-branch
```

</details>

---

## Section 4: Staging and Committing

### Question 6 (⭐⭐ Intermediate)
**What does the staging area (index) allow you to do?**

A) Compile your code before committing  
B) Choose exactly which changes to include in the next commit  
C) Upload files to the internet  
D) Create backups automatically

<details>
<summary>Click to reveal answer</summary>

**Answer: B - Choose exactly which changes to include in the next commit**

**Explanation**: 
The staging area (also called the index) is one of Git's most powerful features. It sits between your working directory and the repository, giving you fine-grained control over your commits.

**Why the staging area exists**:
Without staging, you'd have to commit ALL changes at once. With staging, you can:
- Group related changes together
- Create logical, atomic commits
- Review changes before committing
- Exclude certain files from commits

**Example scenario**:
```bash
# You've been working and modified 5 files:
# - user.js (authentication feature)
# - user.css (styling for auth)
# - admin.js (admin panel bug fix)
# - admin.css (admin panel styling)
# - README.md (documentation update)

git status
# Shows all 5 files as modified

# You want separate commits for:
# 1. Authentication feature
# 2. Admin bug fix  
# 3. Documentation

# Commit 1: Stage only auth-related files
git add user.js user.css
git commit -m "Add user authentication feature"

# Commit 2: Stage only admin-related files
git add admin.js admin.css
git commit -m "Fix admin panel bug"

# Commit 3: Stage documentation
git add README.md
git commit -m "Update README with auth instructions"
```

**The staging workflow**:
```
Working Directory         Staging Area           Repository
(Modified files)       (Ready to commit)      (Committed)
      |                       |                    |
      |---> git add -------->|                    |
      |                       |                    |
      |                       |---> git commit -->|
      |                       |                    |
      |<--- git restore -----|                    |
      |                       |                    |
```

**Practical benefits**:
```bash
# 1. Review before committing
git add file.js
git diff --staged  # See exactly what will be committed

# 2. Partial staging (add only some changes in a file)
git add -p file.js  # Interactive staging
# Choose which hunks (sections) to stage

# 3. Unstage if you change your mind
git restore --staged file.js

# 4. Stage everything except certain files
git add .
git restore --staged sensitive-data.txt
```

**Real-world example**:
```bash
# Morning work session - you:
# - Fixed bug in payment.js
# - Updated tests in payment.test.js
# - Added logging (scattered across multiple files)
# - Accidentally modified config.js

# Commit the bug fix separately
git add payment.js payment.test.js
git commit -m "fix: Resolve payment calculation bug"

# Later commit the logging (after review)
git add src/logger.js src/services/*.js
git commit -m "feat: Add detailed logging system"

# Don't commit config.js yet (needs review)
git restore config.js
```

**Without staging area**:
You'd have to commit everything together or manually save/restore files - messy and error-prone!

</details>

---

## Section 5: Practical Scenarios

### Question 7 (⭐⭐⭐ Advanced)
**You committed a file with sensitive data (like a password). What should you do?**

A) Delete the file and commit again  
B) Use `git commit --amend` to modify the commit  
C) Both A and B, plus review .gitignore  
D) Nothing, Git encrypts all data

<details>
<summary>Click to reveal answer</summary>

**Answer: C - Both A and B, plus review .gitignore**

**Explanation**: 
This is a critical security situation that requires immediate action. Once data is committed, it's in Git history forever (unless you rewrite history).

**Immediate steps**:

**Step 1: Remove the sensitive file**
```bash
# Delete the file
rm sensitive-data.txt

# OR remove just the sensitive content
# (edit the file to remove passwords/keys)
```

**Step 2: Add to .gitignore**
```bash
# Prevent future commits
echo "sensitive-data.txt" >> .gitignore
echo "*.env" >> .gitignore
echo "secrets/" >> .gitignore
```

**Step 3: If this was your last commit (not pushed yet)**
```bash
# Amend the commit to remove the file
git add .gitignore
git rm --cached sensitive-data.txt  # Remove from Git but keep local copy
git commit --amend -m "Initial commit (removed sensitive data)"
```

**Step 4: If you already pushed OR it's not the last commit**
```bash
# ⚠️ This rewrites history - coordinate with team!

# Option A: Interactive rebase (if within last few commits)
git rebase -i HEAD~3  # Go back 3 commits
# Mark the bad commit as "edit"
# Remove the sensitive file
# Continue rebase

# Option B: Use git filter-branch (for older commits)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch sensitive-data.txt" \
  --prune-empty --tag-name-filter cat -- --all

# Option C: Use BFG Repo-Cleaner (easier tool)
# Download from: https://rtyley.github.io/bfg-repo-cleaner/
java -jar bfg.jar --delete-files sensitive-data.txt

# Force push (⚠️ dangerous!)
git push --force
```

**Step 5: Rotate credentials**
```bash
# Most important: Change the exposed passwords/keys!
# - Change passwords
# - Regenerate API keys
# - Rotate secrets
# - Revoke access tokens
```

**Prevention strategies**:

**1. Use .gitignore from the start**
```bash
# Create .gitignore before first commit
cat > .gitignore << EOF
# Environment variables
.env
.env.local
.env.*.local

# Credentials
secrets.json
credentials.yml
*.key
*.pem

# IDE config (might contain passwords)
.vscode/settings.json
.idea/

# OS files
.DS_Store
Thumbs.db
EOF
```

**2. Use environment variables**
```javascript
// Bad ❌
const API_KEY = "sk-1234567890abcdef";

// Good ✅
const API_KEY = process.env.API_KEY;
```

**3. Use git hooks to prevent commits**
```bash
# .git/hooks/pre-commit
#!/bin/bash
if git diff --cached | grep -i "password.*=.*['\"]"; then
    echo "ERROR: Possible password in commit!"
    exit 1
fi
```

**4. Use secret scanning tools**
```bash
# Install git-secrets
brew install git-secrets  # macOS
# or download from: https://github.com/awslabs/git-secrets

# Set up
git secrets --install
git secrets --register-aws  # Add AWS patterns
```

**Remember**:
- Git history is permanent by design
- Rewriting history is dangerous on shared repositories
- Always review `git diff --staged` before committing
- Use pre-commit hooks to catch secrets
- Rotate credentials immediately if exposed

</details>

---

## Scoring Guide

**Total Questions**: 7

- **6-7 correct (86-100%)**: Excellent! Git basics mastered! 🎉
- **4-5 correct (57-71%)**: Good! Review specific concepts. 👍
- **2-3 correct (29-43%)**: Keep practicing! 📚
- **0-1 correct (0-14%)**: Review the notes thoroughly. 💪

---

## Practice Exercises

Try these exercises to solidify your knowledge:

1. Create a new repository and make 5 commits
2. Use `git log` with different options
3. Practice staging only specific files
4. Create and use a `.gitignore` file
5. Amend a commit to add a forgotten file

---

## Next Steps

### If you scored well (75%+):
- ✅ Move to [02_Branching_and_Merging](../02_Branching_and_Merging/)
- ✅ Complete [Coding Challenges](./CHALLENGES.md)
- ✅ Practice with real projects

### If you need more practice:
- 📖 Review [notes.md](./notes.md)
- 💻 Practice commands in a test repository
- 🔄 Retake this quiz
- 🎮 Try [Learn Git Branching](https://learngitbranching.js.org/)

---

## Related Materials

- [notes.md](./notes.md) - Comprehensive Git basics guide
- [CHALLENGES.md](./CHALLENGES.md) - Hands-on coding challenges
- [Git Documentation](https://git-scm.com/doc) - Official docs

---

**Keep practicing!** 🚀🔄
