# Advanced Git Quiz 📝

**Topic**: Advanced Git Commands and Techniques  
**Difficulty**: ⭐⭐⭐ Advanced  
**Time**: ~25 minutes

---

## Section 1: Rebase

### Question 1 (⭐⭐ Intermediate)
**What is the main difference between merge and rebase?**

A) They do the same thing  
B) Merge creates a merge commit; rebase creates a linear history  
C) Rebase is faster than merge  
D) Merge changes commit hashes but rebase doesn't

<details>
<summary>Click to reveal answer</summary>

**Answer: B - Merge creates a merge commit; rebase creates a linear history**

**Explanation**: Merge preserves exact history with a merge commit. Rebase rewrites commits to create a linear history without merge commits.

</details>

---

### Question 2 (⭐⭐⭐ Advanced)
**What is the "Golden Rule" of rebasing?**

A) Always rebase instead of merge  
B) Never rebase public/shared branches  
C) Only rebase on Fridays  
D) Rebase everything for clean history

<details>
<summary>Click to reveal answer</summary>

**Answer: B - Never rebase public/shared branches**

**Explanation**: Rebasing changes commit hashes. If others have those commits, they'll have serious conflicts. Only rebase local branches that haven't been shared.

</details>

---

## Section 2: Cherry-Pick

### Question 3 (⭐⭐ Intermediate)
**What does `git cherry-pick` do?**

A) Deletes a commit  
B) Applies a specific commit to the current branch  
C) Picks the best commits automatically  
D) Merges a branch

<details>
<summary>Click to reveal answer</summary>

**Answer: B - Applies a specific commit to the current branch**

**Explanation**: Cherry-pick allows you to apply a single commit from one branch to another without merging the entire branch.

</details>

---

## Section 3: Stash

### Question 4 (⭐ Beginner)
**When would you use `git stash`?**

A) To permanently delete changes  
B) To temporarily save uncommitted work  
C) To create a new branch  
D) To push to remote

<details>
<summary>Click to reveal answer</summary>

**Answer: B - To temporarily save uncommitted work**

**Explanation**: Stash saves your uncommitted changes without creating a commit, allowing you to switch branches or pull updates cleanly.

</details>

---

### Question 5 (⭐⭐ Intermediate)
**What's the difference between `git stash apply` and `git stash pop`?**

A) They're the same  
B) Apply keeps the stash; pop removes it after applying  
C) Pop is faster  
D) Apply works on all stashes; pop only on the latest

<details>
<summary>Click to reveal answer</summary>

**Answer: B - Apply keeps the stash; pop removes it after applying**

**Explanation**: `apply` reapplies stashed changes but keeps them in the stash list. `pop` applies and removes the stash in one command.

</details>

---

## Section 4: Reset

### Question 6 (⭐⭐⭐ Advanced)
**What does `git reset --hard HEAD~3` do?**

A) Undoes last 3 commits, keeps changes  
B) Creates 3 new commits  
C) Undoes last 3 commits and DISCARDS all changes permanently  
D) Just unstages files

<details>
<summary>Click to reveal answer</summary>

**Answer: C - Undoes last 3 commits and DISCARDS all changes permanently**

**Explanation**: `--hard` is destructive! It moves HEAD back 3 commits and permanently deletes those changes from working directory. Use with extreme caution!

</details>

---

### Question 7 (⭐⭐ Intermediate)
**What's the difference between the three reset modes?**

A) They're all the same  
B) --soft keeps changes staged; --mixed unstages; --hard discards all  
C) They work on different branches  
D) Only the speed differs

<details>
<summary>Click to reveal answer</summary>

**Answer: B - --soft keeps changes staged; --mixed unstages; --hard discards all**

**Explanation**: 
- `--soft`: Moves HEAD, keeps changes staged
- `--mixed`: Moves HEAD, unstages changes (default)
- `--hard`: Moves HEAD, discards all changes ⚠️

</details>

---

## Section 5: Revert

### Question 8 (⭐⭐ Intermediate)
**When should you use `git revert` instead of `git reset`?**

A) Never, reset is always better  
B) When undoing commits that have been pushed/shared  
C) Only for merge commits  
D) When you want faster undoing

<details>
<summary>Click to reveal answer</summary>

**Answer: B - When undoing commits that have been pushed/shared**

**Explanation**: Revert creates a new commit that undoes changes, preserving history. It's safe for public branches. Reset rewrites history and shouldn't be used on shared commits.

</details>

---

## Section 6: Reflog

### Question 9 (⭐⭐⭐ Advanced)
**What is `git reflog` used for?**

A) To see repository files  
B) To track all HEAD movements and recover "lost" commits  
C) To show current branch  
D) To log into Git

<details>
<summary>Click to reveal answer</summary>

**Answer: B - To track all HEAD movements and recover "lost" commits**

**Explanation**: Reflog records every HEAD movement, allowing you to recover commits from deleted branches, hard resets, or other "accidents". It's your safety net!

</details>

---

## Section 7: Tags

### Question 10 (⭐ Beginner)
**What are Git tags typically used for?**

A) To tag people in commits  
B) To mark release points and important commits  
C) To create branches  
D) To delete commits

<details>
<summary>Click to reveal answer</summary>

**Answer: B - To mark release points and important commits**

**Explanation**: Tags are permanent markers for specific commits, typically used to mark version releases (v1.0.0, v2.0.0, etc.).

</details>

---

## Key Takeaways

✅ **Never rebase public branches**  
✅ **Use revert for shared commits**  
✅ **Reset --hard is destructive**  
✅ **Stash temporarily saves work**  
✅ **Cherry-pick applies specific commits**  
✅ **Reflog can recover lost commits**  
✅ **Tags mark important releases**  

---

**Happy Advanced Git Usage!** 🚀
