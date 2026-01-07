# Best Practices Quiz 📝

**Topic**: Git and GitHub Best Practices  
**Difficulty**: ⭐⭐ Intermediate  
**Time**: ~20 minutes

---

## Section 1: Commit Messages

### Question 1 (⭐ Beginner)
**Which commit message follows best practices?**

A) `Update`  
B) `Add user authentication with JWT tokens`  
C) `Fixed stuff`  
D) `changes`

<details>
<summary>Click to reveal answer</summary>

**Answer: B - Add user authentication with JWT tokens**

**Explanation**: Good commit messages are clear, descriptive, use imperative mood, and explain what changed.

</details>

---

### Question 2 (⭐⭐ Intermediate)
**What is the Conventional Commits format?**

A) `<description>: <type>`  
B) `<type>(<scope>): <description>`  
C) `<date>: <message>`  
D) Any format is fine

<details>
<summary>Click to reveal answer</summary>

**Answer: B - `<type>(<scope>): <description>`**

**Explanation**: Conventional Commits use format like `feat(auth): Add login functionality` where type indicates kind of change, scope is optional context, and description explains the change.

</details>

---

## Section 2: Branch Naming

### Question 3 (⭐ Beginner)
**Which branch name follows best practices?**

A) `test`  
B) `feature/user-authentication`  
C) `johns_branch`  
D) `temp`

<details>
<summary>Click to reveal answer</summary>

**Answer: B - feature/user-authentication**

**Explanation**: Good branch names use prefixes (feature/, bugfix/, etc.) and are descriptive, lowercase with hyphens.

</details>

---

## Section 3: Workflows

### Question 4 (⭐⭐ Intermediate)
**What is GitHub Flow?**

A) A complex workflow with many branches  
B) A simple workflow: branch from main, PR, merge, deploy  
C) GitHub's internal development process  
D) The same as Git Flow

<details>
<summary>Click to reveal answer</summary>

**Answer: B - A simple workflow: branch from main, PR, merge, deploy**

**Explanation**: GitHub Flow is simple: main is always deployable, create branches for work, use PRs for review, merge and deploy immediately.

</details>

---

### Question 5 (⭐⭐ Intermediate)
**When should you use Git Flow instead of GitHub Flow?**

A) Never, GitHub Flow is always better  
B) When you have scheduled releases and multiple production versions  
C) When you have a small team  
D) For web applications only

<details>
<summary>Click to reveal answer</summary>

**Answer: B - When you have scheduled releases and multiple production versions**

**Explanation**: Git Flow is better for scheduled releases, desktop software, or when you need to maintain multiple versions in production.

</details>

---

## Section 4: .gitignore

### Question 6 (⭐ Beginner)
**What should ALWAYS be in your .gitignore?**

A) Source code files  
B) README.md  
C) Environment variables and secrets (.env, *.key)  
D) All JavaScript files

<details>
<summary>Click to reveal answer</summary>

**Answer: C - Environment variables and secrets (.env, *.key)**

**Explanation**: Never commit secrets, API keys, passwords, or private keys. Always add them to .gitignore.

</details>

---

## Section 5: Code Review

### Question 7 (⭐⭐ Intermediate)
**What's a good size for a Pull Request?**

A) As large as possible to reduce number of PRs  
B) Small and focused, ideally under 400 lines  
C) Must be exactly 100 lines  
D) Size doesn't matter

<details>
<summary>Click to reveal answer</summary>

**Answer: B - Small and focused, ideally under 400 lines**

**Explanation**: Small PRs are easier to review, faster to merge, less likely to have bugs, and easier to revert if needed.

</details>

---

### Question 8 (⭐⭐ Intermediate)
**How should you provide code review feedback?**

A) Point out only what's wrong  
B) Be constructive, explain why, and praise good code  
C) Just say "looks good" on everything  
D) Focus on code style preferences

<details>
<summary>Click to reveal answer</summary>

**Answer: B - Be constructive, explain why, and praise good code**

**Explanation**: Good code reviews are educational, kind, specific, and balanced. They improve code while maintaining team morale.

</details>

---

## Section 6: Git Hooks

### Question 9 (⭐⭐ Intermediate)
**What are Git hooks?**

A) Physical hooks for your computer  
B) Scripts that run automatically on Git events  
C) GitHub features  
D) Commands to hook branches together

<details>
<summary>Click to reveal answer</summary>

**Answer: B - Scripts that run automatically on Git events**

**Explanation**: Git hooks are scripts (pre-commit, pre-push, etc.) that run automatically to enforce quality checks, run tests, or validate commit messages.

</details>

---

## Section 7: Security

### Question 10 (⭐ Beginner)
**How should you store API keys and secrets?**

A) Commit them directly in code  
B) Use environment variables and .env files (in .gitignore)  
C) Put them in README.md  
D) Email them to team members

<details>
<summary>Click to reveal answer</summary>

**Answer: B - Use environment variables and .env files (in .gitignore)**

**Explanation**: Store secrets in .env files (which are in .gitignore), use environment variables in code, and provide .env.example as a template.

</details>

---

## Key Takeaways

✅ **Write clear, descriptive commit messages**  
✅ **Use conventional commits format**  
✅ **Name branches with prefixes and descriptive names**  
✅ **Choose workflow that fits your team**  
✅ **Never commit secrets**  
✅ **Keep PRs small and focused**  
✅ **Be constructive in code reviews**  
✅ **Use Git hooks for automation**  
✅ **Document your project well**  

---

**Happy Professional Git Usage!** ✨
