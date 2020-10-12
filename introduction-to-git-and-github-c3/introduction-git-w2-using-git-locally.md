introduction-git-w2-using-git-locally

# Introduction to Git and GitHub
## WEEK 1 - Using Git Locally
* * *
### **Advanced Git Interaction**
* * *
#### *Intro to Module 2: Using Git Locally*
We will use git’s ability to revert previous changes, branching to work on experimental feature without affecting the main code, etc.
#### *Skipping the Staging Area*
```bash
git commit -a -m “commit init”
```
a shortcut to stage any changes to tracked files and commit them in one step, skipping the staging stage step. It won’t work on new files because those are untracked. best for truly small changes
git uses HEAD alias to represent the currently checked-out snapshot of your project
#### *Getting More Information About Our Changes*
```bash
git log -p
```
shows added lines with plusses and remove lines with dashes
the difference is, adding -p flag to show associated patches
```bash
git log --stat
```
see which files were changed and how many lines were added or removed
```bash
git show <commit-id>
```
taking the commit ID, it will show information about the commit and it’s associated path

#### *Deleting and Renaming Files*
```bash
git rm <files>
```
delete file in repository

```bash
git mv <old_name> <new_name>
```
rename file in repository

<br/>

### **Undoing Things**
* * *
#### *Undoing Changes Before Committing*
```bash
git checkout all_check.py
```
reverting any changes before staging. restore the file to the latest storage snapshot
```bash
git reset HEAD output.txt
```
in this case, I want to exclude this output file to staging area, but we already add all of the file available with git add * command. Then how to undo it? Just use the command above to kick the files out of the staging area. You can think it as a counterpart of git add
#### *Amending Commits*
Think about you want to commit two files, but you forgot to include the other one to be commited to repository. Stage the file we forgot to be commited, and use -
```bash
git commit –amend
```
to modify and add changes to the most recent commit. Avoid amending commits that have already been made public
#### *Rollbacks*
```bash
git revert HEAD
```
a new commit is created with inverse changes. This cancels previous changes instead of making it as though the original commit never happened.
#### *Identifying a Commit*
The error also happened to be in the most recently created commit, but errors can sometimes take a while to be detected. And so, we might need to revert other commits farther back in time. We can target a specific commit by using its commit ID. The commit ID is the 40 character long string after the word commit, you really can't miss it. This long jumble of letters and numbers is actually something called a hash, which is calculated using an algorithm called SHA1
```bash
git log -2
```
logging the history in the latest two part
```bash
git revert <commit-id>
```
rolling back to specific part 

<br/>

### **Branching and Merging**
* * *
#### *What is a Branch?*
Branch is a pointer to a particular commit. The default branch that git creates for you when a new repository is initialized is called master. The master branch is commonly used to represent the known good state of a project. When you want to develop a feature or try something new in your project, you can create a separate branch to do your work without worrying about messing up this current working state.
#### *Creating New Branches*
```bash
git branch
```
to show all of the branch you have
```bash
git branch <new_branch> 
```
to create new branch called new_branch
```bash
git checkout new_branch
```
to move to new branch
```bash
git checkout -b new_super_branch
```
to create new branch and switches to it at the same time
#### *Working with Branches*
```bash
git branch -d <new_branch>
```
deleting new_branch branch
#### *Merging*
The typical workflow of using Git is to create a separate branch to developing any new features or changes. Once the new feature’s in good shape, we merge the separate branch back to main code. Merging is the term that Git uses for combining branch data and history together.
```bash
git merge new_super_branch
```
there are two algorithms used in to merge, the fast-forward and three-way merge
#### *Merge Conflicts*
If you have two files which both have the same changes applied, it would result in conflict when they got merged. To fix it, open up the conflicted file. Decide which content we should keep and delete the merger markers. Check the status of merging using *git status*
```bash
git log –graph –oneline 
```
to get the detailed information about the merging files. Summarized view of the commit history for a repo
```bash
git merge –abort
```
to throw away a merge and start over
