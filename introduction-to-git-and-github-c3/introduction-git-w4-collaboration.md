introduction-git-w4-collaboration

# Introduction to Git and GitHub
## WEEK 4 - Collaboration

### **Pull Requests**
* * *
#### *A Simple Pull Request on GitHub*
When collaborating on projects hosted on GitHub, the typical workflows, first, create a fork of the repo, and then work on that local fork. A forked repo is just like a normal repo, except Github knows which repo it forked from. So we can eventually merge our changes back into the main repo by creating a pull request. A pull request is a commit or series of commits that you send to the owner of the repository so that they incorporate it into their tree.
The easiest method to do the pull request are by editing directly from the window and click propose change button
It was called pull request because we request sent to the owner and the collaborators of the target repository to pull the recent changes you’ve made
The new fork created when you want to experiment with changes without affecting the main repo. For instance when you want to propose the changes to someone else’s project or base your own project off of theirs

#### *The Typical Pull Request Workflow on GitHub*
To do that, we'll normally have a local copy of the repo in our computer and work with the forked repo as a remote. Just modify the file as you need and do the process as we usually do in github

#### *Updating an Existing Pull Request*
When your pull request are being reviewed and need some more changes, just do the thing as usual as well. But make sure to read the guidelines, there are some project require you to rebase your code.

#### *Squashing Changes*
When we choose squash, the commit messages are added together and an editor opens up to let us make any necessary changes. When we choose fix up, the commit message for that commit is discarded. For our example, we want to use squash so that we can combine both commits but also modify the commit description.
```bash
git rebase -i master 
```
use interactive version of rebase to edit the commit messages
```bash
git push -f  
```
to push the changes as it is

<br/>

### **Code Reviews**
* * *
#### *What are code reviews?*
Doing a code review means going through someone else's code, documentation or configuration and checking that it all makes sense and follows the expected patterns. The goal of a code review is to improve the project by making sure that changes are high quality.
*The Code Review Workflow*

<br/>

### **Managing Projects**
* * *
### *Managing Collaboration*
Be truly understand the pull request, Quick in responding the pull request

### *Tracking Issues*
Adding the issues by going to issues tab and click the new issue button. Type 
```bash
close #(number-of-issue)
```
to close the issues immediately  once this commit is integrated into the main tree

#### *Continuous Integration*
Will build and test our code every time there’s a change. Once we have our code automatically built and tested, the next automation step is Continuous Delivery, where it’s updating with incremental rollouts. There are a bunch of concepts that you'll need to deal with when creating your own CICD. The first one is a concept of pipelines. Pipelines specify the steps that need to run to get the result you want.

