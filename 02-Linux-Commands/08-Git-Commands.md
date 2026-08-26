# Linux Commands Notes
## Part 8 - Git Commands (351-400)

---

# 351. git --version
## Description
Display the installed Git version.

```bash
git --version
```

---

# 352. git config --global user.name
## Description
Set the global Git username.

```bash
git config --global user.name "Abhishek Chouhan"
```

---

# 353. git config --global user.email
## Description
Set the global Git email.

```bash
git config --global user.email "example@gmail.com"
```

---

# 354. git config --list
## Description
Display all Git configuration settings.

```bash
git config --list
```

---

# 355. git init
## Description
Initialize a new Git repository.

```bash
git init
```

---

# 356. git clone
## Description
Clone an existing Git repository.

```bash
git clone https://github.com/user/repository.git
```

---

# 357. git status
## Description
Show the current repository status.

```bash
git status
```

---

# 358. git add
## Description
Stage a file for commit.

```bash
git add file.txt
```

---

# 359. git add .
## Description
Stage all modified files.

```bash
git add .
```

---

# 360. git restore
## Description
Restore working tree files.

```bash
git restore file.txt
```

---

# 361. git restore --staged
## Description
Unstage a file.

```bash
git restore --staged file.txt
```

---

# 362. git commit
## Description
Commit staged changes.

```bash
git commit -m "Initial commit"
```

---

# 363. git log
## Description
Display commit history.

```bash
git log
```

---

# 364. git log --oneline
## Description
Display concise commit history.

```bash
git log --oneline
```

---

# 365. git show
## Description
Display information about a commit.

```bash
git show
```

---

# 366. git diff
## Description
Show unstaged changes.

```bash
git diff
```

---

# 367. git diff --staged
## Description
Show staged changes.

```bash
git diff --staged
```

---

# 368. git branch
## Description
List all local branches.

```bash
git branch
```

---

# 369. git branch new-branch
## Description
Create a new branch.

```bash
git branch feature-login
```

---

# 370. git switch
## Description
Switch to another branch.

```bash
git switch feature-login
```

---

# 371. git switch -c
## Description
Create and switch to a new branch.

```bash
git switch -c feature-dashboard
```

---

# 372. git checkout
## Description
Switch branches (legacy command).

```bash
git checkout main
```

---

# 373. git merge
## Description
Merge another branch into the current branch.

```bash
git merge feature-login
```

---

# 374. git rebase
## Description
Reapply commits on top of another branch.

```bash
git rebase main
```

---

# 375. git remote -v
## Description
Display configured remote repositories.

```bash
git remote -v
```

---

# 376. git remote add origin
## Description
Add a remote repository.

```bash
git remote add origin https://github.com/user/repository.git
```

---

# 377. git push
## Description
Push commits to the remote repository.

```bash
git push origin main
```

---

# 378. git push -u origin main
## Description
Push and set upstream branch.

```bash
git push -u origin main
```

---

# 379. git pull
## Description
Fetch and merge changes from the remote repository.

```bash
git pull origin main
```

---

# 380. git fetch
## Description
Download changes without merging.

```bash
git fetch
```

---

# 381. git stash
## Description
Temporarily save uncommitted changes.

```bash
git stash
```

---

# 382. git stash pop
## Description
Restore the most recent stash.

```bash
git stash pop
```

---

# 383. git stash list
## Description
List all saved stashes.

```bash
git stash list
```

---

# 384. git tag
## Description
List all tags.

```bash
git tag
```

---

# 385. git tag v1.0
## Description
Create a lightweight tag.

```bash
git tag v1.0
```

---

# 386. git reset --soft
## Description
Move HEAD while keeping staged changes.

```bash
git reset --soft HEAD~1
```

---

# 387. git reset --mixed
## Description
Unstage commits while keeping file changes.

```bash
git reset --mixed HEAD~1
```

---

# 388. git reset --hard
## Description
Reset repository and discard changes.

```bash
git reset --hard HEAD
```

---

# 389. git revert
## Description
Create a new commit that reverses a previous commit.

```bash
git revert HEAD
```

---

# 390. git rm
## Description
Remove a tracked file.

```bash
git rm file.txt
```

---

# 391. git mv
## Description
Rename or move a tracked file.

```bash
git mv old.txt new.txt
```

---

# 392. git clean -fd
## Description
Remove untracked files and directories.

```bash
git clean -fd
```

---

# 393. git blame
## Description
Show who last modified each line of a file.

```bash
git blame README.md
```

---

# 394. git cherry-pick
## Description
Apply a specific commit.

```bash
git cherry-pick <commit_hash>
```

---

# 395. git reflog
## Description
Display reference log.

```bash
git reflog
```

---

# 396. git shortlog
## Description
Summarize commit history by author.

```bash
git shortlog
```

---

# 397. git archive
## Description
Create an archive from the repository.

```bash
git archive --format=zip HEAD -o project.zip
```

---

# 398. git describe
## Description
Show the nearest tag for a commit.

```bash
git describe
```

---

# 399. git gc
## Description
Clean up and optimize the repository.

```bash
git gc
```

---

# 400. git help
## Description
Display Git help documentation.

```bash
git help
```

---
