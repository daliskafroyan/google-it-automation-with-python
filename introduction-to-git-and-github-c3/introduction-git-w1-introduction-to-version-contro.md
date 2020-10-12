introduction-git-w1-introduction-to-version-control

# Introduction to Git and GitHub
## WEEK 1 - Introduction to Version Control

### **Before Version Control**
* * *
#### *Intro to Module 1: Version Control*
The most notable feature of the version control are rollback feature which you can use, as the name says, roll back to the previous version. Since you know that this version was working correctly before the change was made, it would be safe to go back to that one until you had time to fix the code, run some tests, and make sure everything works correctly for all machine models.

<br/>

#### *Diffing Files*
```bash
diff -u <pyfile1.py> <pyfile2.py>
```
diff -u is used to compare two files, line by line, and have the differing lines compared side-by-side in the same output

```bash
diff -u <old_file.txt> <new_file.txt> > change.diff
```
get the difference between those two file and redirect the result to change.diff file


#### *Applying Changes*
```bash
patch cpu_usage.py < cpu_usage.diff
```
apply the changes that come from cpu_usage.diff to cpu_usage.py

<br/>


### **Version Control Systems**
* * *
#### *What is Version Control?*
We can make edits to multiple files and treat that collection of edits as a single change which is commonly known as a, commit.
#### *What is Git?*
Git is a free open source system available for installation on Unix based platforms, Windows and macOS.

Git can work as a standalone program as a server and as a client. This means that you can use Git on a single machine without even having a network connection. Or you can use it as a server on a machine where you want to host your repository. And then you can use Git as a client to access the repository from another machine or even the same one.

#### *First Steps with Git*
```bash
git config –-global user.mail  “<me@example.com>”
git config –-global user.name  “<name>”
```
to config our identity for the first time
```bash
git config -l
```
to see the identity
```bash
git init
```
initialize git directory. Act as database of all change
```bash
git add <python_file.py>
```
added our file in staging area which is a file maintained by Git that contains all of the information about what files and change are going to go into your next commit
```bash
git commit
```
to put the code into git directory
#### *Tracking Files*
Files could have three stages: modified, staged, commited. After changing the file, stage those changes and commit them afterwards
```bash
git commit -m 
```
to add the comment
```bash
git log
```
to see the change history
